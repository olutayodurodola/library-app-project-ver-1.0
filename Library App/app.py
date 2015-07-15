
from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)

app.secret_key = "myprecious"

@app.route('/')
def home():
	#return "Hello, World!"
	return render_template("index.html")


@app.route('/welcome')
def welcome():
	return render_template("welcome.html")

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method =='POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			session['logged_in'] = True
			flash('You were just logged in!')
			return redirect(url_for('home'))
	return render_template('login.html',error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were just logged out!')
	return redirect(url_for('welcome'))

@app.route('/testing')
def testing():
	return render_template("testing.html")

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/register')
def register():
	return render_template("register.html")

@app.route('/libraryresources')
def libraryresources():
	return render_template("libraryresources.html")

@app.route('/findabook')
def findabook():
	return render_template("findabook.html")

@app.route('/returnbook')
def returnbook():
	return render_template("returnabook.html")

@app.route('/loanbook')
def loanbook():
	return render_template("loanabook.html")

@app.route('/aboutus')
def aboutus():
	return render_template("aboutus.html")

@app.route('/listbooks')
def listbooks():
	return render_template("books.html")

@app.route('/listmagazines')
def listmagazines():
	return render_template("magazines.html")

@app.route('/listperiodicals')
def listperiodicals():
	return render_template("periodicalsandjournals.html")

@app.route('/listreports')
def listreports():
	return render_template("reports.html")

@app.route('/listmaps')
def listmaps():
	return render_template("maps.html")

@app.route('/searchforbook')
def searchforbook():
	return render_template("searchlibrary.html")

@app.route('/addabook')
def addabook():
	return render_template("addabook.html")

if __name__ == '__main__':
	app.run(debug=True)