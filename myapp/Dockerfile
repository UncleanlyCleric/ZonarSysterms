FROM python:3.7.5

COPY . /lang_api

WORKDIR /lang_api

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
