"""
FearFinder — A Flask-based phobia quiz application.

Progress is persisted with SQLAlchemy (SQLite) so users can:
  • close the browser and resume later,
  • finish only the questions they haven't answered yet,
  • automatically pick up new fears when they are added to fears.py.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_migrate import Migrate
from fears import FEARS
from models import db, User, Answer

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = Flask(__name__)
app.secret_key = "fearfinder-secret-key-change-in-production"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + os.path.join(basedir, "fearfinder.db")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# Quick look-up helpers built once at import time
FEAR_LOOKUP = {f["id"]: f for f in FEARS}
ALL_FEAR_IDS = {f["id"] for f in FEARS}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_or_create_user(name: str) -> User:
    """Return an existing User or create a new one (case-insensitive)."""
    user = User.query.filter(db.func.lower(User.name) == name.lower()).first()
    if user is None:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
    return user


def _unanswered_fears(user: User) -> list[dict]:
    """Return the list of FEARS dicts the user has NOT answered yet."""
    answered_ids = {a.fear_id for a in user.answers}
    return [f for f in FEARS if f["id"] not in answered_ids]


def _all_answers_for(user: User) -> list[dict]:
    """Return all of a user's answers as lightweight dicts."""
    return [
        {"fear_id": a.fear_id, "choice": a.choice}
        for a in user.answers
    ]


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    """Landing page — enter your name to start or continue the quiz."""
    user_id = session.get("user_id")
    user = None
    remaining = 0
    total_answered = 0

    if user_id:
        user = db.session.get(User, user_id)
        if user:
            remaining = len(_unanswered_fears(user))
            total_answered = len(user.answers)

    return render_template(
        "home.html",
        user=user,
        remaining=remaining,
        total_answered=total_answered,
        total=len(FEARS),
    )


@app.route("/start", methods=["POST"])
def start():
    """Capture the player's name and begin (or resume) the quiz."""
    name = request.form.get("name", "").strip()
    if not name:
        return redirect(url_for("home"))

    user = _get_or_create_user(name)
    session["user_id"] = user.id
    session["name"] = user.name

    unanswered = _unanswered_fears(user)
    if not unanswered:
        return redirect(url_for("results"))

    # Store the ordered list of fear IDs still to answer
    session["queue"] = [f["id"] for f in unanswered]
    session["queue_idx"] = 0
    return redirect(url_for("quiz"))


@app.route("/quiz")
def quiz():
    """Display the current unanswered fear's story and question."""
    if "user_id" not in session:
        return redirect(url_for("home"))

    queue = session.get("queue", [])
    idx = session.get("queue_idx", 0)

    if idx >= len(queue):
        return redirect(url_for("results"))

    fear_id = queue[idx]
    fear = FEAR_LOOKUP[fear_id]

    user = db.session.get(User, session["user_id"])
    total_answered = len(user.answers) if user else 0

    return render_template(
        "quiz.html",
        name=session["name"],
        fear=fear,
        current=total_answered + idx + 1,
        current_new=idx + 1,
        remaining=len(queue) - idx,
        total=len(FEARS),
        total_queue=len(queue),
        progress=round(((total_answered + idx) / len(FEARS)) * 100),
    )


@app.route("/answer", methods=["POST"])
def answer():
    """Record the user's answer to the DB and advance."""
    if "user_id" not in session:
        return redirect(url_for("home"))

    queue = session.get("queue", [])
    idx = session.get("queue_idx", 0)

    if idx >= len(queue):
        return redirect(url_for("results"))

    fear_id = queue[idx]
    chosen = int(request.form.get("option", 0))

    # Persist to the database
    existing = Answer.query.filter_by(
        user_id=session["user_id"], fear_id=fear_id
    ).first()
    if existing:
        existing.choice = chosen
    else:
        db.session.add(
            Answer(user_id=session["user_id"], fear_id=fear_id, choice=chosen)
        )
    db.session.commit()

    session["queue_idx"] = idx + 1

    if session["queue_idx"] >= len(queue):
        return redirect(url_for("results"))

    return redirect(url_for("quiz"))


@app.route("/results")
def results():
    """Tally up answers and show a personal fear profile."""
    if "user_id" not in session:
        return redirect(url_for("home"))

    user = db.session.get(User, session["user_id"])
    if not user:
        return redirect(url_for("home"))

    answers = _all_answers_for(user)
    name = user.name

    severe = []
    moderate = []
    mild = []
    no_fear = []

    for ans in answers:
        fear = FEAR_LOOKUP.get(ans["fear_id"])
        if fear is None:
            continue
        entry = {
            "name": fear["name"],
            "fear_of": fear["fear_of"],
            "choice": ans["choice"],
            "chosen_text": fear["options"][ans["choice"]],
        }
        if ans["choice"] == 0:
            severe.append(entry)
        elif ans["choice"] == 1:
            moderate.append(entry)
        elif ans["choice"] == 2:
            mild.append(entry)
        else:
            no_fear.append(entry)

    total_answered = len(answers)
    max_score = len(FEARS) * 3
    fear_score = round(
        ((len(severe) * 3 + len(moderate) * 2 + len(mild) * 1) / max_score) * 100
    ) if max_score else 0

    unanswered = _unanswered_fears(user)

    return render_template(
        "results.html",
        name=name,
        severe=severe,
        moderate=moderate,
        mild=mild,
        no_fear=no_fear,
        total=len(FEARS),
        total_answered=total_answered,
        unanswered_count=len(unanswered),
        fear_score=fear_score,
    )


@app.route("/reset", methods=["POST"])
def reset():
    """Delete all answers for the current user and start fresh."""
    if "user_id" in session:
        Answer.query.filter_by(user_id=session["user_id"]).delete()
        db.session.commit()
    session.clear()
    return redirect(url_for("home"))


# ---------------------------------------------------------------------------
# Bootstrap
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5001)
