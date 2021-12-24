from django.forms.widgets import PasswordInput
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User 
from calendarSite.models import Calendar
from calendarSite.models import Task
from calendarSite.models import User_Task
from calendarSite.models import Subject
from calendarSite.models import User_Subject
from calendarSite.models import Log
from calendarSite.models import Comment

class IndexTests(TestCase):
  """IndexViewのテストクラス"""

  def test_get(self):
    """トップページにアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)


class SubjectListTests(TestCase):

  def setUp(self):
    """
    テスト環境の準備用メソッド。名前は必ず「setUp」とすること。
    同じテストクラス内で共通で使いたいデータがある場合にここで作成する。
    """
    
    post1 = Subject(name='人工知能応用').save()
    post2 = Subject.objects.create(name='プロジェクト型演習')

  def test_get(self):
    """subjectにアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('subject'))
    self.assertEqual(response.status_code, 200)

  def test_get_2posts_by_list(self):
    """GET でアクセス時に、setUp メソッドで追加した 2件追加が返されることを確認"""
    response = self.client.get(reverse('subject'))
    self.assertEqual(response.status_code, 200)
    self.assertQuerysetEqual(
      # Subjectモデルでは __str__ の結果として科目名を返す設定なので、返される科目名が投稿通りになっているかを確認
      response.context['subject_list'],
      ['<Subject: 人工知能応用>', '<Subject: プロジェクト型演習>'],
      ordered = False # 順序は無視するよう指定
    )
    self.assertContains(response, '人工知能応用') # html 内に post1 の name が含まれていることを確認
    self.assertContains(response, 'プロジェクト型演習') # html 内に post2 の name が含まれていることを確認

  def tearDown(self):
      """
      setUp で追加したデータを消す、掃除用メソッド。
      create とはなっているがメソッド名を「tearDown」とすることで setUp と逆の処理を行ってくれる＝消してくれる。
      """
      post1 = Subject.objects.create(name='人工知能応用')
      post2 = Subject.objects.create(name='プロジェクト型演習')
import random
class SabjectManageTest(TestCase):
  username = str(random.random())
  def setUp(self):
    """
    テスト環境の準備用メソッド。名前は必ず「setUp」とすること。
    同じテストクラス内で共通で使いたいデータがある場合にここで作成する。
    """
    #科目作成
    post1 = Subject(name='科目1').save()

    #ユーザー作成
    post2 = User(
            username=self.username,
            email = 'test@gmail.com',
            password = 'kimatsusikenn',
         ).save()
    subject = Subject.objects.order_by('-pk').first()
    user = User.objects.order_by('-pk').first()
    #科目登録
    post3 = User_Subject(user_id=str(user.id),subject_id=str(subject.id)).save()
    post4 = Subject(name='科目2').save()

    # post3 = Task(
    #   name='name1',subject_id=subject,author=str(user.id),
    #   contents = 'test').save()

  def test_get(self):
    """トップページにアクセスできることを確認"""
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)
  
  def test_get_posts_by_index(self):
    """ログインしてトップページにアクセスできることを確認"""

    self.client.login(user_name=self.username,password="kimatsusikenn")
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)

    # self.assertContains(response, '科目1') # html 内に post1 の name が含まれていることを確認
    # self.assertNotContains(response, '科目2') # html 内に post1 の name が含まれていないことを確認

  def tearDown(self):
    """
    setUp で追加したデータを消す、掃除用メソッド。
    create とはなっているがメソッド名を「tearDown」とすることで setUp と逆の処理を行ってくれる＝消してくれる。
    """
    post1 = Subject.objects.create(name='name1')
    post2 = User(
            username='test001',
            email = 'test@gmail.com',
            password = 'kimatsusikenn',
         ).save()
    subject = Subject.objects.order_by('-pk').reverse().first()
    user = User.objects.order_by('-pk').reverse().first()

    post3 = Task.objects.create(
      name='name1',subject_id=subject,author=str(user.id),
      contents = 'test')
     

class SubjectManageTests(TestCase):

  def test_get(self):
    """科目管理ページ(subject_manage)にアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('subject_manage'))
    self.assertEqual(response.status_code, 200)

class CreateSubjectTests(TestCase):

  def test_get(self):
    """科目作成ページにアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('create_subject'))
    self.assertEqual(response.status_code, 200)


