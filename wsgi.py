from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Network test 1"

if __name__ == "__main__":
    application.run()
