from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/insights")
def insights():
    # Sample analytics data (can be made dynamic later)
    data = {
        "popular_brands": ["Zara", "H&M", "Nike"],
        "top_categories": ["Streetwear", "Ethnic", "Formal"],
        "user_stats": {"women": 58, "men": 42},
        "trending_colors": ["Beige", "Lavender", "Olive Green"]
    }
    return render_template("insights.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
