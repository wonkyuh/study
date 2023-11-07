FROM	nginx:latest
LABEL	description="WEB Dockerfile"
RUN	apt-get update \
	&& apt-get install -y vim net-tools iputils-ping procps
COPY	default.conf /etc/nginx/conf.d
