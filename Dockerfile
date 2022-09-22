#
FROM python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# COPY ./typesense_orm.tar.gz /typesense_orm.tar.gz

#
# RUN pip install --no-cache-dir /typesense_orm.tar.gz

#
COPY ./app /code/app

#
EXPOSE 80/tcp
CMD ["sleep", "20", "&", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
