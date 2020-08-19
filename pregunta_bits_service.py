# Libraries
from flask import Flask, request, Response
from json import loads, dumps
from flask_cors import CORS

# PreguntaBits's web service
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
	return 'PreguntaBits'

@app.route('/games', methods=['GET', 'POST'])
def games():
	if request.method == 'GET':
		levels = dict()
		#Open levels file
		with open('data/levels.txt', 'r') as f:
			#Read all the levels
			for index, level in enumerate(f):
				#Create a list with all the level's names
				levels[index] = loads(level)['name'] #from JSON to PYTHON
		#Send a JSON with the names
		return Response(dumps(levels), status=200, mimetype='application/json') #from PYHTON to JSON

	elif request.method == 'POST':
		#Get response from client
		response = loads(request.data)
		#Get level's name required
		wanted_game = response[next(iter(response))]

		#Check if it exists
		with open('data/levels.txt', 'r') as f:
			for index, level in enumerate(f):
				#if it exists Send the entire level required
				if loads(level)['name'] == wanted_game:
					return Response(level, status=200, mimetype='application/json')
					break
			#else send a error message
			error = {'message':'wanted_game does not exist'}
			return Response(dumps(error), status=404, mimetype='application/json')



# Main
if __name__ == '__main__':
	app.run(debug=True, port=4040)