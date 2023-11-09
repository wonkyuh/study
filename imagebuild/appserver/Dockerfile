FROM	tomcat:latest
LABEL	description="WK TOMCAT IMAGE"
RUN	apt-get update \
	&& apt-get install -y git vim net-tools iputils-ping procps
COPY	index.jsp ${CATALINA_HOME}/webapps/ROOT/
COPY	mariadb-java-client-1.8.0.jar ${CATALINA_HOME}/bin
COPY	catalina.sh ${CATALINA_HOME}/bin
RUN	${CATALINA_HOME}/bin/startup.sh