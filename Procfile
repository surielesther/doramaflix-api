web: python manage.py collectstatic --no-input \
    && python manage.py migrate \
    && gunicorn doramaflix.wsgi --log-level debug