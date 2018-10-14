import requests
import inspect

def request(server, code):
	if not isinstance(code, str):
		code = inspect.getsource(code)
	r = requests.post(server + "/run", data={'code': code})
	return r

# test

server = 'http://127.0.0.1:5000'
code = 'a = 4; b = 5; c = a+b; print(b)'
# print(code)
r = request(server, code)
print(r.text)
