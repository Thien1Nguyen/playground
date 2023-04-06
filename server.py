from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def fix_box(int= 3, color ="cornflowerblue"):
    return render_template("index.html", int=int, color= color)

@app.route('/play/<int:int>')
def int_box(int, color ="cornflowerblue"):
    return render_template("index.html", int=int, color= color)

@app.route('/play/<int:int>/<string:color>')
def box(int, color ="cornflowerblue"):
    return render_template("index.html", int=int, color= color)

if __name__ =="__main__":
    app.run(debug = True)