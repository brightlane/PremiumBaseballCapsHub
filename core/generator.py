import datetime
from core.trends import get_trend

affiliate = "https://www.linkconnector.com/ta.php?lc=007949000012003621&atid=HatsCaps&url=https%3A%2F%2Fhats.com%2F%3Fq%3Darmy%2Bbaseball%2Bcaps"

def generate():
    topic = get_trend()
    date = datetime.date.today().isoformat()

    hooks = [
        "This is blowing up right now:",
        "Nobody is talking about this trend yet:",
        "Fashion insiders are watching this:",
        "This style is everywhere in 2026:"
    ]

    hook = random.choice(hooks)

    return {
        "topic": topic,
        "date": date,
        "x": f"""🧢 {hook}

{topic}

🔥 trending globally in fashion circles
🔥 simple, clean, high-impact style

Shop here 👉 {affiliate}

#hats #fashion #streetwear #style""",

        "facebook": f"""
🧢 DAILY STYLE UPDATE

{topic} is becoming a global fashion trend.

People love it because it blends style + function.

👉 Shop here:
{affiliate}
""",

        "reddit": {
            "title": f"Why {topic} is trending in 2026",
            "body": f"""
{topic} is becoming more popular due to its versatility in fashion and outdoor use.

It is widely used in:
- streetwear fashion
- outdoor protection
- casual styling

More info:
{affiliate}
"""
        }
    }
