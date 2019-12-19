from flask import render_template, flash, redirect, url_for
from app import f
from app.forms import LoginForm


@f.route('/')
@f.route('/index')
def index():
    user = {'username': 'Tomasz'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Post from John'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Post from Susan'
        }
    ]
    return render_template('index.html',
                           title='Home Page',
                           user=user,
                           posts=posts)


@f.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.
              format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
