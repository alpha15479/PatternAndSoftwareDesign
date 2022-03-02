from flask import Flask, render_template, request
from crape import Crape, Charcoal, Normal
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/order',methods = ['POST', 'GET'])
def order():
    if request.method == 'POST':
        order = request.form.to_dict()
        Crape(order, Charcoal)
        Crape(order, Normal)
        if order["batter"] == "charcoal":
            x = render_template("home.html", charcoal = Crape(order, Charcoal))
        elif order["batter"] == "normal":
            x = render_template("home.html", normal = Crape(order, Normal))
    return x
app.run(debug=True)