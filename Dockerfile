FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_INDEX 1

ENV FLASK_APP="main.py"
ENV SECRET="boca campeon 2018"
ENV DEBUG=false
ENV DATABASE_URL="mysql+pymysql://root:r8LtFleayvk6ghwO@35.237.244.192:3306/contento"

COPY ./app /app