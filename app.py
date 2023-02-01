from flask import Flask,render_template
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("Homepage.html")

@app.route("/Characters")
def Characters():
    return render_template("Characters-main.html")

@app.route("/Runes")
def Runes():
    return render_template("Runes-main.html")

@app.route("/Upgrades")
def Upgrades():
    return render_template("Upgrades-main.html")

@app.route("/Weapons")
def Weapons():
    return render_template("Weapons-main.html")

@app.route('/Weapons/<weapon>')
def show_weapon(weapon):
    return f"{weapon} is good."
    
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)
    # mole