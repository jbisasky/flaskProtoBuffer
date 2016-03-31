import flask
from flask import Flask
import calendar_pb2
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route('/', methods=['POST'])
def parse_request():
    data = flask.request.data
    print str(data)
    customer = calendar_pb2.Customer()
    customer.ParseFromString(data)
    print(str(customer))
    return str(customer)

@app.route("/user/<username>")
def show_user(username):
    return "Hello " + username

if __name__ == "__main__":
    app.run(debug=True)
