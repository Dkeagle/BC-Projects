from flask import Flask, render_template, redirect, request, url_for, flash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd7a70bcb88e5c190838b4c12fbf0a26efbf328bcf55ebdf5'

def validate(post_content):
    """validate every input from the form with a RegEx, returns True when done"""
    pc = post_content
    
    return True

def check(post_content):
    """check every input from the form and flash error message when needed, returns True when done"""
    pc = post_content
    err = 0
    if not pc.form["first_name"]:
        flash("fn_empty")
        err += 1
    if not pc.form["last_name"]:
        flash("ln_empty")
        err += 1
    if not pc.form["mail"]:
        flash("mail_empty")
        err += 1
    if not pc.form["gender"]:
        flash("gender_empty")
        err += 1
    if not pc.form.get("country"):
        flash("country_empty")
        err += 1
    if not pc.form.get("reason"):
        flash("reason_empty")
        err += 1
    if not pc.form["content"]:
        flash("content_empty")
        err += 1
    return False if err else True

@app.route('/', methods=['GET', 'POST'])
def main():
    """main function, executed when people access the main page"""
    if request.method == 'POST':
        if check(request):
            if validate(request):
                return redirect(url_for('thanks'), code=307)

    return render_template("form.html")

@app.route('/thanks', methods=['POST'])
def thanks():
    """thanks function display the 'thanks for contacting us' page when the form is send and valid"""
    return render_template("thanks.html")