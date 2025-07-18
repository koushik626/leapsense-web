from flask import Flask, render_template_string
from datetime import datetime
import os

app = Flask(__name__)
LOG_FILE = "leapsec_log.txt"

@app.route("/")
def dashboard():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
    else:
        logs = ["No logs found."]

    html = """
    <html>
        <head><title>LeapSense Dashboard</title></head>
        <body>
            <h2>LeapSense - Negative Leap Second Logs</h2>
            <ul>
            {% for log in logs %}
                <li>{{ log }}</li>
            {% endfor %}
            </ul>
        </body>
    </html>
    """
    return render_template_string(html, logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
