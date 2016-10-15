upstream backend {
	server ask-klyukvin.io:8000;
}

server {
	server_name ask-klyukvin.io;

	location /static/ {
		root /home/artem/PycharmProjects/ask-klyukvin/;		
	}

	location /uploads/ {
		root /home/artem/PycharmProjects/ask-klyukvin/;		
	}

	location / {
		proxy_pass http://backend;
	}
}
