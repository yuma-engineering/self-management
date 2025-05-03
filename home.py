from backend.result import product_db 
from backend.models import db,Goal
from flask import request,render_template,redirect,url_for

@product_db.route('/goal',methods=['POST'])
def goaltime():
  select_goal=request.form.get('goal',0)if request.method == 'POST' else 0
  goal=Goal(time=select_goal)
  db.session.add(goal)
  db.session.commit()
  return redirect(url_for('login_db.index'))

@product_db.route('/window')
def window():
  return render_template('window.html')

@product_db.route('/no',methods=['POST'])
def no():
  return redirect(url_for('login_db.index'))


