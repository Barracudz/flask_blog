from flask import render_template, url_for, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author' : 'Hallvard Lunde Hervig',
        'title' : 'My first blog post',
        'content' : 'Hi, this is my first sentence',
        'date_posted' : '23.03.21'
    },
    {
        'author' : 'Hallvard Lunde Hervig',
        'title' : 'Blog update',
        'content' : 'Hi, this is a small update bla bla',
        'date_posted' : '23.03.21'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About page')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # Tells us if form was validated, take user to home page
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
