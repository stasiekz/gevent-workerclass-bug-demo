### Installing dependencies

`pip install -r requirements.txt`

### Running

``gunicorn -w 4 --worker-class=gevent -b 127.0.0.1:8000 --log-level error 'app:app'``

Run `python client.py` 