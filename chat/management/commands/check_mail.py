#check_mail.py
from django.core.management.base import BaseCommand, CommandError

# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = 'Check if you can send an email'

    def handle(self, *args, **options):
        print("Hello world")