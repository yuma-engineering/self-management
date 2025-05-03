from flask import render_template,Blueprint,request,redirect,url_for
from backend.models import Do,db,Doday,Goal
from backend.forms import DoForm
from datetime import date,timedelta


product_db=Blueprint('product',__name__,template_folder='templates')

@product_db.route('/')
def top():
   return render_template('start.html')

@product_db.route('/delete/<int:id>')
def delete(id):
   d_item=Do.query.filter_by(id=id).first()
   db.session.delete(d_item)
   db.session.commit()
   return redirect(url_for('login_db.index'))

@product_db.route('/yes',methods=['GET','POST'])
def result():
   #タスクの合計
   task_list = Do.query.all()
   sum=0
   for d in task_list:
      sum += d.time
   do=Doday(
      time=sum
   )
   db.session.add(do)
   db.session.commit()
   Do.query.delete()      
   db.session.commit() 

   #一週間での集計
   today= date.today()

   this_week_start = today - timedelta(days=today.weekday())
   this_week_end = this_week_start + timedelta(days=6)

   last_week_start = this_week_start - timedelta(days=7)
   last_week_end = this_week_end - timedelta(days=7)

   this_week_sum = db.session.query(db.func.sum(Doday.time))\
         .filter(Doday.date.between(this_week_start, this_week_end))\
        .scalar() or 0

   last_week_sum = db.session.query(db.func.sum(Doday.time))\
        .filter(Doday.date.between(last_week_start, last_week_end))\
        .scalar() or 0

   diff = this_week_sum - last_week_sum

   #selectの値を取得

   #学習時間と目標の関係によってmessageを返す
   message=''
   goal = Goal.query.order_by(Goal.id.desc()).first()
   if goal and goal.time <= sum:
            message='よく頑張りました。明日も頑張りましょう。'
   else:
            message='今日は目標達成出来ませんでしたが、明日から頑張りましょう。'

   return render_template('result.html',sum=sum,this_week=this_week_sum, last_week=last_week_sum, diff=diff,message=message,goal=goal)






