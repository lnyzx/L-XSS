server {
    listen 80 default_server;
    #listen [::]:80;
    server_name _;
    location ^~ /static {
        alias /var/www/frontend/dist/static;
    }

    location / {
        proxy_pass http://localhost:8000;
        proxy_pass_header       Authorization;
        proxy_pass_header       WWW-Authenticate;
        proxy_set_header Host $host;
        proxy_set_header Cookie $http_cookie;
        proxy_set_header X-Forwarded-For $remote_addr;
    }
}