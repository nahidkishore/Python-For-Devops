from flask import Flask

#creating a flask app instance
app=Flask(__name__)

@app.route("/")

def hello():
  return "hello world!!"


app.run("0.0.0.0")