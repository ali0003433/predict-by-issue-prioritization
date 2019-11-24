import flask
from flask import request
from predictor_api import make_prediction
from flask import jsonify

# initialize app 
app = flask.Flask(__name__)

@app.route("/", methods=["POST"])
def print_piped():
    if request.form['mes']:
        msg = request.form['mes']
        print(msg)
        x_input, predictions = make_prediction(str(msg))
        flask.render_template('index.html',
                                chat_in=x_input,
                                prediction=predictions)
    return jsonify(predictions)

@app.route('/', methods=['GET'])
def predict():
    print(request.args)
    if (request.args):
        x_input, predictions = make_prediction(request.args['chat_in'])
        print(x_input)
        return flask.render_template('index.html',
                                     chat_in=x_input,
                                     prediction=predictions)
    else:
        x_input, predictions = make_prediction('')
        return flask.render_template('index.html', 
                                     chat_in=x_input, 
                                     prediction=predictions)

# start the server, listen for requests 
if __name__ == '__main__':
    app.run(debug=True)
    app.run()
