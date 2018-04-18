from flask import Flask,request
app=Flask(__name__)
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='Zé'):
  return "HELLO" + name
@app.route("/")
def index(name='world'):
  name=request.args.get('name')
  return "HELLO" + name
if __name__=='__main__':
  app.run(port=7000,debug=True) 