"""
Database models for FearFinder.
"""

from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A quiz taker identified by a unique (case-insensitive) name."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    answers = db.relationship(
        "Answer", backref="user", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.name!r}>"


class Answer(db.Model):
    """A single recorded answer — one per (user, fear) pair."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    fear_id = db.Column(db.Integer, nullable=False)  # matches FEARS[n]["id"]
    choice = db.Column(db.Integer, nullable=False)    # 0-3
    answered_at = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    __table_args__ = (
        db.UniqueConstraint("user_id", "fear_id", name="uq_user_fear"),
    )

    def __repr__(self):
        return f"<Answer user={self.user_id} fear={self.fear_id} choice={self.choice}>"
