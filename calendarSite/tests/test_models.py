from django.test import TestCase
from calendarSite.models import Subject

class PostModelTests(TestCase):
  def test_is_empty(self):
    """初期状態では何も登録されていないことをチェック"""  
    saved_posts = Subject.objects.all()
    self.assertEqual(saved_posts.count(), 0)
  def test_is_count_one(self):
      """1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト"""
      post = Subject(name="数学",week="1",period="2")
      post.save()
      saved_posts = Subject.objects.all()
      self.assertEqual(saved_posts.count(), 1)
  def test_saving_and_retrieving_post(self):
    """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
    subject = Subject()
    name = 'test_name_to_retrieve'
    subject.name = name
    subject.save()

    saved_subjects = Subject.objects.all()
    actual_subject = saved_subjects[0]

    self.assertEqual(actual_subject.name, name)
