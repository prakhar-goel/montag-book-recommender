""" Montag Book Recommender """

from flask import Flask, render_template
from app import models
from werkzeug import generate_password_hash, check_password_hash
from app import db
from . import home
from flask import request, flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

@home.route("/")
def main():
	return render_template("home/index.html")

@home.route("/showSignUp")
def showSignUp():
    return render_template("home/signup.html")

@home.route('/signUp', methods=['POST'])
def signUp():
	# read the posted values from the UI
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	# validate the received values
	if _email and _password:
		_hashed_password = generate_password_hash(_password)
		addUser = models.User(email=_email, password=_hashed_password)
		db.session.add(addUser)
		db.session.commit()
		flash('You have successfully registered!')

		return redirect(url_for(".main"))	

@home.route('/showSignin')
def showSignin():
#       if session.get('user'):
#               return render_template('userHome.html')
#       else:
        return render_template('home/signin.html')

@home.route("/users")
def show_users():
	res = ""
	for user in models.User.query.limit(5).all():
		res += "<p>" + str(user) + ", " + user.location + "</p>"

	return res

@home.route("/books")
def show_books():
	res = ""
	for book in models.Book.query.limit(5).all():
		res += "<p>" + str(book) + ", " + book.title + "</p>"

	return res

@home.route("/ratings")
def show_ratings():
	joined = models.Rating.query.join(models.Book, models.Rating.uid == models.Book.isbn)
	print(joined)

	res = ""
	for rating in joined.limit(5).all():
		res += "<p>" + rating.title + ", " + str(rating.rating) + "</p>"

	return res