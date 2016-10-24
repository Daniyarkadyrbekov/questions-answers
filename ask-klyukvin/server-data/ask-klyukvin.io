upstream backend {
	server ask-klyukvin.io:8000;
}

proxy_cache_path /var/spool/nginx/ levels=1:2 keys_zone=my_cache:10m 
max_size=100m inactive=5m;
proxy_cache_valid 200 1m; 

server {
	server_name ask-klyukvin.io;

	location ^~ /static/ {
		root /home/artem/Documents/PyCharm/ask-klyukvin/;
        gzip on;		
	}

    location "~\.[\w]{2,4}$" {
        root /home/artem/Documents/PyCharm/ask-klyukvin/static/;
        gzip on;
    }

	location /uploads/ {
		root /home/artem/Documents/PyCharm/ask-klyukvin/;
        gzip on;		
	}

	location / {
   #     proxy_cache my_cache;
		proxy_pass http://backend;
	}
}
