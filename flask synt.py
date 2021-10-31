from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return("Hello world")

@app.route('/bipins')
def bipin():
    return("Hello Bipin Shah")

app.run()
