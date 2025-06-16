from flask import Flask, request, render_template
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score, make_scorer
import pandas as pd

import main

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")




@app.route('/recommendation', methods=["POST", "GET"])
def recommendation():
    if request.method == "POST":
        form = request.form
        song_title = str(form['track_name'])
        song_artist = str(form['track_artist'])
        song_name, song_artist, song_url, album_image, user_song_name, user_song_artist = main.begin(
            song_title=song_title,
            song_artist=song_artist)
        if song_name is None and song_url is None:
            return render_template("prediction.html",
                                   error="Could not find that track. Make sure you entered the details correctly")

        return render_template("prediction.html", song_name=song_name, song_artist=song_artist,
                               song_url=song_url, album_image=album_image, user_song=user_song_name,
                               user_artist=user_song_artist)

    if request.method == "GET":
        return render_template("prediction.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
