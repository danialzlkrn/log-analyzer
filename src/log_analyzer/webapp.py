from flask import Flask, render_template
from analyzer import analyze_log

app = Flask(__name__)

LOG_FILE = "../../sample_logs/apache_access.log"
@app.route("/")
def dashboard():
    data = analyze_log(LOG_FILE)
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)