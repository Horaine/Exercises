from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c05932cc1dea4a58ec4d4c0af6467767'

posts = [
    {
        'author' : 'John Brown',
        'title' : 'Post 1',
        'content' : 'First PictoGram post',
        'date_posted' : 'May 6, 2020'
    },

    {
        'author' : 'Gwen Lyn',
        'title' : 'Post 2',
        'content' : 'Second PictoGram post',
        'date_posted' : 'May 7, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html', posts=posts)

@app.route("/contact")
def contact():
    return render_template('Contact.html', title = 'Contact')

@app.route("/about")
def about():
    return render_template('About.html', title =  'About')



@app.route("/register", methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('Register.html', title =  'Registration', form=form)


@app.route("/Login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@domain.com' and form.password.data == 'password':
            flash('Logged in Successfully', 'Success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your username or password', 'Danger')
    return render_template('Login.html', title =  'Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)