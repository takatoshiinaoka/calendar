#check_mail.py
from django.core.management.base import BaseCommand, CommandError

from calendarSite.models import Task
from calendarSite.models import User_Task
from calendarSite.models import Subject
from calendarSite.models import User_Subject

from django.contrib.auth.models import User

#import pandas as pd
import datetime #日付や時間を指定するモジュール
import smtplib #メールさメールサーバーを操作してメールを送信する SMTP
import ssl #暗号化や認証の仕組み
from email.mime.text import MIMEText #メールを日本語で送信できるようにするためのモジュール
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
from email.mime.multipart import MIMEMultipart #メール本文以外に添付ファイルを送信できるようにする
from email.mime.base import MIMEBase #添付ファイルの形式を指定する
from email import encoders #添付ファイルをメールで送ることができるようにする


gmail_account = ""
gmail_password = "fitrakugaku"

#gmailを送る関数
def gmail_send(send_name, mail_to, task, delivery_date ):
  subject = "課題「{1}」の締切が近づいています。".format(send_name,task)
  body = '''こんにちは、{0}さん<br>
            課題「{1}」の締切が近づいています。<br>
            myFITまたは各案内をご確認ください。<br>
            期限は{2}となります。<br><br>
            プロジェクト型演習team1メンバーより'''.format(send_name,task,delivery_date)
  msg=MIMEMultipart()
  msg['Subject'] = subject
  msg['To'] = mail_to
  msg['From'] = gmail_account
  msg_body = MIMEText(body, "html")
  msg.attach(msg_body)
  server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
  server.login(gmail_account, gmail_password)
  server.send_message(msg)
  server.close()

def check(task_obj):
  for task in task_obj:
    auth_obj=User.objects.all()
    #print("task_id :"+str(task.id)+" name: "+(task.name)+" sub_id:"+str(task.subject_id_id)+" end:"+str(task.end))
    Usertask_obj = User_Task.objects.filter(task_id_id=task.id).all() 
    for Usertask in Usertask_obj: 
      if(Usertask.user_id != "None"):#ログインユーザのタスク
        #print("user_id: "+Usertask.user_id+"  task_id: "+str(Usertask.task_id_id))#タスクのUserid
        for auth in auth_obj:
          if(str(auth.id) == Usertask.user_id):
            #print("user_id:"+str(auth.id)+" user_id:"+Usertask.user_id+" email:"+auth.email+"  username:"+auth.username)
            gmail_send(auth.username, auth.email, task.name , task.end.strftime('%Y/%m/%d %H:%M:%S'))
            #print("送信完了")

# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = 'Check if you can send an email'

    

    def handle(self, *args, **options):
      today_date = datetime.date.today()
      now_x=datetime.datetime.now()

      now = now_x.strftime('%Y-%m-%d %H:%M:%S')
      #print("now   : "+str(now))
      now_s=now_x.strftime('%Y-%m-%d %H:%M:00')
      #print("now 0s: "+str(now_s))

      #end丁度の時刻
      task_obj = Task.objects.filter(end=now_s).all() 
      check(task_obj)

      #endの1時間前
      now_h = (now_x-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:00')#print("now+1h: "+str(now_h)
      task_obj = Task.objects.filter(end=now_h).all() 
      check(task_obj)

      #endの1日前
      now_d = (now_x-datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:00')#print("now+1d: "+str(now_d))
      task_obj = Task.objects.filter(end=now_d).all() 
      check(task_obj)



      #Usertask = User_Task.objects.filter().get(id!=None)
      
      #user_taskテーブルには未実施のタスクのみ保存されている。課題が終わると、usertaskテーブルから消される
      #Usertask = User_Task.objects.filter().all() 
      # for i in Usertask: 
      #   if(i.user_id != "None"):#ログインユーザのタスク
      #     print("user_id: "+i.user_id+"  task_id: "+str(i.task_id_id))#タスクのUserid
      #      #print("task_id: "+str(i.task_id_id))#タスクのUserid

      #mailアドレスとユーザ名取得
      # user_obj=User.objects.all()
      # for j in user_obj:
      #   print("email: "+j.email+"  pw:"+j.username)

      #締切日取得 subject_id=科目名、subject_id_id=科目id

      
      
      #print(now+ datetime.timedelta(days=1))
      #print(Usertask)
      #gmail_send("s20a2005", "s20a2005@bene.fit.ac.jp", "課題1:テスト", "2022/1/2" )
      #print("hello")
