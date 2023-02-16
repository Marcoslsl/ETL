FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=1234

WORKDIR /src 

COPY docker/db/db.sql /docker-entrypoint-initdb.d/
