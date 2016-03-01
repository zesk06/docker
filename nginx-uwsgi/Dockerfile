FROM nginx

RUN apt-get update
RUN apt-get install -y  uwsgi uwsgi-plugin-python \
                        python-bottle \
                        python-pip

RUN apt-get install -y vim
RUN apt-get install -y supervisor


run echo "daemon off;" >> /etc/nginx/nginx.conf
ADD nginx_default.conf  /etc/nginx/conf.d/default.conf
ADD supervisor-app.conf /etc/supervisor/conf.d/supervisor-app.conf

# Bottle application handling
ADD bottle /var/www/bottle
# run pip install
run pip install -r /var/www/bottle/requirements.txt

expose 80
cmd ["supervisord", "-n"]
