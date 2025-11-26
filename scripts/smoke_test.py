"""
Smoke test for the Flask app using only stdlib (no external requests).
Sends: GET / and POST /predict with a sample payload.
"""
import urllib.request
import urllib.error
import json
import sys

BASE = 'http://127.0.0.1:5000'

def do_get(path='/'):
    url = BASE + path
    print(f'GET {url}')
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            body = resp.read().decode('utf-8')
            print('Status:', resp.status)
            print('Body (truncated):', body[:400])
    except urllib.error.HTTPError as e:
        print('HTTPError:', e.code, e.reason)
        print(e.read().decode('utf-8'))
    except Exception as e:
        print('GET error:', e)


def do_post(path='/predict', payload=None):
    url = BASE + path
    if payload is None:
        payload = {"stiffness": 60, "density": 20, "material": "PLA"}
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    print(f'POST {url} with payload: {payload}')
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            body = resp.read().decode('utf-8')
            print('Status:', resp.status)
            print('Body:', body)
    except urllib.error.HTTPError as e:
        print('HTTPError:', e.code, e.reason)
        print(e.read().decode('utf-8'))
    except Exception as e:
        print('POST error:', e)


if __name__ == '__main__':
    do_get('/')
    print('\n---\n')
    do_post('/predict')
    sys.exit(0)
