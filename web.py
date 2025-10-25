from flask import Flask
import os
import main  # импорт твоего основного файла, где бот запускается

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running on Render!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)