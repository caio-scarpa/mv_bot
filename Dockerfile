FROM python:3.10-alpine

WORKDIR /usr/src/app

COPY ./ ./
RUN pip install  -r requirements.txt

EXPOSE 443

CMD [ "python", "./__main__.py" ]