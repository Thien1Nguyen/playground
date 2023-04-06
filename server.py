from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/<int:int>/<color>')
def box(int, color):
    return render_template("index.html", int=int, color= color)

if __name__ =="__main__":
    app.run(debug = True)