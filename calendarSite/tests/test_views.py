from django.test import TestCase
from django.urls import reverse

from ..models import Subject

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
    post1 = Subject.objects.create(name='人工知能応用')
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