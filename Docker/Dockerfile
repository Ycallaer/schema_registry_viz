FROM python:3.7-alpine3.8
LABEL maintainer="YYC"

ENV SR_VIZ_ENV="local" \
CERT_FILE_PATH=""

RUN apk --no-cache --update-cache add gcc gfortran build-base wget freetype-dev libpng-dev openblas-dev musl-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./Docker/start.sh /start.sh
COPY ./Docker/gunicorn_conf.py /gunicorn_conf.py
COPY ./schema_reg_viz /schema_reg_viz/schema_reg_viz
COPY ./static /schema_reg_viz/static
COPY ./templates /schema_reg_viz/templates
RUN chmod +x /start.sh

WORKDIR /schema_reg_viz/

ENV PYTHONPATH=/schema_reg_viz

EXPOSE 80

CMD ["/start.sh"]