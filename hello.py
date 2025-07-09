from flask import Flask # type: ignore
app=Flask(__name__)
@app.route('/')
def hello():
    return ("Hello world welcome to this")
if __name__=="__main__":
    app.run(debug=True)