import datetime
import random
import os

affiliate = "https://www.linkconnector.com/ta.php?lc=007949000012003621&atid=HatsCaps&url=https%3A%2F%2Fhats.com%2F%3Fq%3Darmy%2Bbaseball%2Bcaps"

topics = [
    "Army Baseball Caps",
    "Snapback Streetwear Hats",
    "Military Style Caps",
    "Outdoor Tactical Caps",
    "Summer Baseball Caps Trends",
    "Camo Caps Fashion Guide",
    "Best Caps for Sun Protection"
]

keywords = [
    "buy baseball caps online",
    "army caps for men",
    "best snapback hats",
    "military style hats fashion",
    "trucker caps breathable",
    "camo hats outfit ideas"
]

today = datetime.date.today().isoformat()
topic = random.choice(topics)

file_name = f"blogs/blog-{today}.html"

html = f"""<!DOCTYPE html>
<html>
<head>
<title>{topic} - Daily Hat Guide {today}</title>

<meta name="description" content="Daily SEO guide about {topic}. Learn styles, trends and where to buy premium caps online.">
<meta name="keywords" content="{', '.join(random.sample(keywords, 4))}">

</head>
<body>

<h1>{topic} – Complete Guide</h1>

<p>Welcome to today’s daily fashion guide about {topic}. This article explores trends, usage, and buying tips.</p>

<h2>Why {topic} is Trending</h2>
<p>Global fashion trends are pushing demand for stylish and durable caps in everyday wear.</p>

<h2>Best Uses</h2>
<ul>
<li>Outdoor wear</li>
<li>Street fashion</li>
<li>Sports activities</li>
<li>Travel protection</li>
</ul>

<h2>Buying Guide</h2>
<p>Choose high-quality caps based on material, fit, and durability.</p>

<h2>Where to Buy</h2>
<p>
<a href="{affiliate}">Shop Premium Caps on Hats.com</a>
</p>

<h2>SEO Tip of the Day</h2>
<p>Focus on long-tail keywords like "best {topic.lower()} for summer outfits".</p>

<footer>
<p>Daily automated SEO blog generated on {today}</p>
</footer>

</body>
</html>
"""

os.makedirs("blogs", exist_ok=True)

with open(file_name, "w", encoding="utf-8") as f:
    f.write(html)

print("Blog generated:", file_name)
