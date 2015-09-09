export C_FORCE_ROOT="true"

cd webapp2
celery -A webapp2.celery worker