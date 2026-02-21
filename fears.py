"""
Complete collection of phobias/fears, each with a short illustrative story
and a quiz question.
"""

FEARS = [
    {
        "id": 1,
        "name": "Arachnophobia",
        "fear_of": "Spiders",
        "story": (
            "Maya was cleaning out the old garden shed when she reached behind a dusty "
            "shelf and felt something brush across her fingers — thin, quick, alive. She "
            "yanked her hand back and saw a massive brown spider clinging to the shelf edge, "
            "its legs spanning wider than her palm. It watched her with a cluster of dark "
            "eyes. She stumbled backward, knocking over a row of clay pots that shattered "
            "on the concrete floor. Her heart hammered. She couldn't go back inside the shed "
            "for three days."
        ),
        "question": "How would you react if a large spider suddenly appeared on your hand?",
        "options": [
            "I'd scream and shake it off in pure panic.",
            "I'd freeze for a moment, then calmly brush it away.",
            "I'd observe it curiously — spiders don't bother me.",
            "I'd feel uncomfortable but manage to deal with it.",
        ],
    },
    {
        "id": 2,
        "name": "Ophidiophobia",
        "fear_of": "Snakes",
        "story": (
            "Carlos was hiking along a narrow trail through tall grass when he heard a dry "
            "rattle — a sound like seeds shaking inside a gourd. He froze mid-step. Coiled "
            "on a sun-warmed rock inches from his boot was a rattlesnake, its forked tongue "
            "tasting the air. Carlos' legs turned to stone. Every childhood warning screamed "
            "inside his skull. He backed away one trembling inch at a time, not breathing "
            "until the trail curved out of sight."
        ),
        "question": "You're on a nature trail and a snake slithers across your path. What do you do?",
        "options": [
            "I'd turn around and run the other way.",
            "I'd stand still and wait for it to pass, but I'd be terrified.",
            "I'd calmly step aside and keep going.",
            "I'd be fascinated and try to get a closer look.",
        ],
    },
    {
        "id": 3,
        "name": "Acrophobia",
        "fear_of": "Heights",
        "story": (
            "Lena stepped onto the glass-floored observation deck on the 95th floor. The city "
            "spread out below her feet like a tiny model — cars the size of ants, people invisible. "
            "The glass was perfectly safe, an engineer had assured the group, but Lena's stomach "
            "dropped as though she were already falling. Her knees buckled. She grabbed the railing "
            "and pressed her back against the solid wall, refusing to look down again. Her friends "
            "laughed and waved from the center of the platform, but Lena couldn't move."
        ),
        "question": "You're invited to a rooftop restaurant with a glass floor high above the city. How do you feel?",
        "options": [
            "Absolutely not — I can't even think about it without feeling dizzy.",
            "I'd go but stay close to the walls the entire time.",
            "A little nervous, but the view would be worth it.",
            "Sounds exciting — I love heights!",
        ],
    },
    {
        "id": 4,
        "name": "Claustrophobia",
        "fear_of": "Confined spaces",
        "story": (
            "The elevator lurched and stopped between floors. The lights flickered, then dimmed "
            "to a pale emergency glow. David pressed the alarm button once, twice, ten times. "
            "Nothing. The walls seemed to inch closer. The air grew thick and warm. He loosened "
            "his collar, tried to slow his breathing, but each breath felt shallower than the last. "
            "Twenty minutes felt like twenty hours before the doors finally ground open and he "
            "stumbled into the lobby, shaking."
        ),
        "question": "An elevator you're in gets stuck between floors. How do you react?",
        "options": [
            "Full panic — I'd bang on the doors and scream for help.",
            "I'd feel extremely anxious but try to call for help calmly.",
            "I'd be annoyed but not particularly scared.",
            "I'd sit down and wait patiently — it'll get fixed.",
        ],
    },
    {
        "id": 5,
        "name": "Nyctophobia",
        "fear_of": "Darkness",
        "story": (
            "The power went out at 11 PM during the storm. Sophie reached for her phone but the "
            "battery was dead. The house was swallowed by an absolute blackness she had never "
            "experienced — no streetlights, no standby LEDs, nothing. Every creak of the old house "
            "became footsteps. Every gust against the window became a presence. She pressed herself "
            "into the corner of the couch with a blanket pulled over her head, waiting for dawn "
            "like a child afraid of monsters."
        ),
        "question": "The power goes out on a stormy night and you're alone. How do you handle it?",
        "options": [
            "I'd be terrified — the dark is my worst nightmare.",
            "I'd feel uneasy and immediately look for candles or a flashlight.",
            "I'd be a little spooked but mostly fine.",
            "I'd enjoy the atmosphere — storms in the dark are cozy.",
        ],
    },
    {
        "id": 6,
        "name": "Cynophobia",
        "fear_of": "Dogs",
        "story": (
            "When James was seven, a neighbor's German Shepherd broke free from its chain and "
            "charged at him. He still remembers the sound of its claws on the sidewalk, the bark "
            "that felt like a thunderclap. Now, at thirty-two, when a golden retriever puppy "
            "bounded toward him in the park, James' body reacted before his mind could: his pulse "
            "spiked, his hands flew up to shield his face, and he stepped behind his friend like "
            "a human shield. The puppy just wanted to lick his shoes."
        ),
        "question": "A friendly dog runs up to greet you in the park. What's your reaction?",
        "options": [
            "I'd step back immediately — dogs make me very nervous.",
            "I'd tense up but try to stay still.",
            "I'd cautiously pet it after a moment.",
            "I'd happily crouch down and play with it!",
        ],
    },
    {
        "id": 7,
        "name": "Astraphobia",
        "fear_of": "Thunder and lightning",
        "story": (
            "The sky split open with a crack so loud the windows rattled. Lightning turned the "
            "bedroom white for a split second, then darkness slammed back. Alex dove under the "
            "covers. Another boom rolled through the house like a freight train. She pressed her "
            "palms against her ears, counting the seconds between flash and thunder, praying "
            "the storm was moving away. It wasn't. For two hours she lay rigid, flinching at "
            "every strike."
        ),
        "question": "A violent thunderstorm rolls in while you're at home. How do you react?",
        "options": [
            "I'd hide somewhere and cover my ears until it passes.",
            "I'd close the curtains and try to distract myself.",
            "A bit jumpy but mostly fine watching from inside.",
            "I'd stand at the window and watch — storms are amazing.",
        ],
    },
    {
        "id": 8,
        "name": "Trypanophobia",
        "fear_of": "Needles / Injections",
        "story": (
            "The nurse smiled and said, 'Just a little pinch.' But Marcus had already turned pale. "
            "He gripped the armrest so hard his knuckles went white. He couldn't look at the "
            "silver tray with its neat row of syringes. When the nurse swabbed his arm with the "
            "cold alcohol wipe, the room tilted. 'Deep breaths,' she said. Marcus took one breath "
            "and fainted straight off the chair."
        ),
        "question": "You need to get a blood test. How do you feel about it?",
        "options": [
            "I dread it for days and might even cancel the appointment.",
            "I'm very nervous but I force myself to go through with it.",
            "Slightly uncomfortable, but it's no big deal.",
            "Doesn't bother me at all.",
        ],
    },
    {
        "id": 9,
        "name": "Aerophobia",
        "fear_of": "Flying",
        "story": (
            "The plane hit a pocket of turbulence and dropped. Passengers gasped. Rachel's "
            "knuckles went white around both armrests. She squeezed her eyes shut and whispered "
            "numbers — counting to ten, starting over, counting again. The seatbelt sign dinged "
            "on. Another jolt. She was convinced, absolutely certain, that the wings were tearing "
            "off. Her seatmate offered her a mint. She couldn't unclench her jaw to accept it."
        ),
        "question": "You have the chance to fly somewhere for a dream vacation. How do you feel about the flight?",
        "options": [
            "I'd seriously consider driving instead, no matter how far.",
            "I'd fly, but I'd need medication or a drink to cope.",
            "A little anxious at takeoff, but fine once we're cruising.",
            "Love flying — window seat, please!",
        ],
    },
    {
        "id": 10,
        "name": "Glossophobia",
        "fear_of": "Public speaking",
        "story": (
            "Priya had rehearsed the presentation forty times. She knew every slide, every "
            "transition. But when she walked to the podium and saw three hundred faces staring "
            "back, her mind went blank. Her mouth dried up. The first sentence came out as a "
            "whisper. She felt the heat crawling up her neck, the tremor in her hands visible "
            "even from the back row. She powered through on autopilot, but afterward she couldn't "
            "remember a single word she'd said."
        ),
        "question": "You're asked to give a speech at a large event. How do you respond?",
        "options": [
            "I'd decline — I physically cannot speak in front of crowds.",
            "I'd accept but agonize over it for weeks beforehand.",
            "I'd be nervous but manage once I got started.",
            "I'd enjoy it — I'm comfortable in front of crowds.",
        ],
    },
    {
        "id": 11,
        "name": "Trypophobia",
        "fear_of": "Clusters of small holes",
        "story": (
            "Mia was scrolling through a nature documentary page when she saw a close-up of a "
            "lotus seed pod — dozens of small, dark holes packed tightly together. Her skin "
            "crawled instantly. It felt like thousands of tiny insects were marching under her "
            "flesh. She slammed the laptop shut and rubbed her arms furiously, but the phantom "
            "sensation lingered for hours. She couldn't eat dinner."
        ),
        "question": "You see an image of tightly clustered small holes (like a honeycomb or seed pod). How does it make you feel?",
        "options": [
            "Deeply disturbed — it makes my skin crawl.",
            "Uncomfortable and I'd look away quickly.",
            "Slightly odd feeling, but nothing major.",
            "Doesn't affect me at all.",
        ],
    },
    {
        "id": 12,
        "name": "Agoraphobia",
        "fear_of": "Open or crowded spaces",
        "story": (
            "Daniel hadn't left his apartment in three weeks. The thought of the sprawling "
            "parking lot, the open sky, the unpredictable crowd at the grocery store made his "
            "chest tighten. His friend offered to go with him, to be right beside him. Daniel "
            "got as far as the front door, hand on the knob, before the wave hit — dizziness, "
            "nausea, the certainty that something terrible would happen the moment he stepped "
            "outside. He let go of the knob and sat down on the floor."
        ),
        "question": "You're invited to an outdoor festival with thousands of people. What's your reaction?",
        "options": [
            "I couldn't go — wide open crowded spaces overwhelm me completely.",
            "I'd try but might need to leave early if it gets too much.",
            "I'd feel a bit anxious but would push through and enjoy it.",
            "Sounds like a great time — count me in!",
        ],
    },
    {
        "id": 13,
        "name": "Mysophobia",
        "fear_of": "Germs and contamination",
        "story": (
            "Elena watched the man on the subway cough into his hand, then grab the pole she'd "
            "been holding. She released it immediately, tucking her hands into her sleeves. At "
            "home she scrubbed her hands seven times, each wash lasting exactly sixty seconds, "
            "until the skin was raw and red. She changed her clothes, wiped down her phone, her "
            "keys, her wallet. Only then, two hours later, did her heartbeat return to normal."
        ),
        "question": "Someone near you sneezes without covering their mouth. How do you react?",
        "options": [
            "I'd feel contaminated and need to sanitize everything immediately.",
            "I'd be disgusted and move away as fast as possible.",
            "I'd be mildly annoyed but not overly worried.",
            "It wouldn't really bother me.",
        ],
    },
    {
        "id": 14,
        "name": "Aquaphobia",
        "fear_of": "Water",
        "story": (
            "The lake looked peaceful enough from the dock. But when Kai's friends jumped in, "
            "splashing and laughing, he sat frozen on the wooden planks. The dark water below "
            "hid everything — weeds, rocks, depth. He couldn't see the bottom. What was down "
            "there? His breath quickened. Even when the water only reached his friends' waists, "
            "Kai couldn't make himself step off the dock. He said he was fine just watching."
        ),
        "question": "Friends invite you to swim in a lake. How do you feel?",
        "options": [
            "No way — I'm terrified of water, especially when I can't see the bottom.",
            "I might wade in up to my knees, but no deeper.",
            "A little nervous, but I'd jump in after a moment.",
            "I'd dive right in — love swimming!",
        ],
    },
    {
        "id": 15,
        "name": "Thanatophobia",
        "fear_of": "Death",
        "story": (
            "It always hit Ryan at 3 AM. Lying in the dark, staring at the ceiling, the thought "
            "would creep in: one day, this ends. Not just sleep — everything. Consciousness. "
            "Memories. The thought was so large, so absolute, that it felt like falling into a "
            "void. His chest would tighten, his breathing would stall, and he'd have to sit up "
            "and turn on every light in the room just to feel real again."
        ),
        "question": "How do you feel when you think about mortality and the concept of death?",
        "options": [
            "It fills me with overwhelming dread — I try never to think about it.",
            "It makes me very anxious and uneasy.",
            "It's uncomfortable, but I can process it rationally.",
            "I've made peace with it — it's a natural part of life.",
        ],
    },
    {
        "id": 16,
        "name": "Entomophobia",
        "fear_of": "Insects",
        "story": (
            "The cockroach appeared from under the fridge like a small armored tank. It moved "
            "fast — too fast — across the kitchen floor toward Nora's bare feet. She leaped "
            "onto the counter with a shriek that brought the neighbors knocking. It took her "
            "husband twenty minutes to find and remove the roach. Nora didn't step on the kitchen "
            "floor without shoes for six months after that."
        ),
        "question": "A large beetle flies into your room and lands on your desk. What do you do?",
        "options": [
            "I'd leave the room immediately and get someone else to deal with it.",
            "I'd be really uncomfortable but try to shoo it out with something long.",
            "I'd calmly trap it in a cup and release it outside.",
            "I'd pick it up without a second thought.",
        ],
    },
    {
        "id": 17,
        "name": "Hemophobia",
        "fear_of": "Blood",
        "story": (
            "Oliver nicked his finger while slicing tomatoes. A thin line of red welled up — "
            "nothing serious, barely a paper cut. But the sight of that crimson bead sent a wave "
            "of nausea crashing through him. The kitchen tilted. He sat down hard on the floor, "
            "head between his knees, breathing in counts of four. His wife found him there five "
            "minutes later, still unable to look at his own finger."
        ),
        "question": "You get a small cut and see blood. How do you react?",
        "options": [
            "I feel faint or nauseous at the sight of even a little blood.",
            "I'd feel queasy but could put a bandage on it.",
            "I'd clean it up without much thought.",
            "Blood doesn't bother me in the slightest.",
        ],
    },
    {
        "id": 18,
        "name": "Coulrophobia",
        "fear_of": "Clowns",
        "story": (
            "The birthday party was supposed to be fun. But when the clown walked in with that "
            "painted grin stretching ear to ear and those oversized shoes slapping the floor, "
            "eight-year-old Toby ran behind the couch. Now, twenty years later, Toby still "
            "changes the channel when a clown appears on screen. Something about the frozen "
            "smile hiding a real face underneath makes his throat tighten."
        ),
        "question": "You're at an event and a clown approaches you to make balloon animals. How do you feel?",
        "options": [
            "Genuinely frightened — clowns terrify me.",
            "Very uneasy — I'd avoid eye contact and move away.",
            "Slightly creeped out, but I can deal with it.",
            "I think clowns are fun or at least harmless.",
        ],
    },
    {
        "id": 19,
        "name": "Dentophobia",
        "fear_of": "Dentists",
        "story": (
            "The dentist's waiting room had calming music and pastel walls, but Sarah's palms "
            "were drenched. The sound of the drill from behind the door hit her like a siren. "
            "She'd postponed this appointment four times already, letting a small cavity become "
            "a throbbing infection. When the hygienist called her name, Sarah stood up, walked "
            "three steps toward the door, turned around, and walked out of the building."
        ),
        "question": "It's time for your six-month dental checkup. How do you feel?",
        "options": [
            "I skip them entirely — I can't handle the dentist.",
            "I go but I'm a wreck the entire time.",
            "A little nervous, but I sit through it fine.",
            "No issue at all — dentist visits don't bother me.",
        ],
    },
    {
        "id": 20,
        "name": "Social Phobia",
        "fear_of": "Social situations",
        "story": (
            "The party was just ten people — close friends, supposedly a safe space. But when "
            "Tyler walked in and everyone turned to say hello, he felt like a spotlight was "
            "burning through him. Every word he said sounded wrong in his own ears. He overthought "
            "each sentence before speaking, and the delay made conversations awkward. After "
            "thirty minutes he invented an emergency text and left, relief flooding him the "
            "moment his car door closed."
        ),
        "question": "You're invited to a small gathering where you only know a few people. How do you feel?",
        "options": [
            "I'd probably decline — social situations drain and frighten me.",
            "I'd go but spend most of the time dreading conversations.",
            "A bit nervous at first, but I warm up.",
            "I love meeting new people — sounds great!",
        ],
    },
    {
        "id": 21,
        "name": "Emetophobia",
        "fear_of": "Vomiting",
        "story": (
            "One whiff of someone feeling sick on the bus and Grace's whole body went into "
            "alert mode. She pressed against the window, breathing through her sleeve. She "
            "skipped meals when her stomach felt even slightly off. She avoided restaurants, "
            "roller coasters, and boats — anything that might trigger nausea. The fear of throwing "
            "up controlled more of her daily decisions than she'd ever admit."
        ),
        "question": "Someone next to you says they feel nauseous. What do you do?",
        "options": [
            "I'd immediately leave — the thought of vomiting terrifies me.",
            "I'd distance myself and feel intensely anxious.",
            "I'd be somewhat concerned but try to help.",
            "I'd help them without much personal distress.",
        ],
    },
    {
        "id": 22,
        "name": "Necrophobia",
        "fear_of": "Dead things / Death-related objects",
        "story": (
            "At the open-casket funeral, everyone filed past to pay respects. But when it was "
            "Lin's turn, she couldn't approach the casket. The waxen stillness of the body, the "
            "unnatural pose, the makeup trying to mimic life — it sent ice through her veins. "
            "She sat in the back pew, staring at the floor, unable to look toward the front of "
            "the room for the entire service."
        ),
        "question": "How would you feel about attending an open-casket funeral?",
        "options": [
            "I couldn't do it — dead bodies are deeply disturbing to me.",
            "I'd attend but avoid looking at the casket.",
            "It's somber, but I can handle it.",
            "It doesn't disturb me — it's a natural part of saying goodbye.",
        ],
    },
    {
        "id": 23,
        "name": "Pyrophobia",
        "fear_of": "Fire",
        "story": (
            "The campfire crackled and everyone moved closer for warmth. Everyone except Hana. "
            "She sat three log-lengths back, watching the sparks drift upward like tiny threats. "
            "When a log shifted and sent a shower of embers into the air, she flinched so hard "
            "she spilled her drink. Her friends thought she was being dramatic. Hana knew the "
            "scar on her arm — from a kitchen accident at age five — was reason enough."
        ),
        "question": "You're at a campfire and someone throws more wood on, making it flare up. How do you react?",
        "options": [
            "I'd move far away immediately — fire terrifies me.",
            "I'd scoot back nervously and keep a wary eye on it.",
            "I'd be cautious but not overly worried.",
            "I love campfires — the bigger the better.",
        ],
    },
    {
        "id": 24,
        "name": "Athazagoraphobia",
        "fear_of": "Being forgotten or ignored",
        "story": (
            "It started when Damon's friends planned a trip and forgot to invite him. He only "
            "found out from photos on social media — everyone laughing, together, without him. "
            "The knot in his stomach wasn't just disappointment; it was terror. What if they'd "
            "all moved on? What if he simply stopped mattering? He checked his phone every ten "
            "minutes after that, measuring his worth in reply times and message counts."
        ),
        "question": "Your friends go out without inviting you and you see it on social media. How does it affect you?",
        "options": [
            "It devastates me — I feel like I'm being erased.",
            "It really hurts, and I'd obsess over why I wasn't included.",
            "I'd feel left out but move on pretty quickly.",
            "I wouldn't mind much — they probably just forgot.",
        ],
    },
    {
        "id": 25,
        "name": "Autophobia",
        "fear_of": "Being alone",
        "story": (
            "When Ava's roommate moved out, the silence of the empty apartment was deafening. "
            "She filled every moment with podcasts, phone calls, TV — anything to mimic the "
            "presence of another person. But at night, when the noise stopped and the apartment "
            "was just her, the loneliness felt like a physical weight on her chest. She started "
            "sleeping at friends' places, unable to face the empty rooms."
        ),
        "question": "You have to spend a full weekend completely alone at home. How do you feel?",
        "options": [
            "It terrifies me — I can't stand being completely alone.",
            "I'd manage, but I'd feel very anxious and lonely.",
            "I'd be fine — maybe a little bored.",
            "I'd love it — alone time is my favorite.",
        ],
    },
    {
        "id": 26,
        "name": "Xenophobia",
        "fear_of": "Strangers or the unknown",
        "story": (
            "When the new family moved in next door, the whole neighborhood went to welcome them. "
            "But Gene stayed behind his curtain, watching. Their language was different, their "
            "food smelled unfamiliar, their customs were strange. Gene knew, rationally, that "
            "they were just people — but the unfamiliarity triggered something primitive in him, "
            "a wall he couldn't explain. It took him months before he could wave back."
        ),
        "question": "You're placed in a group project with people from very different backgrounds. How do you feel?",
        "options": [
            "Very anxious — unfamiliar people and customs unsettle me deeply.",
            "Uncomfortable at first, but I'd try to push past it.",
            "A little outside my comfort zone, but mostly okay.",
            "Excited — I enjoy learning about different perspectives.",
        ],
    },
    {
        "id": 27,
        "name": "Phasmophobia",
        "fear_of": "Ghosts",
        "story": (
            "The old house creaked at night — every old house does. But when Sam heard what "
            "sounded like footsteps in the hallway and found no one there, rational explanations "
            "evaporated. He checked every room, every closet. Nothing. But the sense of a presence "
            "remained — cold, watchful. He left every light on and slept with the TV blaring, "
            "because the silence felt like something was listening."
        ),
        "question": "You're staying overnight in a house that locals say is haunted. How does that make you feel?",
        "options": [
            "I absolutely would not stay — ghosts or not, it's terrifying.",
            "I'd stay but sleep with all the lights on, very on edge.",
            "A bit creeped out, but it's just a house.",
            "I'd love the experience — ghost stories are fun, not scary.",
        ],
    },
    {
        "id": 28,
        "name": "Thalassophobia",
        "fear_of": "Deep ocean / Large bodies of water",
        "story": (
            "The boat stopped in the middle of the ocean for a snorkeling break. Everyone grabbed "
            "their gear and jumped in. But when Maria looked over the edge and saw nothing but "
            "bottomless, dark blue stretching into infinity below, her breath caught. The depth "
            "was incomprehensible — miles of water hiding things she couldn't see. She stayed on "
            "the boat, gripping the railing, unable to put even a toe in that void."
        ),
        "question": "You're on a boat in the deep ocean and invited to snorkel. How do you react?",
        "options": [
            "No chance — the thought of deep water beneath me is paralyzing.",
            "I'd be extremely nervous and probably stay on the boat.",
            "I'd be a little uneasy but give it a try.",
            "I'd jump right in — the ocean is incredible.",
        ],
    },
    {
        "id": 29,
        "name": "Chronophobia",
        "fear_of": "The passage of time",
        "story": (
            "Every New Year's Eve, while everyone celebrated, Jordan felt a creeping dread. "
            "Another year gone. Time slipping through her fingers like sand. She would stare at "
            "clocks sometimes, watching the second hand tick, overwhelmed by the relentless, "
            "unstoppable forward march. Birthdays weren't celebrations — they were reminders that "
            "the countdown was always running."
        ),
        "question": "How do you feel when you realize another year has passed?",
        "options": [
            "It fills me with dread — time passing terrifies me.",
            "It makes me anxious — I feel like I'm running out of time.",
            "A bit reflective, but mostly I look forward.",
            "I welcome it — each year brings new experiences.",
        ],
    },
    {
        "id": 30,
        "name": "Nosocomephobia",
        "fear_of": "Hospitals",
        "story": (
            "The antiseptic smell hit Marcus the moment the automatic doors opened. White walls, "
            "fluorescent lights, beeping machines. He was only visiting a friend recovering from "
            "a minor surgery, but his body responded as if he were the patient. His palms went "
            "clammy, the corridor seemed to narrow, and every passing gurney made his stomach "
            "lurch. He left his friend a text from the parking lot: 'Sorry, I couldn't come in.'"
        ),
        "question": "A friend is in the hospital and asks you to visit. How do you feel about going?",
        "options": [
            "I can't — hospitals make me feel like I'm going to collapse.",
            "I'd force myself to go but feel sick the whole time.",
            "I'd be slightly uncomfortable but manage fine.",
            "Hospitals don't bother me at all.",
        ],
    },
    {
        "id": 31,
        "name": "Atychiphobia",
        "fear_of": "Failure",
        "story": (
            "Eve stared at the blank application form for the dream job. She had the qualifications, "
            "the experience, the recommendations. But a voice inside her whispered: what if you're not "
            "good enough? What if you try and fail in front of everyone? The fear of rejection was so "
            "paralyzing that she closed the application window and told herself she'd do it tomorrow. "
            "Tomorrow became next week. Next week became never."
        ),
        "question": "There's an opportunity for something you really want, but you might fail. What do you do?",
        "options": [
            "I wouldn't try — the possibility of failure is too overwhelming.",
            "I'd agonize over it and might not follow through.",
            "I'd be nervous but go for it anyway.",
            "Failure doesn't scare me — it's part of the process.",
        ],
    },
    {
        "id": 32,
        "name": "Philophobia",
        "fear_of": "Falling in love",
        "story": (
            "After the third date, when things were going perfectly, that familiar panic set in. "
            "Kai could feel themselves getting attached, and that was the danger. Attachment meant "
            "vulnerability. Vulnerability meant pain. They'd been through it before — the devastating "
            "heartbreak that made them question everything. So Kai stopped responding to messages, "
            "canceled plans, pulled away. Better to be alone than to risk that kind of hurt again."
        ),
        "question": "You notice you're developing strong feelings for someone. How do you react?",
        "options": [
            "I'd pull away — falling in love feels too dangerous.",
            "I'd feel excited but also deeply anxious about getting hurt.",
            "I'd cautiously explore the feelings.",
            "I'd embrace it fully — love is always worth the risk.",
        ],
    },
    {
        "id": 33,
        "name": "Zoophobia",
        "fear_of": "Animals in general",
        "story": (
            "At the petting zoo, children ran from pen to pen, giggling and feeding goats from "
            "their palms. But Rami stood outside the fence, watching with wide eyes. The goat's "
            "rectangular pupils, the chicken's jerky head movements, the rabbit's unpredictable "
            "hops — every animal seemed alien and threatening. His daughter tugged his hand, "
            "begging him to come in. He knelt down and said, 'You go ahead, sweetheart. Daddy "
            "will watch from here.'"
        ),
        "question": "You're visiting a petting zoo with friendly farm animals. How do you feel?",
        "options": [
            "I'd stay outside the enclosure — animals in general make me uneasy.",
            "I'd go in but avoid touching any of them.",
            "I'd cautiously interact with the calmer animals.",
            "I'd love it — animals are wonderful!",
        ],
    },
    {
        "id": 34,
        "name": "Tokophobia",
        "fear_of": "Pregnancy and childbirth",
        "story": (
            "Watching the documentary about childbirth in health class changed something in "
            "Layla permanently. The sounds, the pain, the loss of control over one's own body — "
            "it wasn't beautiful to her, it was horrifying. Years later, when friends excitedly "
            "shared pregnancy announcements, Layla smiled and congratulated them, but inside "
            "she felt a wave of dread just imagining it for herself."
        ),
        "question": "How do you feel when you see detailed depictions of childbirth?",
        "options": [
            "Deeply terrified — it's one of my biggest fears.",
            "Very uncomfortable and anxious.",
            "A bit squeamish, but it's natural.",
            "It doesn't bother me — it's a miracle of life.",
        ],
    },
    {
        "id": 35,
        "name": "Technophobia",
        "fear_of": "Technology",
        "story": (
            "The company switched to a new computer system overnight. Brenda stared at the "
            "unfamiliar interface, her hands hovering above the keyboard like it might bite. "
            "Every click felt like it could break something irreversible. When a dialog box "
            "appeared asking her to 'confirm action,' she froze — what action? What would happen? "
            "She called IT seven times that first week, each time apologizing for being 'hopeless.'"
        ),
        "question": "You need to use a brand-new software system at work with no training. How do you feel?",
        "options": [
            "Panicked — new technology overwhelms and scares me.",
            "Very stressed — I'd need lots of help to get started.",
            "A bit frustrated, but I'd figure it out.",
            "Excited — I love learning new tech.",
        ],
    },
    {
        "id": 36,
        "name": "Catoptrophobia",
        "fear_of": "Mirrors",
        "story": (
            "It always happened late at night. Passing the bathroom mirror, Ben would catch his "
            "own reflection and for a split second — just a fraction — it looked wrong. The eyes "
            "seemed to linger a beat too long, the smile slightly out of sync with his own. "
            "Rationally, he knew it was just his reflection. But he'd covered the hallway mirror "
            "with a towel anyway. Just in case."
        ),
        "question": "You're in a dimly lit room and catch your reflection unexpectedly. How do you react?",
        "options": [
            "I'd be genuinely scared — mirrors unsettle me deeply.",
            "I'd feel a chill and look away quickly.",
            "A brief startle, nothing more.",
            "I wouldn't think twice about it.",
        ],
    },
    {
        "id": 37,
        "name": "Pogonophobia",
        "fear_of": "Beards",
        "story": (
            "In crowded places, Lily found her eyes drawn to faces with thick beards — not out of "
            "admiration, but unease. Something about the way a beard concealed the jaw, obscured "
            "expressions, and hid the face beneath made her deeply uncomfortable. When her cousin "
            "grew a full beard over winter, she couldn't look at him the same way. She knew it was "
            "irrational. That didn't make the discomfort go away."
        ),
        "question": "You're introduced to someone with a very large, thick beard. How do you feel?",
        "options": [
            "Genuinely uncomfortable — beards disturb me.",
            "Slightly uneasy but I can manage.",
            "I notice it but feel nothing particular.",
            "I think beards are great — no issue at all.",
        ],
    },
    {
        "id": 38,
        "name": "Ombrophobia",
        "fear_of": "Rain",
        "story": (
            "The forecast said rain, and just seeing the word on her phone app made Jess tense up. "
            "She hated the sound of it against the windows, the way it blurred the world outside, "
            "the feeling of being trapped indoors by an endless grey curtain. When an unexpected "
            "shower caught her walking home, she ran to the nearest awning and stood there for "
            "forty minutes rather than walk two blocks in the rain."
        ),
        "question": "It starts raining unexpectedly while you're outside. How do you react?",
        "options": [
            "I'd seek shelter immediately — rain makes me extremely anxious.",
            "I'd feel very uncomfortable and rush to get inside.",
            "I'd be mildly annoyed but keep going.",
            "I'd enjoy it — rain is refreshing!",
        ],
    },
    {
        "id": 39,
        "name": "Nomophobia",
        "fear_of": "Being without a mobile phone",
        "story": (
            "When Aaron realized he'd left his phone at the restaurant, the reaction was instant "
            "and physical. Racing heart, sweating palms, a hollow pit in his stomach. He drove "
            "back at twice the speed limit. It wasn't about the expensive device — it was the "
            "disconnection. No messages, no maps, no way to call for help. For those fifteen "
            "minutes, he felt as exposed and vulnerable as if he'd lost a limb."
        ),
        "question": "You realize you left your phone at home and won't be able to get it for hours. How do you feel?",
        "options": [
            "Panicked — I feel completely lost without my phone.",
            "Very anxious — I'd keep thinking about it all day.",
            "Mildly inconvenienced, but I'd manage.",
            "Relieved, actually — a nice break from screens.",
        ],
    },
    {
        "id": 40,
        "name": "Megalophobia",
        "fear_of": "Large objects",
        "story": (
            "The cargo ship loomed over the harbor like a rusted mountain. Standing on the dock, "
            "Felix craned his neck and felt his sense of scale shatter. The hull stretched so far "
            "in both directions it stopped looking like something humans built and started looking "
            "like something alive. His legs felt weak. The sheer impossible size of the thing "
            "pressed down on him like gravity had doubled."
        ),
        "question": "You're standing near a massive structure — a huge dam, ship, or statue. How do you feel?",
        "options": [
            "Overwhelmed and frightened by the sheer scale.",
            "Uneasy — very large things make me uncomfortable.",
            "Impressed but not bothered.",
            "Awed and excited — I love huge structures!",
        ],
    },
    {
        "id": 41,
        "name": "Iatrophobia",
        "fear_of": "Doctors",
        "story": (
            "The doctor's office was bright and clean, decorated with calming watercolor prints. "
            "But for Maya, stepping through that door triggered a cascade of dread. The white coat, "
            "the stethoscope, the clipboard with its mysterious notes — every element felt like a "
            "prelude to bad news. She'd ignored a persistent cough for three months rather than "
            "make an appointment. 'It's probably nothing,' she told herself each morning, coughing "
            "harder than the day before."
        ),
        "question": "You've had a persistent symptom and should see a doctor. How do you feel about making the appointment?",
        "options": [
            "I'd avoid it as long as possible — doctors terrify me.",
            "I'd eventually go but with extreme reluctance and anxiety.",
            "I'd go fairly promptly, maybe a little nervous.",
            "I'd book it right away — better safe than sorry.",
        ],
    },
    {
        "id": 42,
        "name": "Decidophobia",
        "fear_of": "Making decisions",
        "story": (
            "The waiter came back for the third time. 'Have you decided?' he asked with a "
            "professional smile that was starting to strain. Omar stared at the menu, paralyzed. "
            "The pasta could be wrong. The steak could be overcooked. What if he ordered the salad "
            "and regretted it? Every choice felt like a trap with consequences he couldn't predict. "
            "His friends ordered for him in the end, and even then he felt a vague sense of failure."
        ),
        "question": "You're faced with an important life decision with multiple options. How do you handle it?",
        "options": [
            "I freeze — making decisions fills me with dread.",
            "I agonize for a very long time and often ask others to decide for me.",
            "I deliberate carefully but eventually commit.",
            "I trust my gut and decide confidently.",
        ],
    },
    {
        "id": 43,
        "name": "Somniphobia",
        "fear_of": "Sleep",
        "story": (
            "Most people looked forward to bedtime. For Claire, it was the worst part of the day. "
            "Lying down meant surrendering control — to nightmares, to sleep paralysis, to the "
            "terrifying moment of consciousness dissolving into nothing. She drank coffee until "
            "midnight, binged shows until her eyes burned, anything to delay the inevitable moment "
            "when she had to close her eyes and let the darkness take over."
        ),
        "question": "How do you feel when it's time to go to sleep at night?",
        "options": [
            "I dread it — falling asleep scares me.",
            "I feel anxious and often stall before going to bed.",
            "I'm usually fine, maybe occasionally restless.",
            "I love sleep — my head hits the pillow and I'm out.",
        ],
    },
    {
        "id": 44,
        "name": "Ergophobia",
        "fear_of": "Work or the workplace",
        "story": (
            "Every Sunday evening, Jake's stomach turned to lead. The thought of Monday morning — "
            "the commute, the emails, the meetings, the performance reviews — triggered a physical "
            "response he couldn't control. It wasn't laziness. He wanted to contribute. But the "
            "workplace felt like a minefield of judgment, deadlines, and potential humiliation. "
            "He called in sick more often than he could afford to."
        ),
        "question": "How do you feel Sunday evening thinking about the work week ahead?",
        "options": [
            "Severely anxious — it's almost paralyzing.",
            "Very stressed — the thought of work fills me with dread.",
            "A little unenthusiastic, but I'm okay.",
            "I look forward to it — I enjoy my work.",
        ],
    },
    {
        "id": 45,
        "name": "Gamophobia",
        "fear_of": "Marriage or commitment",
        "story": (
            "When his girlfriend mentioned moving in together, Jason felt ice in his veins. It "
            "wasn't that he didn't love her — he did, deeply. But the word 'together' implied "
            "permanence, and permanence implied a cage. He'd seen his parents' miserable marriage, "
            "the slow erosion of two people who once loved each other. The closer he got to someone, "
            "the louder the alarm bells rang: this will end badly."
        ),
        "question": "How do you feel about the idea of lifelong commitment or marriage?",
        "options": [
            "It terrifies me — I feel trapped by the very concept.",
            "I want it in theory but the idea fills me with deep anxiety.",
            "A little nervous, but I see it as a positive thing.",
            "I'm all for it — commitment brings security and joy.",
        ],
    },
    {
        "id": 46,
        "name": "Gerascophobia",
        "fear_of": "Growing old",
        "story": (
            "Vera found the first grey hair at twenty-eight. Most people would shrug. Vera cried. "
            "Not out of vanity, but from a deep, existential terror. Grey hair meant time was "
            "passing. Wrinkles meant decay. She spent hours researching anti-aging products, not "
            "to look young but to feel like she could slow the inevitable march toward frailty "
            "and irrelevance."
        ),
        "question": "How do you feel about the physical signs of aging (grey hair, wrinkles, etc.)?",
        "options": [
            "It fills me with genuine terror.",
            "It makes me quite anxious and I try to fight against it.",
            "It bothers me a little, but I accept it.",
            "I embrace aging — it's a sign of a life well-lived.",
        ],
    },
    {
        "id": 47,
        "name": "Eisoptrophobia",
        "fear_of": "Seeing yourself in a mirror (self-image)",
        "story": (
            "There was a time when Milo could look in the mirror without flinching. But somewhere "
            "along the way, his reflection became a stranger — one he didn't like. Every glance "
            "revealed flaws he couldn't unsee: the wrong proportions, the asymmetry, the gap "
            "between who he wanted to be and who stared back. He started getting dressed in the "
            "dark, brushing his teeth without looking up."
        ),
        "question": "How do you feel when you look at yourself in the mirror?",
        "options": [
            "I avoid mirrors — seeing my reflection causes intense distress.",
            "I feel very uncomfortable and critical of what I see.",
            "I have moments of self-doubt but I'm mostly okay with it.",
            "I'm comfortable with my reflection.",
        ],
    },
    {
        "id": 48,
        "name": "Wiccaphobia",
        "fear_of": "Witchcraft or the supernatural",
        "story": (
            "When their roommate started collecting crystals and reading tarot cards, Pat told "
            "themselves it was harmless. But the Ouija board was too much. Even sitting near it "
            "made Pat's skin prickle. The idea that unseen forces could be invoked — spirits, "
            "energy, anything beyond the explainable — triggered a primal fear Pat couldn't "
            "rationalize away. They moved out the following month."
        ),
        "question": "A friend wants to do a tarot reading or use a Ouija board. How do you feel?",
        "options": [
            "Absolutely not — I'm genuinely scared of supernatural forces.",
            "Very uneasy — I'd rather not be around it.",
            "Skeptical but slightly intrigued.",
            "I think it's fun — let's do it!",
        ],
    },
    {
        "id": 49,
        "name": "Scopophobia",
        "fear_of": "Being stared at",
        "story": (
            "On the crowded subway, Iris felt it: eyes on her. Not one pair — several. Or maybe "
            "none. She couldn't tell which was worse — being watched, or the paranoia of thinking "
            "she was. She adjusted her coat, checked her face on her phone screen, moved to a "
            "different car. The feeling followed her. By the time she got home, she was exhausted "
            "from the effort of being perceived."
        ),
        "question": "You notice someone across the room staring at you. How do you react?",
        "options": [
            "I'd feel intensely panicked and need to leave.",
            "I'd become very self-conscious and anxious.",
            "I'd wonder why but not be too bothered.",
            "I'd stare back or not care at all.",
        ],
    },
    {
        "id": 50,
        "name": "Monophobia",
        "fear_of": "Being alone in isolation",
        "story": (
            "The cabin in the woods was supposed to be a relaxing solo retreat. For the first "
            "hour, it was peaceful. By hour three, the silence was oppressive. By nightfall, "
            "with no phone signal, no neighbors, and nothing but trees and darkness in every "
            "direction, Leo felt his thoughts turning hostile. Every sound was amplified. Every "
            "shadow had intent. The isolation wasn't peaceful — it was a prison with no walls."
        ),
        "question": "You're spending a night alone in a remote cabin with no phone signal. How do you feel?",
        "options": [
            "Terrified — complete isolation is my nightmare.",
            "Very anxious — I'd struggle to relax.",
            "A bit uneasy but I'd enjoy the quiet.",
            "Perfect — exactly the kind of escape I need.",
        ],
    },
    {
        "id": 51,
        "name": "Ornithophobia",
        "fear_of": "Birds",
        "story": (
            "The pigeons gathered on the bench like a jury. When Emma sat down with her sandwich, "
            "one hopped onto the armrest and cocked its head at her. Then another landed. Then "
            "five more. Their beady eyes, their jerky movements, the way they fluttered suddenly "
            "and without warning — Emma bolted, dropping her lunch. She could still hear the "
            "frantic flapping behind her, wings beating against air like a dozen tiny heartbeats "
            "chasing her down the path."
        ),
        "question": "You're eating lunch in the park and a flock of pigeons gathers around you. How do you react?",
        "options": [
            "I'd leave immediately — birds coming near me is terrifying.",
            "I'd feel very uneasy and try to shoo them away.",
            "A little annoying, but I'd keep eating.",
            "I'd toss them some crumbs — I love birds!",
        ],
    },
    {
        "id": 52,
        "name": "Musophobia",
        "fear_of": "Mice and rats",
        "story": (
            "The scratching started at 2 AM — faint, rapid, coming from inside the wall. Greg lay "
            "rigid in bed, staring at the baseboard. Then a grey shape darted across the moonlit "
            "floor and disappeared under the dresser. He was on top of the bed in an instant, "
            "feet pulled up, heart slamming. It was tiny, barely the size of his thumb. It didn't "
            "matter. He slept in his car that night."
        ),
        "question": "You spot a mouse running across your kitchen floor. How do you react?",
        "options": [
            "I'd scream and leave the room — mice terrify me.",
            "I'd be really unsettled and call someone to handle it.",
            "I'd set a trap and move on with my day.",
            "I'd think it was kind of cute, honestly.",
        ],
    },
    {
        "id": 53,
        "name": "Ailurophobia",
        "fear_of": "Cats",
        "story": (
            "Diana's friend said, 'Don't worry, she's friendly,' as a sleek black cat wound "
            "between the chair legs toward her. But Diana had already drawn her feet up onto "
            "the couch. Something about the silent way cats moved — appearing suddenly on counters, "
            "staring without blinking, the retractable claws hidden inside velvet paws — made her "
            "skin crawl. The cat jumped onto the couch beside her and Diana vaulted over the "
            "armrest like an Olympic hurdler."
        ),
        "question": "You visit a friend and their cat jumps onto your lap. How do you feel?",
        "options": [
            "I'd panic and push it off — cats genuinely scare me.",
            "I'd freeze up and ask my friend to remove it.",
            "I'd be a little surprised but pet it gently.",
            "I'd love it — cats are wonderful company.",
        ],
    },
    {
        "id": 54,
        "name": "Apiphobia",
        "fear_of": "Bees and wasps",
        "story": (
            "The picnic was perfect until a yellow jacket landed on the rim of Ben's soda can. "
            "He froze. The insect crawled in a slow, deliberate circle, its black-and-yellow "
            "abdomen pulsing. Everyone said, 'Just stay still, it'll fly away.' But Ben's body "
            "didn't listen to reason. He swatted wildly, knocked over the can, and sprinted ten "
            "yards before he realized the wasp was still back at the table, now enjoying his "
            "spilled drink."
        ),
        "question": "A bee is buzzing around your head while you're outside. What do you do?",
        "options": [
            "Full panic — I'd run away flailing my arms.",
            "I'd be really anxious and try to slowly move away.",
            "I'd stay still and wait for it to leave — a little tense.",
            "Doesn't bother me — bees are harmless if you're calm.",
        ],
    },
    {
        "id": 55,
        "name": "Scoleciphobia",
        "fear_of": "Worms",
        "story": (
            "After the rain, the sidewalk became a minefield. Earthworms everywhere — pink, "
            "glistening, writhing on the wet concrete. Most people stepped over them without "
            "a thought. Tara couldn't. She stood at the edge of the path, her stomach turning, "
            "unable to make herself walk through the squirming gauntlet. She took a twenty-minute "
            "detour through the parking lot to avoid a two-minute walk."
        ),
        "question": "After a rainstorm, the ground is covered in earthworms. How do you handle walking through?",
        "options": [
            "I wouldn't — I'd find another route entirely.",
            "I'd be disgusted and tiptoe through as fast as possible.",
            "Slightly gross, but I'd walk through without much thought.",
            "Doesn't bother me at all — they're just worms.",
        ],
    },
    {
        "id": 56,
        "name": "Lepidopterophobia",
        "fear_of": "Butterflies and moths",
        "story": (
            "People always laughed when Naomi said she was afraid of butterflies. 'They're "
            "beautiful!' they'd say. But beauty wasn't the problem. It was the erratic flight — "
            "the way they zigzagged unpredictably, suddenly changing direction to flutter directly "
            "at your face. When a large moth flew into her bedroom one summer night, bouncing off "
            "the lampshade with papery wings, Naomi locked herself in the bathroom until her "
            "sister came to remove it."
        ),
        "question": "A large butterfly lands on your shoulder while you're in a garden. How do you react?",
        "options": [
            "I'd freak out and brush it off immediately — their fluttering terrifies me.",
            "I'd be very uncomfortable and want it gone.",
            "A little startled, but I'd let it sit there.",
            "That would make my day — butterflies are magical.",
        ],
    },
    {
        "id": 57,
        "name": "Chiroptophobia",
        "fear_of": "Bats",
        "story": (
            "The first one swooped past Dominic's head at dusk, close enough that he felt the "
            "air from its wings. Then another, and another — a whole colony pouring out from "
            "under the bridge like a dark cloud. They weren't interested in him, the guide "
            "explained. They were chasing mosquitoes. But their darting, unpredictable flight "
            "paths and leathery silhouettes against the dying sky sent Dominic scrambling back "
            "to the car with his jacket over his head."
        ),
        "question": "You're told a colony of bats lives near the cabin you're staying in. How do you feel?",
        "options": [
            "I'd refuse to stay — bats absolutely terrify me.",
            "I'd be very uneasy, especially after dark.",
            "A bit creeped out, but they won't bother me.",
            "I'd think it was cool and try to watch them at dusk.",
        ],
    },
    {
        "id": 58,
        "name": "Selachophobia",
        "fear_of": "Sharks",
        "story": (
            "The water was crystal clear, the beach pristine, the lifeguard flag green. But "
            "when Anton waded in past his waist, his mind did what it always did — it imagined "
            "what was below. A grey shape gliding silently beneath the surface, a dorsal fin, "
            "rows of teeth. He knew the odds were astronomically low. Statistics meant nothing "
            "to the animal part of his brain. He backed out of the water and didn't go in past "
            "his ankles for the rest of the vacation."
        ),
        "question": "You're swimming at a beautiful beach and someone mentions they once saw a shark nearby. How do you react?",
        "options": [
            "I'm out of the water immediately and not going back in.",
            "I'd be very anxious and stay in the shallows.",
            "A little unnerving, but I'd keep swimming.",
            "Doesn't change anything — shark attacks are incredibly rare.",
        ],
    },
    {
        "id": 59,
        "name": "Equinophobia",
        "fear_of": "Horses",
        "story": (
            "From a distance, horses looked majestic. Up close, standing next to one at the "
            "county fair, Violet was overwhelmed by the sheer mass of the animal — the barrel "
            "chest, the iron-shod hooves, the way it tossed its head and stamped without warning. "
            "When the horse turned to look at her, she stumbled backward. An animal that weighed "
            "a thousand pounds and could crush her with a single kick was not something she wanted "
            "to be within arm's reach of."
        ),
        "question": "You're offered a chance to ride a horse on a guided trail. How do you feel?",
        "options": [
            "No way — being near a horse makes me genuinely afraid.",
            "I'd be very nervous and would probably decline.",
            "A little intimidated by their size, but I'd try it.",
            "I'd love it — horses are incredible animals.",
        ],
    },
    {
        "id": 60,
        "name": "Ranidaphobia",
        "fear_of": "Frogs and toads",
        "story": (
            "The garden hose disturbed something in the flower bed. A fat toad leaped out and "
            "landed with a wet slap on Omar's bare foot. The cold, clammy skin against his own "
            "sent an electric shock of revulsion through his entire body. He kicked reflexively "
            "and the toad tumbled into the grass. Omar dropped the hose and went inside, scrubbing "
            "his foot as if he'd stepped in something toxic. He wore boots in the garden after that."
        ),
        "question": "You find a frog sitting on your doorstep. How do you react?",
        "options": [
            "I'd back away — frogs and toads repulse and scare me.",
            "I'd be pretty uncomfortable and go around to another entrance.",
            "I'd nudge it aside — slightly gross but no big deal.",
            "I'd pick it up and move it to the garden — frogs are great!",
        ],
    },
    {
        "id": 61,
        "name": "Ichthyophobia",
        "fear_of": "Fish",
        "story": (
            "The aquarium was supposed to be a fun date. But standing in front of the floor-to-"
            "ceiling tank, watching hundreds of fish glide past with their unblinking, glassy "
            "eyes and gaping mouths, Petra felt the walls closing in. When a massive grouper "
            "pressed its face against the glass inches from hers, she grabbed her partner's arm "
            "and pulled them toward the exit. 'I thought you liked the ocean,' her partner said. "
            "'I like the idea of the ocean,' Petra replied. 'Not the things living in it.'"
        ),
        "question": "You're snorkeling and a school of fish swims right up to you. How do you feel?",
        "options": [
            "Panicked — fish up close genuinely scare me.",
            "Very uncomfortable — I'd swim away quickly.",
            "A bit startled but I'd enjoy watching them.",
            "That's the whole point of snorkeling — amazing!",
        ],
    },
    {
        "id": 62,
        "name": "Vehophobia",
        "fear_of": "Driving",
        "story": (
            "Hannah got her license at sixteen like everyone else. But after a near-miss on the "
            "highway — a truck drifting into her lane, the blast of its horn, the jerk of the "
            "steering wheel — something changed. Every time she sat in the driver's seat, her "
            "hands clamped the wheel at ten and two, knuckles white. Merging made her nauseous. "
            "Highways were impossible. Gradually she stopped driving altogether, arranging her "
            "entire life around bus routes and rides from friends."
        ),
        "question": "You need to drive on a busy highway during rush hour. How do you feel?",
        "options": [
            "I can't — driving terrifies me to the point I avoid it.",
            "Extremely anxious — I'd be gripping the wheel and barely breathing.",
            "A bit stressful, but I can handle it.",
            "Totally fine — I'm a confident driver.",
        ],
    },
    {
        "id": 63,
        "name": "Gephyrophobia",
        "fear_of": "Bridges",
        "story": (
            "The bridge stretched over the river like a long, narrow dare. Concrete barriers on "
            "either side, water glinting far below through the gaps. Dennis gripped the steering "
            "wheel and fixed his eyes straight ahead, refusing to look left or right. The bridge "
            "swayed slightly — they all do, engineers say — but to Dennis it felt like the whole "
            "structure was about to fold into the water. He drove fifteen miles out of his way "
            "every morning to avoid that bridge."
        ),
        "question": "You need to cross a long, high bridge to reach your destination. How do you feel?",
        "options": [
            "I'd find another route — I can't handle crossing bridges.",
            "I'd white-knuckle through it with extreme anxiety.",
            "A little nervous over high bridges, but manageable.",
            "Bridges don't bother me at all — I enjoy the view.",
        ],
    },
    {
        "id": 64,
        "name": "Lilapsophobia",
        "fear_of": "Tornadoes and severe storms",
        "story": (
            "The sky turned green — that sickly, unnatural green that people in tornado country "
            "know means trouble. The sirens started wailing. Rosa ran to the basement, pulled the "
            "mattress over herself, and clutched a flashlight with both hands. The sound above was "
            "like a freight train grinding across the roof. Dishes shattered upstairs. Something "
            "heavy hit the side of the house. When it passed, Rosa stayed under the mattress for "
            "another two hours, shaking, unable to convince her body the danger was gone."
        ),
        "question": "You hear tornado sirens and the sky looks threatening. How do you react?",
        "options": [
            "Absolute terror — severe storms reduce me to a shaking mess.",
            "I'd take shelter immediately and be extremely anxious the whole time.",
            "I'd go to a safe spot and wait it out fairly calmly.",
            "I'd probably look outside — severe weather is fascinating to me.",
        ],
    },
    {
        "id": 65,
        "name": "Anemophobia",
        "fear_of": "Wind",
        "story": (
            "It was just wind. That's what everyone said. But when the gusts hit fifty miles per "
            "hour, rattling the windows and bending the trees sideways, Felix couldn't breathe. "
            "The howling was constant, relentless — like the atmosphere itself was angry. A trash "
            "can lid flew past the window and he jumped back as if it had come through the glass. "
            "He spent the night in the interior bathroom, the only room where he couldn't hear "
            "the wind trying to peel the world apart."
        ),
        "question": "A very windy day makes the trees bend and debris fly around. How do you feel?",
        "options": [
            "Genuinely scared — strong wind makes me feel unsafe and panicked.",
            "Very uneasy — I'd go inside and stay away from windows.",
            "Slightly on edge, but I'd carry on with my day.",
            "I love windy days — there's an energy to them.",
        ],
    },
    {
        "id": 66,
        "name": "Chionophobia",
        "fear_of": "Snow",
        "story": (
            "The forecast said two inches. By noon, it was twelve and still falling. Ada watched "
            "the white blanket erase the world outside — the road, the sidewalk, the car. Everything "
            "familiar vanished under an endless, silent white. The thought of being buried, trapped, "
            "roads impassable, power lines collapsing under the weight — it wasn't a winter "
            "wonderland to Ada. It was a slow-motion catastrophe falling from the sky."
        ),
        "question": "You wake up to find a heavy snowstorm has blanketed everything outside. How do you feel?",
        "options": [
            "Deeply anxious — snow makes me feel trapped and panicked.",
            "Uncomfortable and stressed about being snowed in.",
            "Mildly inconvenienced but I'd adjust.",
            "Excited — snow days are the best!",
        ],
    },
    {
        "id": 67,
        "name": "Bathophobia",
        "fear_of": "Depths",
        "story": (
            "The swimming pool was divided into sections. The shallow end, the medium, and then "
            "the deep end — twelve feet, marked with a red line on the wall. Leo swam comfortably "
            "to the middle. But the moment the floor dropped away and his feet found nothing "
            "beneath them, a primal alarm fired in his brain. The water was the same. The "
            "temperature was the same. But the depth — the invisible void below his kicking "
            "feet — turned the water into something hostile."
        ),
        "question": "You're swimming and suddenly realize the water beneath you is very deep. How do you react?",
        "options": [
            "Instant panic — I need to get to shallow water immediately.",
            "Very anxious — I'd swim back toward the shallows quickly.",
            "A little unsettling, but I'd keep swimming.",
            "Doesn't bother me — deep water is fine.",
        ],
    },
    {
        "id": 68,
        "name": "Automatonophobia",
        "fear_of": "Human-like figures (mannequins, wax figures, ventriloquist dummies)",
        "story": (
            "The wax museum was supposed to be cheesy fun. But walking through dimly lit rooms "
            "full of life-sized human replicas, frozen mid-gesture with glassy painted eyes, "
            "something in Chloe's brain refused to accept they weren't alive. She kept checking "
            "behind her, certain one had moved. When she turned a corner and came face to face "
            "with a figure she hadn't seen, she screamed loud enough to startle the actual humans "
            "two rooms over."
        ),
        "question": "You walk through a wax museum filled with lifelike human figures. How do you feel?",
        "options": [
            "Deeply unsettled — human-like figures terrify me.",
            "Creeped out — I'd want to get through quickly.",
            "A bit eerie but mostly fun.",
            "I think they're fascinating — I'd examine every one.",
        ],
    },
    {
        "id": 69,
        "name": "Pediophobia",
        "fear_of": "Dolls",
        "story": (
            "Grandma's attic was full of antique dolls — porcelain faces, painted red lips, eyes "
            "that clicked open and shut when tilted. Yuki was sent up to find a box of Christmas "
            "ornaments. She turned on the attic light and thirty pairs of glossy eyes stared back "
            "from the shelves. One doll sat slightly askew, its head tilted as if it had been "
            "listening. Yuki came back down without the ornaments and refused to go up again."
        ),
        "question": "You see a collection of antique porcelain dolls displayed on shelves. How do you feel?",
        "options": [
            "Deeply frightened — dolls with lifelike faces terrify me.",
            "Very uncomfortable — I'd avoid looking at them.",
            "Slightly creepy, but I can appreciate the craftsmanship.",
            "I think they're charming — I'd love to collect them.",
        ],
    },
    {
        "id": 70,
        "name": "Globophobia",
        "fear_of": "Balloons",
        "story": (
            "The birthday party was in full swing — streamers, cake, and balloons everywhere. "
            "Danny sat rigid at the table while kids batted balloons around the room. Every tap "
            "was a potential explosion. When a child sat on one and it popped with a rubbery bang, "
            "Danny's hands flew to his ears and his eyes squeezed shut. He spent the rest of the "
            "party in the kitchen, as far from the latex time bombs as possible."
        ),
        "question": "You're at a party surrounded by balloons, and kids are popping them. How do you feel?",
        "options": [
            "I'd need to leave — the anticipation of popping balloons terrifies me.",
            "Very tense — I'd be flinching at every sound.",
            "A bit jumpy at the pops, but mostly fine.",
            "Doesn't bother me — pop away!",
        ],
    },
    {
        "id": 71,
        "name": "Koumpounophobia",
        "fear_of": "Buttons",
        "story": (
            "Shopping for a new winter coat should have been simple. But when Grace ran her fingers "
            "across the rack, the plastic and metal buttons made her recoil. The smooth, disc-like "
            "shapes, the tiny holes, the way they caught on fabric — something about them set off "
            "a visceral disgust she couldn't explain. She only wore zippered and pullover clothing. "
            "When her office uniform required a button-down shirt, she had her tailor replace them "
            "with snaps."
        ),
        "question": "You're handed a jar full of assorted buttons and asked to sort them. How do you react?",
        "options": [
            "I couldn't touch them — buttons genuinely repulse me.",
            "I'd feel very uncomfortable but try to push through.",
            "Slightly weird, but I'd do it without issue.",
            "I'd enjoy sorting them — buttons are satisfying to organize.",
        ],
    },
    {
        "id": 72,
        "name": "Triskaidekaphobia",
        "fear_of": "The number 13",
        "story": (
            "When the hotel assigned Richard room 1313, his stomach dropped. He asked the clerk "
            "to change it. She smiled and said all other rooms were booked. He stood in the lobby "
            "for a full minute, weighing whether to sleep in his car. Rationally, he knew a number "
            "couldn't hurt him. But the weight of superstition pressed on him like a physical thing. "
            "He took the room, left the lights on all night, and checked out at 5 AM."
        ),
        "question": "You're given seat number 13 on a flight or room 13 in a hotel. How do you feel?",
        "options": [
            "I'd insist on changing — the number 13 genuinely scares me.",
            "I'd feel uneasy and anxious the whole time.",
            "I'd notice it but shrug it off.",
            "It's just a number — means nothing to me.",
        ],
    },
    {
        "id": 73,
        "name": "Phagophobia",
        "fear_of": "Swallowing or choking",
        "story": (
            "Ever since the incident at dinner — a piece of steak lodged in her throat, the "
            "seconds of airless panic before her boyfriend performed the Heimlich — Angela couldn't "
            "eat solid food without fear. Each bite was chewed dozens of times, reduced to mush "
            "before she attempted to swallow. Even then, her throat would tighten, refusing. She "
            "lost fifteen pounds in two months, living mostly on smoothies and soup, too afraid "
            "to swallow anything her body might reject."
        ),
        "question": "You're eating a meal and a bite feels like it's going down slowly. How do you react?",
        "options": [
            "I'd panic — the fear of choking is overwhelming for me.",
            "I'd stop eating and feel very anxious for a while.",
            "I'd drink some water and continue cautiously.",
            "I wouldn't think much of it — everyone swallows wrong sometimes.",
        ],
    },
    {
        "id": 74,
        "name": "Algophobia",
        "fear_of": "Pain",
        "story": (
            "The doctor said the procedure would involve 'minor discomfort.' But for Javier, there "
            "was no such thing as minor pain. Even the anticipation of a stubbed toe could make his "
            "palms sweat. He'd cancelled surgeries, avoided sports, and turned down roller coasters — "
            "not for the thrill, but for the possibility that something might hurt. The fear of pain "
            "had become more debilitating than any pain itself."
        ),
        "question": "You need a minor medical procedure that might cause some discomfort. How do you feel?",
        "options": [
            "I'd consider refusing — the thought of any pain fills me with dread.",
            "I'd go through with it but be extremely anxious beforehand.",
            "I'd be a bit nervous but accept it's temporary.",
            "Pain doesn't really bother me — I'd get it done without worry.",
        ],
    },
    {
        "id": 75,
        "name": "Nosophobia",
        "fear_of": "Contracting a specific illness",
        "story": (
            "Every headache was a tumor. Every cough was the start of something terminal. When "
            "Rena read about a rare disease online, she immediately noticed symptoms in herself — "
            "the tingling in her hand, the slight fatigue, the occasional blurred vision. Three "
            "doctors told her she was fine. She didn't believe any of them. The fear wasn't "
            "rational, and knowing that didn't help."
        ),
        "question": "You read about a rare illness and notice you have one of the symptoms. How do you react?",
        "options": [
            "I'd be consumed with fear — I'd be certain I had it.",
            "I'd be very anxious and probably see a doctor immediately.",
            "I'd note it but remind myself it's probably nothing.",
            "I wouldn't give it a second thought.",
        ],
    },
    {
        "id": 76,
        "name": "Pharmacophobia",
        "fear_of": "Taking medication",
        "story": (
            "The doctor pressed the prescription into Caleb's hand and said, 'Take one a day, "
            "you'll feel better in two weeks.' Caleb stared at the small orange bottle at home "
            "for three days before opening it. What if there were side effects? What if his body "
            "rejected it? He read every word of the pamphlet folded inside, cataloguing every "
            "rare reaction until the cure sounded worse than the illness. The bottle stayed full."
        ),
        "question": "A doctor prescribes you a new medication. How do you feel about taking it?",
        "options": [
            "I probably won't take it — putting medication in my body terrifies me.",
            "I'd be very anxious and research every possible side effect first.",
            "I'd be cautious but take it as prescribed.",
            "I'd take it without hesitation — I trust my doctor.",
        ],
    },
    {
        "id": 77,
        "name": "Tomophobia",
        "fear_of": "Surgical operations",
        "story": (
            "The surgeon smiled and called it 'routine.' A thirty-minute outpatient procedure. "
            "But for Brooke, the word 'surgery' activated a slideshow of horrors: the operating "
            "table, the bright light, the mask lowering over her face, consciousness slipping away "
            "while strangers cut into her. She postponed it twice, then a third time, letting a "
            "treatable condition become a serious one because the idea of being operated on was "
            "more frightening than being sick."
        ),
        "question": "You're told you need a minor surgery. How do you feel?",
        "options": [
            "I'd avoid it at all costs — surgery is my worst fear.",
            "I'd be extremely anxious and might delay it repeatedly.",
            "I'd be nervous but schedule it and go through with it.",
            "I'd get it done — surgery doesn't particularly frighten me.",
        ],
    },
    {
        "id": 78,
        "name": "Obesophobia",
        "fear_of": "Gaining weight",
        "story": (
            "The scale read two pounds more than yesterday. Two pounds. For most people, a normal "
            "fluctuation. For Mandy, it was a crisis. She skipped breakfast, then lunch. She ran "
            "six miles on the treadmill even though her knees ached. The number on the scale "
            "governed her mood, her meals, her self-worth. Rational thought had nothing to do "
            "with it — the fear of gaining weight had its own gravity, pulling her routines into "
            "its orbit."
        ),
        "question": "You notice your clothes feel a little tighter than usual. How do you react?",
        "options": [
            "I'd spiral into anxiety — weight gain is one of my deepest fears.",
            "I'd feel very distressed and immediately change my habits.",
            "I'd be mildly conscious of it and maybe eat a bit healthier.",
            "I wouldn't care much — bodies fluctuate naturally.",
        ],
    },
    {
        "id": 79,
        "name": "Cibophobia",
        "fear_of": "Food",
        "story": (
            "The restaurant menu was a battlefield. Sasha studied each dish not for taste but for "
            "danger — undercooked chicken, hidden allergens, unfamiliar ingredients that might "
            "make her sick. She asked the waiter three questions about the salad alone. In the "
            "end, she ordered plain bread and water. Her friends exchanged glances. Sasha noticed "
            "but couldn't explain that every bite of unfamiliar food felt like a gamble with her "
            "body as the stakes."
        ),
        "question": "You're at a dinner party and the host serves a dish you've never tried before. How do you feel?",
        "options": [
            "I'd refuse to eat it — unfamiliar food fills me with fear.",
            "I'd be very anxious and might barely taste it.",
            "I'd be a little hesitant but try a bite.",
            "I'd dig in — I love trying new foods!",
        ],
    },
    {
        "id": 80,
        "name": "Haphephobia",
        "fear_of": "Being touched",
        "story": (
            "When the coworker reached out and patted Theo on the back — a casual, friendly "
            "gesture — his entire body went rigid. The point of contact burned like a brand. "
            "It wasn't pain, exactly. It was an overwhelming invasion, a breach of some invisible "
            "boundary that his nervous system treated as a threat. He excused himself, went to the "
            "bathroom, and stood gripping the sink until his breathing normalized. A friendly pat. "
            "That's all it was."
        ),
        "question": "An acquaintance gives you a friendly hug in greeting. How do you react?",
        "options": [
            "I'd tense up completely — being touched is truly distressing to me.",
            "I'd endure it but feel very uncomfortable and on edge.",
            "A bit surprised, but I'd go with it.",
            "I welcome hugs — physical contact is warm and comforting.",
        ],
    },
    {
        "id": 81,
        "name": "Telephonophobia",
        "fear_of": "Making or receiving phone calls",
        "story": (
            "The phone buzzed with an incoming call from an unknown number. Nina stared at it "
            "like it was a ticking bomb. She let it ring out, then felt her heart race when it "
            "rang again. She needed to schedule a dentist appointment — she'd been putting it off "
            "for months because it required a phone call. Emails, texts, online forms — anything "
            "but hearing a live voice expecting an immediate, unrehearsed response."
        ),
        "question": "You need to make an important phone call to someone you don't know. How do you feel?",
        "options": [
            "I'd dread it — phone calls cause me real panic.",
            "Very anxious — I'd rehearse what to say multiple times first.",
            "A little awkward, but I'd just dial and get it over with.",
            "No issue — I make phone calls without thinking twice.",
        ],
    },
    {
        "id": 82,
        "name": "Anthropophobia",
        "fear_of": "People in general",
        "story": (
            "The grocery store at 3 PM was too crowded. So was the 9 AM window. So was online "
            "pickup, because someone still handed you the bags. Yuto had narrowed his life to a "
            "series of carefully timed maneuvers designed to minimize contact with other human "
            "beings. It wasn't that he disliked people — he feared them. Their unpredictability, "
            "their judgments, their capacity to wound with a word or a look. Alone felt safe. "
            "Together felt like standing in traffic."
        ),
        "question": "You need to run errands in a busy area with lots of people around. How do you feel?",
        "options": [
            "Overwhelmed with fear — being around people is deeply distressing.",
            "Very anxious — I'd try to go at the quietest possible time.",
            "A little draining, but I can manage fine.",
            "I enjoy being around people — busy places energize me.",
        ],
    },
    {
        "id": 83,
        "name": "Katagelophobia",
        "fear_of": "Being ridiculed or laughed at",
        "story": (
            "In the meeting, Daryl offered an idea. A small, tentative suggestion. Someone "
            "chuckled — not at him, just at a coincidental timing with something on their phone. "
            "But Daryl's face went red. His mind rewrote the moment instantly: they were laughing "
            "at him. His idea was stupid. He was stupid. He didn't speak again for the rest of "
            "the meeting, or the next one, or the one after that. The echo of that accidental "
            "laugh silenced him for weeks."
        ),
        "question": "You make a mistake in front of a group and someone laughs. How do you react?",
        "options": [
            "I'd be devastated — being laughed at is my worst nightmare.",
            "I'd feel deeply embarrassed and replay it in my mind for days.",
            "I'd be a bit embarrassed but laugh it off.",
            "I'd laugh along — everyone makes mistakes.",
        ],
    },
    {
        "id": 84,
        "name": "Aphenphosmphobia",
        "fear_of": "Intimacy and close relationships",
        "story": (
            "The relationship was going well — too well. That was the problem. The closer they "
            "got, the more Quinn wanted to run. Not because of anything wrong, but because "
            "intimacy meant being truly seen — flaws, fears, the unfiltered self. The vulnerability "
            "was suffocating. Quinn started cancelling dates, creating distance, rebuilding the "
            "walls that had taken months to lower. Being known felt like being exposed."
        ),
        "question": "Someone you care about wants to have a deep, emotionally open conversation. How do you feel?",
        "options": [
            "Terrified — emotional intimacy makes me want to shut down.",
            "Very anxious — I'd struggle to open up.",
            "A bit uncomfortable at first, but I value the connection.",
            "I welcome it — deep conversations strengthen bonds.",
        ],
    },
    {
        "id": 85,
        "name": "Gymnophobia",
        "fear_of": "Nudity",
        "story": (
            "The gym locker room should have been routine. But for Hank, the open showers and "
            "casual undressing around strangers were a minefield of anxiety. Not just about his own "
            "body — the presence of nudity itself, the exposure, the rawness of it. He changed in "
            "a bathroom stall. He showered at home. He timed his arrivals and departures to avoid "
            "the changing rush. Being unclothed — or near anyone who was — felt like a violation "
            "of some fundamental boundary."
        ),
        "question": "You're at a spa where communal areas are clothing-optional. How do you react?",
        "options": [
            "I couldn't handle it — nudity in any context deeply distresses me.",
            "I'd be extremely uncomfortable and keep fully covered.",
            "A bit awkward at first, but I'd adjust.",
            "I'm completely comfortable — the human body is natural.",
        ],
    },
    {
        "id": 86,
        "name": "Dystychiphobia",
        "fear_of": "Accidents",
        "story": (
            "Every car ride was a rehearsal of disaster in Farah's mind. She imagined the tire "
            "blowout, the swerving truck, the patch of ice. She pictured the crumple of metal "
            "and the sound of shattering glass before a single thing went wrong. The scenarios "
            "were so vivid they were almost memories. She double-checked seatbelts, avoided "
            "highways, and refused to travel in bad weather. Her life shrank to fit the narrow "
            "corridor of perceived safety."
        ),
        "question": "You hear sirens while driving — an accident has happened ahead. How do you feel?",
        "options": [
            "I'd be gripped with terror — the fear of accidents rules my life.",
            "Very shaken — I'd drive the rest of the way hyper-alert and anxious.",
            "Somewhat sobered but I'd continue without much distress.",
            "Mildly aware, but it wouldn't really affect my mood.",
        ],
    },
    {
        "id": 87,
        "name": "Peniaphobia",
        "fear_of": "Poverty",
        "story": (
            "Ethan checked his bank account six times a day. He had savings. He had a stable job. "
            "But the number never felt like enough. Every unexpected bill — a car repair, a medical "
            "copay — triggered a cascade of catastrophic thinking: what if it all disappears? What "
            "if one bad month starts a spiral into homelessness? He denied himself small pleasures, "
            "hoarded money like oxygen, and still lay awake at night convinced ruin was one "
            "paycheck away."
        ),
        "question": "An unexpected expense comes up that you can afford but it dips into your savings. How do you react?",
        "options": [
            "I'd be consumed with anxiety — the fear of running out of money haunts me.",
            "I'd be very stressed and cut back on everything for weeks.",
            "I'd be mildly annoyed but handle it.",
            "No big deal — that's what savings are for.",
        ],
    },
    {
        "id": 88,
        "name": "Kenophobia",
        "fear_of": "Voids and empty spaces",
        "story": (
            "The warehouse was vast — hundreds of feet of bare concrete floor stretching to distant "
            "walls under a ceiling that vanished into shadow. There was nothing in it. That was the "
            "problem. The emptiness felt sentient, hungry, as if the space itself was too large to "
            "be safe. Maggie stood at the entrance and couldn't make herself walk into that yawning "
            "expanse. The void felt like it would swallow her whole."
        ),
        "question": "You walk into an enormous, completely empty room. How does it make you feel?",
        "options": [
            "Deeply unsettled — empty voids make me feel panicked.",
            "Uncomfortable and exposed — I'd want to leave quickly.",
            "A little eerie, but not enough to bother me.",
            "It feels peaceful and open — I like big empty spaces.",
        ],
    },
    {
        "id": 89,
        "name": "Agyrophobia",
        "fear_of": "Crossing streets",
        "story": (
            "The crosswalk signal turned green. Pedestrians stepped off the curb in an easy flow. "
            "But Keith stayed planted on the sidewalk, watching cars that might not stop, drivers "
            "who might not see him, the terrible vulnerability of a human body on asphalt between "
            "two tons of moving steel. The signal turned red again. He waited for the next green. "
            "And the next. It took twenty minutes and a gap with no visible traffic before he "
            "finally sprinted across."
        ),
        "question": "You need to cross a busy intersection. How do you feel?",
        "options": [
            "I'd be paralyzed with fear — crossing streets terrifies me.",
            "Very anxious — I'd wait for the safest possible moment.",
            "A bit cautious, but I'd cross normally.",
            "Fine — I cross streets without giving it much thought.",
        ],
    },
    {
        "id": 90,
        "name": "Hodophobia",
        "fear_of": "Traveling",
        "story": (
            "The trip was booked three months in advance. Flight, hotel, itinerary — all perfectly "
            "planned. But as departure day approached, Lucia's dread grew like a rising tide. Not "
            "the flying (she'd made peace with that). It was the leaving — the unknown territory, "
            "the disrupted routine, the thousand things that could go wrong in an unfamiliar place. "
            "She cancelled the night before, told her friends she was sick, and felt equal parts "
            "relief and shame."
        ),
        "question": "You're offered a free trip to an exciting destination you've never visited. How do you feel?",
        "options": [
            "I'd decline — the idea of traveling terrifies me.",
            "I'd want to go but be consumed with anxiety about leaving home.",
            "A little nervous about the unknown, but mostly excited.",
            "I'd jump at the chance — traveling is one of my favorite things!",
        ],
    },
    {
        "id": 91,
        "name": "Taphophobia",
        "fear_of": "Being buried alive",
        "story": (
            "It started with a documentary about Victorian-era safety coffins — coffins with bells "
            "attached because premature burial was disturbingly common. After watching it, Rita "
            "couldn't stop imagining it: waking up in darkness, in a box, underground, with no one "
            "able to hear her scream. She updated her will to specify cremation. Then she updated it "
            "again, adding redundant instructions, because what if someone didn't read it carefully "
            "enough?"
        ),
        "question": "How do you feel when you think about the concept of being buried alive?",
        "options": [
            "It's one of my greatest fears — I can't even think about it without panicking.",
            "Extremely disturbing — it makes me deeply anxious.",
            "Unsettling to consider, but I don't dwell on it.",
            "It's just a hypothetical — doesn't really bother me.",
        ],
    },
    {
        "id": 92,
        "name": "Submechanophobia",
        "fear_of": "Submerged man-made objects",
        "story": (
            "The lake was clear enough to see the old car resting on the bottom — an abandoned "
            "wreck from decades ago, half-buried in silt, windows dark and empty. Connor's skin "
            "prickled. There was something profoundly wrong about man-made objects underwater: "
            "sunken ships, submerged statues, flooded buildings. They didn't belong there, and "
            "their wrongness created a revulsion he felt in his bones. He wouldn't swim anywhere "
            "near the wreck."
        ),
        "question": "You see a sunken car or structure visible underwater while swimming. How do you react?",
        "options": [
            "I'd get out of the water immediately — submerged objects terrify me.",
            "I'd swim away from it — something about it deeply unnerves me.",
            "A bit creepy, but I might swim closer out of curiosity.",
            "I'd find it fascinating and want to explore it.",
        ],
    },
    {
        "id": 93,
        "name": "Atelophobia",
        "fear_of": "Imperfection",
        "story": (
            "The essay was due at midnight. Vanessa had been writing and rewriting the introduction "
            "since 9 AM. Fourteen hours. One paragraph. Each version was almost right but not "
            "quite — a word out of place, a rhythm slightly off, a sentence that didn't capture "
            "exactly what she meant. She couldn't submit something imperfect. It would define her. "
            "Reveal her. Expose the gap between who she was and who she needed to be. She submitted "
            "it at 11:59, sick to her stomach, already composing revisions in her head."
        ),
        "question": "You've finished a project but notice a minor flaw just before the deadline. How do you react?",
        "options": [
            "I'd be consumed with anxiety — imperfection feels catastrophic to me.",
            "I'd spend all remaining time trying to fix it, even at great stress.",
            "I'd try to fix it quickly, but accept it if I can't.",
            "Good enough is good enough — I'd submit it and move on.",
        ],
    },
    {
        "id": 94,
        "name": "Metathesiophobia",
        "fear_of": "Change",
        "story": (
            "The company announced a restructure. New teams, new roles, new office layout. Most "
            "people shrugged. Some were excited. But for Drew, the announcement read like a "
            "demolition notice for everything stable in his life. The routine he'd built, the "
            "desk he'd sat at for five years, the team he'd learned to trust — all changing. "
            "The unknown was not an adventure. It was a threat. He spent two weeks refreshing "
            "job listings, not because he wanted to leave, but because any change he chose felt "
            "less terrifying than change imposed on him."
        ),
        "question": "Major changes are announced at your workplace or in your life. How do you react?",
        "options": [
            "I'm overwhelmed with dread — change in any form terrifies me.",
            "I feel very anxious and resist it as long as possible.",
            "I'm uneasy at first but adapt fairly quickly.",
            "I welcome change — it keeps life interesting.",
        ],
    },
    {
        "id": 95,
        "name": "Cherophobia",
        "fear_of": "Happiness or joyful events",
        "story": (
            "Things were going well — too well. New job, great relationship, everything clicking "
            "into place. But instead of enjoying it, Maris was waiting for the other shoe to drop. "
            "Happiness felt like a setup. Every good moment was a debt that would eventually come "
            "due in pain. She caught herself sabotaging plans, declining invitations, dimming her "
            "own joy before life could do it for her. Better to stay at a comfortable neutral than "
            "to climb high enough that the fall would break something."
        ),
        "question": "Everything in your life is going really well right now. How does that make you feel?",
        "options": [
            "Anxious — when things are good, I'm convinced something bad is coming.",
            "Slightly on edge — I have trouble trusting good fortune.",
            "Happy but aware it might not last — and that's okay.",
            "Purely happy — I enjoy good times without worrying about what's next.",
        ],
    },
    {
        "id": 96,
        "name": "Aichmophobia",
        "fear_of": "Sharp or pointed objects",
        "story": (
            "The steak knife sat on the table like every other utensil. But when Angie looked at "
            "it, she didn't see a tool — she saw a point, a blade, the terrible potential it "
            "carried. She used a butter knife instead. At home, she'd replaced all the pointed "
            "scissors with round-tipped ones, stored kitchen knives in a locked drawer, and avoided "
            "sewing needles entirely. It wasn't the objects themselves. It was the sharp, piercing "
            "possibility they represented."
        ),
        "question": "You're asked to use a very sharp knife to help prepare food in the kitchen. How do you feel?",
        "options": [
            "I'd refuse — sharp objects genuinely make me feel panicked.",
            "I'd be very uncomfortable and handle it as minimally as possible.",
            "I'd be a little cautious but use it normally.",
            "No issue at all — I'm comfortable with sharp tools.",
        ],
    },
    {
        "id": 97,
        "name": "Nyctohylophobia",
        "fear_of": "Dark forests or wooded areas at night",
        "story": (
            "The trail back to camp was only a quarter mile through the trees. In daylight, it "
            "was a pleasant walk. But at night, with only a dying flashlight and the canopy "
            "blocking every star, the forest transformed. The trees pressed close like walls. "
            "Every rustle was footsteps. Every snapping branch was something large and alert. "
            "Cole ran the last hundred yards, burst into the clearing, and swore he would never "
            "set foot in a forest after dark again."
        ),
        "question": "You have to walk through a dense forest at night to get back to your campsite. How do you feel?",
        "options": [
            "I couldn't do it — dark forests are absolutely terrifying to me.",
            "I'd be extremely scared but force myself, practically running.",
            "A bit spooked, but I'd manage with a good flashlight.",
            "I'd enjoy the nighttime atmosphere — forests at night are magical.",
        ],
    },
    {
        "id": 98,
        "name": "Siderodromophobia",
        "fear_of": "Trains or rail travel",
        "story": (
            "The platform vibrated before the train arrived — a low hum that climbed into a roar "
            "as the massive steel machine announced itself. For Phoebe, standing on the platform "
            "was like standing on the edge of a cliff. The speed, the weight, the unforgiving "
            "precision of the rails — one misstep and the consequences were absolute. Inside the "
            "car, she pressed against the window, feeling every sway and rattle, convinced the "
            "derailment was one loose bolt away."
        ),
        "question": "You need to take a train for a long-distance journey. How do you feel about it?",
        "options": [
            "I'd look for any alternative — trains genuinely frighten me.",
            "I'd go but be tense and anxious the entire ride.",
            "A little nervous at speed, but mostly I'd enjoy the journey.",
            "I love train travel — it's one of my favorite ways to go.",
        ],
    },
    {
        "id": 99,
        "name": "Cleithrophobia",
        "fear_of": "Being trapped or locked in",
        "story": (
            "The escape room was supposed to be team-building fun. Puzzles, clues, sixty minutes "
            "on the clock. But the moment the door clicked shut behind her, Sandra's world narrowed. "
            "The locked door wasn't a game mechanic — it was a cage. She knew there was a safety "
            "button, knew the staff was watching on cameras, knew she could leave anytime. None of "
            "that mattered. Her brain screamed one word: trapped. She pressed the emergency release "
            "at the four-minute mark."
        ),
        "question": "Friends invite you to do an escape room. How do you feel?",
        "options": [
            "I'd decline — being locked in a room is genuinely terrifying to me.",
            "I'd feel very anxious and would need constant reassurance I can leave.",
            "A tiny bit nervous at first, but mostly it sounds fun.",
            "I'd love it — escape rooms are a great time!",
        ],
    },
    {
        "id": 100,
        "name": "Heliophobia",
        "fear_of": "Sunlight",
        "story": (
            "Summer was everyone else's favorite season. For Greta, it was a siege. The relentless "
            "sun beating through every window, the expectation to go outside, the brightness that "
            "felt less like warmth and more like exposure. She kept her blinds permanently drawn, "
            "planned errands for overcast days, and wore long sleeves even in July. The sun wasn't "
            "cheerful to her. It was an interrogation lamp she couldn't switch off."
        ),
        "question": "It's a bright, sunny day and friends want to spend hours outside. How do you feel?",
        "options": [
            "Deeply uncomfortable — prolonged sunlight genuinely distresses me.",
            "I'd go but stay in the shade as much as possible, feeling uneasy.",
            "I'd enjoy it in moderation — maybe find shade now and then.",
            "I'd soak it up — sunshine is the best!",
        ],
    },
    {
        "id": 101,
        "name": "Alektorophobia",
        "fear_of": "Chickens and roosters",
        "story": (
            "The farm visit seemed harmless until the rooster came strutting around the corner "
            "of the barn — chest puffed, comb bright red, talons clicking on the concrete. It "
            "locked eyes with Delia and charged. She hadn't expected something that barely reached "
            "her knee to be so terrifying, but the flapping wings, the aggressive pecking, and "
            "the prehistoric screech sent her scrambling over a fence she didn't know she could "
            "climb."
        ),
        "question": "You're at a farm and a rooster starts walking toward you aggressively. How do you react?",
        "options": [
            "I'd run — chickens and roosters genuinely scare me.",
            "I'd back away quickly, very nervous.",
            "I'd stand my ground — it's just a bird.",
            "I'd find it funny and try to shoo it away.",
        ],
    },
    {
        "id": 102,
        "name": "Ablutophobia",
        "fear_of": "Bathing or washing",
        "story": (
            "It wasn't about being dirty. It was about the water — the vulnerability of standing "
            "naked under a stream, eyes closed against the soap, unable to see or hear properly. "
            "For Isaac, every shower felt like a small surrender of control. The steam, the enclosed "
            "space, the sound of water masking everything else — it was too much. He kept showers "
            "under two minutes, always with the curtain partially open, always facing the door."
        ),
        "question": "How do you feel about your daily shower or bath routine?",
        "options": [
            "I dread it — bathing makes me feel extremely vulnerable and anxious.",
            "I rush through it — being in water like that is uncomfortable.",
            "It's routine — I don't think much about it.",
            "I love a long, relaxing bath or shower.",
        ],
    },
    {
        "id": 103,
        "name": "Ecclesiophobia",
        "fear_of": "Churches or religious buildings",
        "story": (
            "The wedding was in a cathedral — vaulted ceilings, stained glass, rows of wooden "
            "pews stretching toward a distant altar. Most guests admired the architecture. But "
            "when Helen stepped through the heavy doors, the air changed. Something about the "
            "vast silence, the watchful icons, the centuries of whispered prayers soaked into the "
            "stone — it pressed down on her. She sat in the last pew, nearest the exit, and left "
            "before the vows."
        ),
        "question": "You're invited to an event held inside a grand, old church. How do you feel?",
        "options": [
            "I'd struggle to go in — religious buildings fill me with dread.",
            "I'd attend but feel deeply uneasy the entire time.",
            "A bit solemn, but I'd appreciate the atmosphere.",
            "I find churches beautiful and peaceful.",
        ],
    },
    {
        "id": 104,
        "name": "Amaxophobia",
        "fear_of": "Riding in vehicles",
        "story": (
            "It wasn't about driving — Risa didn't even have a license. It was about being a "
            "passenger. Every time a friend drove her somewhere, she became hyperaware of every "
            "detail: the speedometer creeping up, the distance to the car ahead, the way the "
            "driver glanced at their phone for just a second. She pressed an invisible brake pedal "
            "on the passenger side, gripped the door handle at every turn, and arrived at every "
            "destination drenched in stress sweat."
        ),
        "question": "Someone offers you a ride and they drive a bit fast. How do you feel?",
        "options": [
            "Terrified — riding in any vehicle is a nightmare for me.",
            "Very anxious — I'd be holding on tight and watching the road constantly.",
            "A little nervous, but I'd trust the driver.",
            "I'm fine — I enjoy the ride.",
        ],
    },
    {
        "id": 105,
        "name": "Mageirocophobia",
        "fear_of": "Cooking",
        "story": (
            "The recipe said 'simple.' Thirty minutes. Five ingredients. But standing in front "
            "of the stove, Wes felt paralyzed. The hot oil sizzled and popped — what if it "
            "splattered? The knife was too sharp — what if he slipped? The oven timer confused "
            "him — what if something burned, or worse, started a fire? He stood there so long "
            "the oil started smoking. He turned off the burner, ordered delivery, and ate alone "
            "with the cookbook staring at him from the counter like an accusation."
        ),
        "question": "You need to cook a meal from scratch, including using the stove and sharp knives. How do you feel?",
        "options": [
            "Panicked — cooking terrifies me and I avoid it completely.",
            "Very stressed — I'd need someone beside me the whole time.",
            "A little unsure, but I'd follow a recipe and manage.",
            "I love cooking — it's one of my favorite activities.",
        ],
    },
    {
        "id": 106,
        "name": "Panphobia",
        "fear_of": "Everything or a constant unknown dread",
        "story": (
            "There was no specific trigger. That was the worst part. Adrian woke with dread, "
            "carried it through breakfast, through work, through dinner, into sleep. It wasn't "
            "spiders or heights or crowds — it was everything and nothing. A pervasive sense that "
            "something was fundamentally wrong, that danger lurked in the ordinary. The cereal "
            "box, the parking lot, the mailman's greeting — all filtered through a lens of "
            "unshakeable, sourceless fear."
        ),
        "question": "You wake up with a general feeling of dread, but there's no specific reason. How often does this happen?",
        "options": [
            "Constantly — I live with a background hum of fear about everything.",
            "Frequently — unexplained anxiety is a regular part of my life.",
            "Occasionally — some mornings are just off.",
            "Almost never — I generally wake up feeling fine.",
        ],
    },
    {
        "id": 107,
        "name": "Tachophobia",
        "fear_of": "Speed",
        "story": (
            "The highway on-ramp required acceleration to sixty in a few hundred feet. For most "
            "drivers, it was automatic. For Wade, it was a daily crisis. The speedometer climbing "
            "past forty made his vision narrow. At fifty, his hands shook. At sixty, the world "
            "outside the windshield blurred into a streak of mortal danger. He drove the back "
            "roads everywhere — an extra forty minutes each way — because nothing above thirty-five "
            "miles per hour felt survivable."
        ),
        "question": "You're on a roller coaster or in a car going very fast. How does the speed make you feel?",
        "options": [
            "Terrified — speed in any form makes me feel like I'm going to die.",
            "Very uncomfortable — I grip whatever I can and close my eyes.",
            "A little intense, but I can handle it.",
            "I love speed — the faster the better!",
        ],
    },
    {
        "id": 108,
        "name": "Spectrophobia",
        "fear_of": "Reflections or looking in mirrors in the dark",
        "story": (
            "The bathroom mirror was fine in daylight. But at 2 AM, when Annika got up for water, "
            "passing that mirror in the dark hallway was a gauntlet. She knew what she'd see — "
            "herself, barely visible in the dimness. But her brain expected something else: a shape "
            "behind her, a face not quite her own, eyes that might blink when hers didn't. She "
            "started covering the hallway mirror with a towel before bed, because what you can't "
            "see in a dark reflection might see you."
        ),
        "question": "You pass a mirror in a dark hallway late at night. How do you feel?",
        "options": [
            "Genuinely frightened — dark mirrors feel like portals to something wrong.",
            "Very uneasy — I'd avoid looking and hurry past.",
            "A brief chill, nothing lasting.",
            "It wouldn't cross my mind at all.",
        ],
    },
    {
        "id": 109,
        "name": "Basophobia",
        "fear_of": "Falling",
        "story": (
            "It wasn't the height that got to Cass — it was the sensation of potentially falling. "
            "Standing on a step ladder, walking on an icy sidewalk, even leaning back in a tilting "
            "chair — any moment where balance felt uncertain triggered a full-body alarm. Her "
            "muscles locked, her hands reached for the nearest solid thing, and her heart hammered "
            "as if gravity had just issued a personal threat. She walked on flat, dry ground "
            "whenever possible, and treated any slope like a cliff."
        ),
        "question": "You're walking on an icy sidewalk and feel yourself start to slip. How do you react?",
        "options": [
            "I'd freeze in terror — the sensation of losing balance is deeply frightening.",
            "I'd be shaken and extremely cautious for the rest of the walk.",
            "I'd catch myself and keep going, a bit more carefully.",
            "I'd barely notice — slipping is no big deal.",
        ],
    },
    {
        "id": 110,
        "name": "Sociophobia",
        "fear_of": "Being judged by others",
        "story": (
            "The outfit was wrong. Elise had changed four times and they were all wrong. Not "
            "because of how they looked in the mirror, but because of how they'd look to others. "
            "Every choice sent a message she couldn't control — too casual, too formal, too "
            "attention-seeking, too invisible. She arrived at the dinner party twenty minutes late, "
            "wearing the first outfit after all, and spent the evening convinced everyone was "
            "silently evaluating every word she said and every choice she'd made."
        ),
        "question": "You're about to enter a room full of people you want to impress. How do you feel?",
        "options": [
            "Paralyzed — the fear of being judged is overwhelming.",
            "Extremely anxious — I'd be hyper-aware of everything I say and do.",
            "A bit self-conscious, but I'd relax once I settled in.",
            "Confident — I don't worry much about others' judgments.",
        ],
    },
    {
        "id": 111,
        "name": "Ankylophobia",
        "fear_of": "Joint immobility or being physically stuck",
        "story": (
            "When the cast went on Tomas' broken wrist, the clasp of plaster felt less like "
            "treatment and more like imprisonment. Six weeks of a joint locked in place — unable "
            "to bend, flex, or rotate. He could feel the immobility like a weight. Some nights "
            "he'd lie awake flexing his other hand obsessively, terrified that his working joints "
            "might somehow lock too. The day the cast came off, he moved his wrist back and forth "
            "for twenty minutes straight, just to prove he still could."
        ),
        "question": "Imagine you need to wear a brace that completely immobilizes your arm for weeks. How do you feel?",
        "options": [
            "Deeply distressed — the thought of a joint being frozen fills me with dread.",
            "Very uncomfortable — I'd constantly be aware of the restriction.",
            "Annoying, but I'd tolerate it for recovery.",
            "Not a big deal — I'd adapt quickly.",
        ],
    },
    {
        "id": 112,
        "name": "Xanthophobia",
        "fear_of": "The color yellow",
        "story": (
            "It started without a clear origin. Sunflowers, school buses, caution tape, yield "
            "signs — anything bright yellow triggered a wave of unease in Marcy that she couldn't "
            "rationalize. The color felt aggressive, warning-like, even when it was just a painted "
            "wall or a friend's sweater. She rearranged her wardrobe, avoided certain aisles at "
            "the store, and repainted the kitchen twice. People laughed when she tried to explain. "
            "That made it lonelier."
        ),
        "question": "You walk into a room painted entirely in bright yellow. How does it make you feel?",
        "options": [
            "Genuinely distressed — the color yellow provokes a strong negative reaction in me.",
            "Uncomfortable — I'd want to leave the room.",
            "A bold choice — I might find it a bit much, but it's fine.",
            "I love yellow — it's bright and cheerful!",
        ],
    },
    {
        "id": 113,
        "name": "Sitophobia",
        "fear_of": "Eating or consuming food",
        "story": (
            "Lunchtime was a performance. Niko sat at the break room table, opened his container, "
            "and stared at the food as if it required defusing. What if it had spoiled? What if "
            "there was something in it he was unknowingly allergic to? What if the act of eating "
            "itself triggered the choking, the nausea, the loss of control he feared most? He took "
            "one bite, chewed thirty-two times — always thirty-two — and waited five minutes before "
            "attempting the next. Lunch took an hour and a half."
        ),
        "question": "It's mealtime and food is in front of you. How easy is it for you to start eating?",
        "options": [
            "Extremely difficult — eating itself fills me with anxiety.",
            "I struggle — I often delay or eat very slowly with lots of worry.",
            "I eat normally, maybe with minor fussiness.",
            "I eat freely and enjoy meals without a second thought.",
        ],
    },
    {
        "id": 114,
        "name": "Asthenophobia",
        "fear_of": "Fainting or showing weakness",
        "story": (
            "The worst part wasn't feeling dizzy. The worst part was the idea of being seen — "
            "collapsing in public, losing control of her body in front of strangers. When Val "
            "felt lightheaded at the grocery store, she didn't sit down. She white-knuckled the "
            "cart, locked her knees, and powered through the checkout line by sheer will. She'd "
            "rather risk passing out on her own terms in the parking lot than let anyone witness "
            "her falling apart."
        ),
        "question": "You feel dizzy in a crowded place. How do you react?",
        "options": [
            "I'd be consumed with panic — the thought of fainting in public terrifies me.",
            "I'd be very anxious and try to leave or find somewhere private.",
            "I'd sit down and wait for it to pass — mildly concerned.",
            "I'd just take a seat — it happens sometimes, no big deal.",
        ],
    },
    {
        "id": 115,
        "name": "Ombrophobia",
        "fear_of": "Rain or being rained on",
        "story": (
            "The forecast said rain, and just seeing the word on her phone app made Cassidy tense "
            "up. She hated the sound of it against the windows, the way it blurred the world "
            "outside, the cold drops landing on exposed skin like tiny violations. When an "
            "unexpected shower caught her walking home, she pressed under a storefront awning and "
            "waited forty-five minutes for the sky to clear rather than walk three blocks in "
            "the rain."
        ),
        "question": "You're caught outside in an unexpected rainstorm without an umbrella. How do you feel?",
        "options": [
            "I'd seek shelter immediately — being rained on genuinely distresses me.",
            "I'd be very uncomfortable and rush to get indoors.",
            "A bit annoyed, but I'd keep walking.",
            "I'd enjoy it — walking in the rain is refreshing!",
        ],
    },
    {
        "id": 116,
        "name": "Plutophobia",
        "fear_of": "Wealth or becoming wealthy",
        "story": (
            "The bonus was generous — far more than expected. But instead of celebration, Nathan "
            "felt a creeping anxiety. More money meant more to lose, more attention, more "
            "expectations. He'd seen what wealth did to his uncle — the estranged family, the "
            "paranoia, the friends who were only friends while the money lasted. Nathan donated "
            "half the bonus anonymously that same week, not out of charity, but out of a desperate "
            "need to return to safe, comfortable modesty."
        ),
        "question": "You unexpectedly come into a large sum of money. How do you feel?",
        "options": [
            "Anxious — having significant wealth scares me.",
            "Conflicted — the responsibility and attention worry me.",
            "Surprised but pleased — I'd use it wisely.",
            "Thrilled — that's a dream come true!",
        ],
    },
    {
        "id": 117,
        "name": "Anuptaphobia",
        "fear_of": "Staying single forever",
        "story": (
            "Another friend changed their status to 'In a Relationship.' Another wedding invitation "
            "arrived in the mail. Paige smiled and RSVP'd 'plus one,' knowing there was no plus "
            "one. The fear wasn't about being alone right now — it was about being alone forever. "
            "Every birthday that passed without a partner felt like evidence that she was "
            "fundamentally unlovable. The fear drove her into relationships she knew were wrong, "
            "because wrong felt better than empty."
        ),
        "question": "You see friends pairing off and settling down while you're still single. How does it make you feel?",
        "options": [
            "It fills me with deep dread — I'm terrified of being alone forever.",
            "Very anxious — I think about it constantly.",
            "A little wistful, but I trust that things will work out.",
            "I'm perfectly content — being single has its own rewards.",
        ],
    },
    {
        "id": 118,
        "name": "Pistanthrophobia",
        "fear_of": "Trusting other people",
        "story": (
            "After the betrayal — a best friend sharing a secret that was never theirs to tell — "
            "something in Sam calcified. New people were suspects. Kind gestures had hidden "
            "agendas. Compliments were manipulation. Even years later, with new friends who'd never "
            "given reason for doubt, Sam kept an exit strategy for every relationship. Trust was a "
            "door that, once broken, Sam couldn't bring herself to open again."
        ),
        "question": "A new friend shares something personal and asks you to trust them in return. How do you feel?",
        "options": [
            "I can't — trusting people terrifies me to my core.",
            "I'd want to but feel deeply anxious and guarded.",
            "I'd be cautious but open to building trust over time.",
            "I'd trust them — people generally mean well.",
        ],
    },
    {
        "id": 119,
        "name": "Cryophobia",
        "fear_of": "Extreme cold, ice, or frost",
        "story": (
            "The freezer aisle in the grocery store was enough. The blast of cold air when the "
            "door opened, the frost on the glass, the way the chill sank into Rory's fingers and "
            "refused to leave — it all felt threatening. Winter was a months-long siege: icy "
            "sidewalks that could send you crashing down, wind chill that stole your breath, "
            "the numbness creeping into extremities like a slow erasure. Rory wore gloves indoors "
            "from October to April."
        ),
        "question": "You step outside on a bitterly cold winter morning — frost everywhere, wind howling. How do you feel?",
        "options": [
            "Genuine fear — extreme cold makes me feel unsafe and panicked.",
            "Very uncomfortable — I dread cold weather deeply.",
            "Unpleasant, but I bundle up and get through it.",
            "I love cold weather — bring on the frost!",
        ],
    },
    {
        "id": 120,
        "name": "Hippopotomonstrosesquippedaliophobia",
        "fear_of": "Long words",
        "story": (
            "When the biology teacher wrote 'deoxyribonucleic acid' on the whiteboard, most "
            "students just groaned. But for Laynie, seeing that massive word stretched across the "
            "board triggered something beyond annoyance. The letters blurred together, the "
            "syllables tangled in her mouth before she even tried to speak. Being called on to "
            "read long scientific terms aloud was a recurring nightmare — the stumbling, the "
            "laughter, the burning shame of failing at something so supposedly simple."
        ),
        "question": "You're asked to read aloud a passage full of very long, complex words. How do you feel?",
        "options": [
            "Panicked — long words genuinely overwhelm and frighten me.",
            "Very anxious — I'd dread being embarrassed by mispronouncing them.",
            "A little nervous, but I'd give it my best shot.",
            "No problem — I'd enjoy the challenge.",
        ],
    },
]
