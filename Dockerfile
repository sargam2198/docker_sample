FROM ubuntu
LABEL MAINTAINER  yaduka.shivam@gmail.com
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
curl -sSl https://get.docker.com/ | sh
COPY apache2.conf /etc/apache2/
COPY serve-cgi-bin.conf /etc/apache2/conf-available/
COPY ./flask_demo /var/www/cgi-bin/ 
WORKDIR /var/www/cgi-bin/ 
RUN pip install -r requirements.txt
CMD python flask_predict_api.py
CMD ["apache2ctl", "-D", "FOREGROUND"]  
#a2enmod cgi
  




#FROM continuumio/anaconda3:4.4.0
#MAINTAINER UNP, https://unp.education
#COPY ./flask_demo /usr/local/python/
#EXPOSE 5000
#WORKDIR /var/www/cgi-bin/ 
#RUN pip install -r requirements.txt
#CMD python flask_predict_api.py
