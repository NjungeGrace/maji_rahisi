#import necessary libraries
from flask import Flask, request, Response

#instantiating flask
app = Flask(__name__)

#setting up the routes
@app.route("/ussd", methods = ["POST"])

#defining the necessary functions
def maji_main():
    response = "CON MAJI INFO\nService under setup."
    return Response(response, mimetype="text/plain")

#run the flask app
if __name__ == "__main__":
    app.run(port = 5000)
