from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps

from app import app
from app import db
from models import User, Book, Rturned, Author, Loan

print(db)

@app.route('/home')
def home():
	
	return render_template("index.html")


@app.route('/', methods=['GET','POST'])
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
	return redirect(url_for('home'))

@app.route('/testing')
def testing():
	return render_template("testing.html")

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/register')
def reg():
	return render_template("register.html")


@app.route('/register', methods=['GET','POST'])
def register():
	error = None
	if request.method == 'POST':
		
		fname = request.form['firstname']
		lname = request.form['lastname']
		dept = request.form['department']
		stud = request.form['studnum']
		em = request.form['email']
		tel = request.form['telnum']
		addr = request.form['address']
		usern = request.form['username']
		pwd = request.form['password']

		userreg = User(firstname = fname, lastname = lname, department = dept, studnum = stud, email = em, telnum = tel, address = addr, username = usern, password = pwd)
		db.session.add(userreg)
		db.session.commit()
		flash('Registered Sucessfully')
	else:
		error = 'Invalid credentials. Please try again.'
	
		return redirect(url_for('home'))
	return render_template("register.html", error = error)

@app.route('/libraryresources')
def libraryresources():
	return render_template("libraryresources.html")

@app.route('/findabook')
def findabook():
	return render_template("findabook.html")

@app.route('/returnbook')
def returnbook():
	return render_template("returnabook.html")



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
def addbook():
	return render_template("addabook.html")

@app.route('/addabook', methods=['GET','POST'])
def addabook():
	error = None
	if request.method == 'POST':


		title1 = request.form['title']
		author1 = request.form['author']
		subject1 = request.form['subject']
		section1 = request.form['section']
		publisher1 = request.form['publisher']
		pubyear1 = request.form['pubyear']
		isavailable1 = request.form['isavailable']
		isloaned1 = request.form['isloaned']
		isreturned1 = request.form['isreturned']

		bookreg = Book(title = title1, author = author1, subject = subject1, section = section1, publisher = publisher1, pubyear = pubyear1, isavailable = isavailable1, isloaned = isloaned1, isreturned = isreturned1)
		db.session.add(bookreg)
		db.session.commit()
		flash('Added Sucessfully')
	
	else:
		error = 'Invalid credentials. Please try again.'
		return redirect(url_for('home'))
	
	return render_template('addabook.html', error = error)

@app.route('/loanbook')
def loanbook():
	mylistofbooks = []
	allbooks = db.session.query(Book).order_by(Book.title)
	
	return render_template("loanabook.html", allbooks = allbooks)
'''
@app.route('/loanbook', methods=['GET','POST'])
def loanbk():
	mylistofbooks = []
	return render_template("loanbook.html")
'''