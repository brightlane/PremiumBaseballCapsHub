import datetime
import random

affiliate = "https://www.linkconnector.com/ta.php?lc=007949000012003621&atid=HatsCaps&url=https%3A%2F%2Fhats.com%2F%3Fq%3Darmy%2Bbaseball%2Bcaps"

topics = [
    "Army Baseball Caps",
    "Snapback Streetwear Hats",
    "Military Style Caps",
    "Camo Hats Trends",
    "Outdoor Tactical Caps"
]

topic = random.choice(topics)

today = datetime.date.today().isoformat()

# Social captions (X / Twitter style)
x_post = f"""
🧢 Daily Hat Drop ({today})

{topic} are trending worldwide right now.

🔥 Durable
🔥 Stylish
🔥 Perfect for outdoor wear

👉 Shop here: {affiliate}

#hats #baseballcaps #streetwear #fashion
"""

# Facebook style (longer)
facebook_post = f"""
🧢 DAILY STYLE UPDATE

Today’s focus: {topic}

Baseball caps continue to dominate global fashion because they combine comfort, style, and functionality.

Whether you're into streetwear or outdoor gear, this trend is growing fast.

Shop premium caps here:
{affiliate}
"""

# Reddit style (informational)
reddit_post = f"""
Title: Why {topic} Are Trending in 2026

Body:
Baseball caps like {topic} are becoming more popular due to their versatility and global fashion appeal.

They are used in:
- Streetwear fashion
- Outdoor activities
- Sports culture

You can explore premium options here:
{affiliate}
"""

print("X POST:\n", x_post)
print("\nFACEBOOK POST:\n", facebook_post)
print("\nREDDIT POST:\n", reddit_post)

# Save for manual or API use
with open("social-posts.txt", "w", encoding="utf-8") as f:
    f.write(x_post + "\n\n" + facebook_post + "\n\n" + reddit_post)
