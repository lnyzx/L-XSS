# L`XSS

功能性XSS平台

参考了蓝莲花的XSS平台和余弦的xssor以及ph师傅的playground

目前只完成了 encode/decode 界面和XSS平台的功能



使用时要更改 settings.py 里的 BASE_URI 为部署的 url和端口(例如部署在www.example.com则填写www.example.com:None，有端口则填端口) ，MD5_PASSWD 为md5加密后的密码，最好关闭 debug 模式



### 界面

#### login

![login](E:\开发\lxss\guide\login.png)

#### encode/decode

![encode](E:\开发\lxss\guide\encode.png)

#### record

![record](E:\开发\lxss\guide\record.png)