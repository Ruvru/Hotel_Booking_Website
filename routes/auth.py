from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_user,logout_user,login_required,current_user
from extension import db
from models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

#Registration
@auth_bp.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password_hash = request.form['password']
        phone_number = request.form['phone']


        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email address already exists')
            return redirect(url_for('auth.register'))

        user=User.query.filter_by(username=username,email=email,phone_number=phone_number)
        user.set_password_hash(password_hash)

        db.session.add(user)
        db.session.commit()

        flash('Registration Successful! Please login.','success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

#Login
@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if request.method == 'POST':
        email = request.form['email']
        password_hash = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password_hash):
            login_user(user,remember=True)
            flash(f'Welcome back,{user.username}!','success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password','danger')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html')

#logout
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out','success')
    return redirect(url_for('main.home'))


# We'll add login/register routes later