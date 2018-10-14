import io
import json

from flask import Flask
from flask import request
from contextlib import redirect_stdout

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run():
	# print(request.form['code']) 
	g = {}
	l = {}
	p = io.StringIO()
	try:
		with redirect_stdout(p):
			exec(request.form['code'], g, l)
		# print(str(l))
		return_val = {'locals': l, 'print': p.getvalue()}
		return json.dumps(return_val)
	except Exception as e:
		import traceback
		error = traceback.format_exc()
		print(error.upper())
		return str(error.upper())
