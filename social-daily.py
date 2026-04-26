import datetime
import random

affiliate = "https://www.linkconnector.com/ta.php?lc=007949000012003621&atid=HatsCaps&url=https%3A%2F%2Fhats.com%2F%3Fq%3Darmy%2Bbaseball%2Bcaps"

topics = [
    "Army Baseball Caps",
    "Snapback Streetwear Hats",
    "Military Style Caps",
    "Camo Tactical Caps",
    "Outdoor Baseball Caps Trends"
]

topic = random.choice(topics)
today = datetime.date.today().isoformat()

# ---------------------------
# X (Twitter) POST
# ---------------------------
x_post = f"""
🧢 Daily Hat Trend ({today})

{topic} are dominating fashion right now.

🔥 Durable
🔥 Stylish
🔥 Global streetwear essential

Shop here 👉 {affiliate}

#hats #baseballcaps #streetwear #fashion
"""

# ---------------------------
# FACEBOOK POST
# ---------------------------
facebook_post = f"""
🧢 DAILY STYLE UPDATE

Today’s spotlight: {topic}

Baseball caps continue to grow globally because they combine comfort, identity, and function.

Whether for fashion or outdoor use, this trend is expanding fast.

👉 Shop here:
{affiliate}
"""

# ---------------------------
# LINKEDIN POST (professional tone)
# ---------------------------
linkedin_post = f"""
Baseball caps like {topic} are becoming a global fashion and utility trend.

They are widely used in:
- Outdoor industries
- Sports culture
- Streetwear fashion markets

More people are choosing functional fashion accessories that combine style and durability.

Explore here:
{affiliate}
"""

# ---------------------------
# REDDIT POST (informational style)
# ---------------------------
reddit_title = f"Why {topic} Are Trending in 2026"
reddit_body = f"""
Baseball caps such as {topic} are gaining popularity due to their versatility and global appeal.

They are commonly used for:
- Fashion styling
- Outdoor protection
- Sports and casual wear

More info:
{affiliate}
"""

# Save outputs
with open("social-output.txt", "w", encoding="utf-8") as f:
    f.write("X POST:\n" + x_post + "\n\n")
    f.write("FACEBOOK POST:\n" + facebook_post + "\n\n")
    f.write("LINKEDIN POST:\n" + linkedin_post + "\n\n")
    f.write("REDDIT TITLE:\n" + reddit_title + "\n")
    f.write("REDDIT BODY:\n" + reddit_body + "\n")

print("Social posts generated")
