from flask import Flask, render_template

app = Flask('app')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/jauns_piedzivojums')
def jauns_piedzivojums():
    return render_template("jauns_piedzivojums.html")


app.run(host='0.0.0.0', port=8080)
