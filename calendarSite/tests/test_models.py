from django.test import TestCase
from calendarSite.models import Subject

class PostModelTests(TestCase):
  def test_is_empty(self):
    """初期状態では何も登録されていないことをチェック"""  
    saved_posts = Subject.objects.all()
    self.assertEqual(saved_posts.count(), 0)