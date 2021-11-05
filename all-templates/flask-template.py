from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
import os
from flask_cors import CORS, cross_origin
import flask_monitoringdashboard as dashboard


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
dashboard.bind(app)
CORS(app)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
@cross_origin()
def route1():
    try:
        if request.json is not None:
            #your function here
            return Response("some msg")
        elif request.form is not None:
            #your function here
            return Response("some msg")
        else:
            #your function here
            return Response("some msg")
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def route2():
    #Same as above

#port = int(os.getenv("PORT",5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8003
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
