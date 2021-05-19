FROM python:latest
LABEL "maintainer"="William Villani Stiehler"

COPY . /var/www
WORKDIR /var/www
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

ENV PORT=5000
EXPOSE $PORT

ENTRYPOINT ython main.py --host=0.0.0.0 --port=$PORT --reload 

# p
#python main.py migrate && python app.py  run --host=0.0.0.0 --port=$PORT --reload 