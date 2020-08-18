# Libraries
from flask import Flask

# PreguntaBits's web service
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hola mundo'

# Main
if __name__ == '__main__':
	app.run(debug=True, port=4040)