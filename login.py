from flask import Blueprint,render_template,redirect,url_for,flash,jsonify,request
from flask_login import current_user,login_required,login_user,logout_user
from backend.forms import LoginForm,RegistrationForm,DoForm
from backend.models import db,User,Do,Goal
from backend.result import product_db
from flask_cors import CORS


login_db=Blueprint('login_db',__name__,template_folder='templates')

CORS(login_db, supports_credentials=True)


@login_db.route('/api/do', methods=['POST', 'GET'])
@login_required
def index():
    if request.method == 'POST':
        data = request.get_json()
        todo = data.get('todo')
        time = data.get('time')

        if not todo or not time:
            return jsonify({"success": False, "error": "Missing data"}), 400

        do = Do(todo=todo, time=time, user_id=current_user.id)
        db.session.add(do)
        db.session.commit()

        return jsonify({"success": True})

    # GETリクエスト時の処理
    goal = Goal.query.filter_by(user_id=current_user.id).order_by(Goal.id.desc()).first()
    do_list = Do.query.filter_by(user_id=current_user.id).all()
    response = {
        'goal': goal.time if goal else None,
        'tasks': [{'todo': d.todo, 'time': d.time} for d in do_list]
    }
    return jsonify(response)

@login_db.route('/api/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('ログインに成功しました。')
            return redirect(url_for('login_db.index'))
        else:
            flash('ユーザー名またはパスワードが無効です。')
    return render_template('login.html', form=form)

@login_db.route('/api/logout')
@login_required
def logout():
    logout_user()
    flash('ログアウトしました。')
    return redirect(url_for('login_db.login'))

@login_db.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('ユーザー登録が完了しました。')
        return redirect(url_for('login_db.login'))
    return render_template('register.html', form=form)

import backend.result
import backend.home 


