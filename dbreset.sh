cd calendarProject

rm -d -r migrations
cd ..
rm -d -r db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


# bash dbreset.sh で実行
 