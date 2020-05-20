FROM python:3.8

#ADD /requirements.txt requirements.txt

COPY vk.py /mock/
COPY requirements.txt /mock/

WORKDIR /mock

RUN pip3.8 install -r /mock/requirements.txt

#ADD /mock mock

CMD ["python3.8", "vk.py"]