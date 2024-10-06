from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/types")
def types():
    return render_template("exoplanets.html")

@app.route("/types/gas-giants")
def gasGiants():
    return render_template("gas-giants.html")

@app.route("/51-Pegasi")
def pegasi_51():
    return render_template("51-pegasi.html")

@app.route("/types/neptunian-planets")
def neptunian():
    return render_template("neptunian-planets.html")

@app.route("/hat-p")
def hat_p():
    return render_template("hat-p.html")

@app.route("/types/super-earth")
def super_earth():
    return render_template("super-earth.html")

@app.route("/toi-700")
def toi_700():
    return render_template("toi-700.html")

@app.route("/toi-system")
def toi_system():
    return render_template("toi-700-system.html")

@app.route("/types/terristrial-planets")
def terristrial():
    return render_template("terristrial-planets.html")

@app.route("/kepler-78")
def kepler_78():
    return render_template("kepler-78.html")

@app.route("/study")
def study():
    return render_template("study.html")


if __name__ == "__main__":
    app.run(debug=True)