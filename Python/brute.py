import flask
from operator import eq
app = flask.Flask(__name__)

main_pass = 'fiveguys'

@app.route('/', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        #username = flask.request.args.get('username')
        password = flask.request.args.get('password')
        print(password)
        if str(main_pass) == str(password):
            return flask.Response('You in boi', 200)
        else:
            return flask.Response('Nice try', 403)
        

    else:
        return flask.Response('Eyy', 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
