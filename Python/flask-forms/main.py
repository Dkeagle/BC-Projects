from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd7a70bcb88e5c190838b4c12fbf0a26efbf328bcf55ebdf5'

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        mail = request.form['mail']
        country = request.form.get('country')
        gender = request.form['gender']
        reason = request.form['reason']
        content = request.form['content']

        return redirect(url_for('thanks',first_name=first_name, code=307))

    return render_template("form.html")

@app.route('/thanks', methods=['POST'])
def thanks():
    return render_template("thanks.html")