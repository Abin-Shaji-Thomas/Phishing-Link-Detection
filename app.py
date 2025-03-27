from flask import Flask, render_template, request
from detector import is_phishing_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            result = is_phishing_url(url)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
