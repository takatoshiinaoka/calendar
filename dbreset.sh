cd calendarProject
rm -d -r migrations/
cd ..
rm -d -r db.sqlite3
python manage.py makemigrations calendarProject
python manage.py migrate
python manage.py createsuperuser

# bash dbreset.sh で実行