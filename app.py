from flask import Flask
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = '123'

boggle_game = Boggle()

@app.route('/')
def homepage():
    """ Create home page for game"""

    board = boggle_game.make_board()
    session ['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template("index.html", board=board, highscore=highscore, nplays=nplays)

@app.route("/check-word")
def check_word():
    """Check if word is in dict"""

    word = request.args("word")
    board = session["board"]
    response = boggle_game.check_valid_word()

    return jsonify({'Result' : response})

@app.route("/post-score", method=['POST'])
def post_score():
    """Receive score, update nplays, update highscore if applicable"""

    score = request.json("score")
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    session["nplays"] = nplays + 1
    session["highscore"] = max(score, highscore)

    return jsonify(brokeRecord= score > highscore)
    
