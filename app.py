from flask import Flask, request, render_template
import main  # Your main module

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit-form", methods=["POST"])
def submit_form():
    choice = request.form.get("choice")
    username = request.form.get("username")
    message = request.form.get("message")

    url = main.create_twitter_action_url(choice, username, message, headless=True)

    if url:
        return (f'<div class="result-card">'
                f'<code id="urlText">{url}</code> '
                f'<span class="copy-icon" onclick="copyToClipboard(\'urlText\')">&#x1f4cb;</span>'
                '</div>')
    else:
        return "Invalid choice or action failed."

if __name__ == "__main__":
    app.run(debug=True)
