from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
  html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a puppy.  Awww...
        </p>
        <img src="http://loremflickr.com/320/240/dog">
    """
  return html.format(name.title())
    #return "Hello {}!".format(name.title())
 
@app.route("/jedi/<firstname>/<lastname>")
def jedi_name(firstname, lastname):
  jedi = lastname[:3] + firstname[:2]
  
  
  return "Your Jedi name is {}!".format(jedi.title())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)