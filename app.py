from flask import Flask, render_template, request, redirect, url_for
import pytube
import os
from pathlib import Path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        quality = request.form['quality']
        download_video(video_url, quality)

    return render_template('index.html')

def download_video(video_url, quality):
    video = pytube.YouTube(video_url)
    if quality == 'highest':
        video_stream = video.streams.get_highest_resolution()
    elif quality == 'lowest':
        video_stream = video.streams.get_lowest_resolution()
    # Add more quality options and conditions as needed
    else:
        video_stream = video.streams.get_highest_resolution()  # Default to highest quality

    # Get the user's home directory
    home_dir = str(Path.home())

    # Get the default Downloads folder for the user's operating system
    downloads_dir = os.path.join(home_dir, 'Downloads')

    video_stream.download(downloads_dir)

if __name__ == '__main__':
    app.run(debug=True)
