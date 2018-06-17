sed -e "s/DEBUG = True/DEBUG = False/g" lxss/settings.py > settings.py
cp settings.py lxss/settings.py
rm settings.py
nohup python3 -u manage.py runserver 2>&1 &