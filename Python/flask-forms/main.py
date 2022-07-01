from flask import Flask, render_template, redirect, request, url_for, flash, session
import re
import bleach as bl
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd7a70bcb88e5c190838b4c12fbf0a26efbf328bcf55ebdf5'

def sanitize(post_content):
    """sanitize every input field using the bleach module"""
    pc = post_content
    for v in pc.form.values():
        v = bl.clean(v)
    return True

def validate(post_content):
    """validate every input from the form with a RegEx, returns True when done"""
    pc = post_content
    err = 0
    name_regex = "[a-zA-Z-]+"
    mail_regex = "[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+"

    if not re.match(name_regex, pc.form["first_name"]):
        flash("fn_incorrect")
        err += 1
    if not re.match(name_regex, pc.form["last_name"]):
        flash("ln_incorrect")
        err += 1
    if not re.match(mail_regex, pc.form["mail"]):
        flash("mail_incorrect")
        err += 1
    return False if err else True

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
                if sanitize(request):
                    print(request.form, file=sys.stderr)
                    session["form_data"] = request.form
                    return redirect(url_for('thanks'), code=307)

    return render_template("form.html")

@app.route('/thanks', methods=['POST'])
def thanks():
    """thanks function display the 'thanks for contacting us' page when the form is send and valid"""
    return render_template("thanks.html", form_data=session["form_data"])