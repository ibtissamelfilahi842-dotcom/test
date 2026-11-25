from pathlib import Path

from flask import Flask, send_file

app = Flask(__name__)
video_path = Path(__file__).resolve().parent / "video.mp4"


@app.get("/")
def index():
    return send_file(video_path, mimetype="video/mp4", conditional=True)


if __name__ == "__main__":
    app.run()
