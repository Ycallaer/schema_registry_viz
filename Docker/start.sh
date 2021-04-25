#! /usr/bin/env sh
set -x

if [ -f /schema_reg_viz/schema_reg_viz/main.py ]; then
    DEFAULT_MODULE_NAME=schema_reg_viz.main
elif [ -f /schema_reg_viz/main.py ]; then
    DEFAULT_MODULE_NAME=main
fi
MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

if [ -f /schema_reg_viz/gunicorn_conf.py ]; then
    DEFAULT_GUNICORN_CONF=/schema_reg_viz/gunicorn_conf.py
elif [ -f /schema_reg_viz/app/gunicorn_conf.py ]; then
    DEFAULT_GUNICORN_CONF=/schema_reg_viz/app/gunicorn_conf.py
else
    DEFAULT_GUNICORN_CONF=/gunicorn_conf.py
fi
export GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}

# Start Gunicorn
exec gunicorn -k uvicorn.workers.UvicornWorker -c "$GUNICORN_CONF" "$APP_MODULE"