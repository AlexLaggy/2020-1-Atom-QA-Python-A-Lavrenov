FROM python:3.8

#ADD /requirements.txt requirements.txt

#COPY vk.py /mock/
#COPY requirements.txt /mock/


RUN pip3.8 install -r /var/jenkins_home/src/Final_Project/mock/requirements.txt

#ADD /mock mock

CMD ["python3.8", "/var/jenkins_home/src/Final_Project/mock/vk.py"]