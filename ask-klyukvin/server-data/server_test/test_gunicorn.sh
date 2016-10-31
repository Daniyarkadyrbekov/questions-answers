# GUNICORN_ADDR="ask-klyukvin.io:8000"
# CALL_ADDR= "ask-klyukvin.io/tag_question/"

# cd ../../

# gunicorn -b $GUNICORN_ADDR wsgi.py

# echo "Started gunicorn"

ab -n 5000 -c 100 http://ask:8000/new/


