from flask import Flask, render_template



app = Flask(__name__, 
static_url_path="",
static_folder="static",
template_folder="templates")



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/tech")
def tech():
    return render_template("tech.html")



if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)