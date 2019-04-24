#!/bin/sh
# lxss的安装脚本，需要配置django的secret_key，登陆密码，部署的 url:port，更改 data 目录的读写权限
# 把 backend/static/login 复制到 frontend/static/ 中，因为如果用 nginx 反代理静态文件只能选择一个目录

echo "[!] Welcome to Lnyas's XSS platform ..."
echo "[!] If you want to know more about install, please see READNE.md ..."
echo "[!] start install ..."
echo "[!] chmod and copy static file ..."
mkdir backend/data/
chmod -R 755 backend/data/
chmod -R 755 frontend/dist/static

cp -r backend/static/login frontend/dist/static/
cp -r backend/static/cheatsheet frontend/dist/static/
cp -r backend/static/templates frontend/dist/static/
echo "[!] generate django secret-key..."
secretkey=`cat /proc/sys/kernel/random/uuid`
echo ${secretkey}
echo "[+] Please input your password:"
read passwd
md5passwd=`echo -n ${passwd}|md5sum|cut -d ' ' -f1`
echo ${md5passwd}
echo "[+] Please input your host (just like 'xss.example.com'):"
read host
echo ${host}


sed -e "s/DEBUG = False/DEBUG = True/g;/^MD5_PASSWD.*/s//MD5_PASSWD = '${md5passwd}'/g;/^BASE_URI.*/s//BASE_URI = '${host}'/g;/^SECRET_KEY.*/s//SECRET_KEY = '${secretkey}'/g" lxss/settings.py > settings.py
cp settings.py lxss/settings.py
rm settings.py

echo "[!] install done, use start.sh or \`python3 manage.py runserver\` to start it"
