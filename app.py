from flask import Flask,render_template
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("Homepage.html")

@app.route("/Images")
def Images():
    return render_template("Images.html")

@app.route("/Tables")
def Tables():
    return render_template("Tables.html")

    
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)
    # mole