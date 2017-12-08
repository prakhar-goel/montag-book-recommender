from flask import request, render_template, redirect, flash, url_for
from app import db
from app import models
from flask_login import current_user, login_required, login_user, logout_user
from .form import UserForm

from . import auth

@auth.route("/signup", methods=["GET", "POST"])
def signup():
	form = UserForm(request.form)
	if request.method == "POST":
		if form.validate_on_submit():
			user = models.User(email=form.email.data)
			user.set_password(form.password.data)
			db.session.add(user)
			db.session.commit()
			login_user(user)
			flash('You have successfully signed up!')

		return redirect(url_for("home.index"))

	return render_template("auth/signup.html", form=form)

@auth.route('/login', methods=["GET", "POST"])
def login():
	form = UserForm(request.form)
	if request.method == "POST":
		if form.validate_on_submit():
			user = models.User.query.filter_by(email=form.email.data).first()
			print("GOTEM!!")
			if user is not None and user.check_password(form.password.data):
				print("FOUNDEM!")
				user.authenticated = True
				db.session.add(user)
				db.session.commit()
				login_user(user)
				flash('Welcome back!')
				return redirect(url_for("home.index"))
			else:
				flash('Email or password not valid.', 'error')

	return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	current_user.authenticated = False
	db.session.add(current_user)
	db.session.commit()
	logout_user()
	return redirect(url_for('.login'))