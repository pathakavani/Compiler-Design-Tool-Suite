import flask
from flask import Flask, render_template, request, current_app,session,redirect, url_for, Response
import project_cmd
import subprocess
import os
from flask_caching import Cache


cache = Cache(config={'CACHE_TYPE':'NullCache'})
app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
  return render_template("index.html")


@app.route('/pre',methods=['GET','POST'])
def pre():
  if request.method=="GET":
    return render_template("pre.html")
  if request.method=="POST":
    exp=request.form['exp']
    exp1=exp.replace(" ","")
    try:
      result=project_cmd.infix_to_prefix(exp1)
      return render_template('pre.html', result=result, exp1=exp1)
    except:
      err="Invalid Expression"
      return render_template('pre.html', exp1=exp1, err=err)

@app.route('/pos',methods=['GET','POST'])
def pos():
  if request.method=="GET":
    return render_template("pos.html")
  if request.method=="POST":
    exp=request.form['exp']
    exp1 = exp.replace(" ", "")
    try:
      result=project_cmd.infix_to_postfix(exp1)
      return render_template('pos.html', result=result, exp1=exp1)
    except:
      err="Invalid Expression"
      return render_template('pos.html', exp1=exp1, err=err)

@app.route('/evalpre',methods=['GET','POST'])
def evalpre():
  if request.method=="GET":
    return render_template("evalpre.html")
  if request.method=="POST":
    exp=request.form['exp']
    exp1 = exp.replace(" ", "")
    try:
      result=project_cmd.evaluate_prefix(exp1)
      return render_template('evalpre.html', result=result, exp1=exp1)
    except:
      err="Invalid Expression"
      return render_template('evalpre.html', exp1=exp1, err=err)


@app.route('/evalpost',methods=['GET','POST'])
def evalpost():
  if request.method=="GET":
    return render_template("evalpost.html")
  if request.method=="POST":
    exp=request.form['exp']
    exp1 = exp.replace(" ", "")
    try:
      result=project_cmd.evaluate_postfix(exp1)
      return render_template('evalpost.html', result=result, exp1=exp1)
    except:
      err="Invalid Expression"
      return render_template('evalpost.html', exp1=exp1, err=err)


@app.route('/evalin',methods=['GET','POST'])
def evalin():
  if request.method=="GET":
    return render_template("evalin.html")
  if request.method=="POST":
    exp=request.form['exp']
    exp1 = exp.replace(" ","")
    try:
      result = project_cmd.evaluate_infix(exp1)
      return render_template('evalin.html', result=result, exp1=exp1)
    except:
      err = "Invalid Expression"
      return render_template('evalin.html', exp1=exp1, err=err)

@app.route('/syntax',methods=['GET','POST'])
def syntax():
  if request.method=="GET":
    return render_template("syntax.html")
  if request.method=="POST":
    exp=request.form['exp']
    exp1=exp.replace(" ","")
    staticpath="/home/avani/Documents/LP4/static/images/"
    pnge="ast.png"
    astimage=os.path.join(staticpath,pnge)
    astfile=os.path.join("/home/avani/Documents/LP4/","ast.py")
    result=subprocess.call('rm %s' %(astimage),shell=True)
    result1 = subprocess.call('python %s "%s" > ast.dot && dot -Tpng -o %s ast.dot' % (astfile, exp1, astimage), shell=True)
    if os.path.isfile(astimage):
      return render_template('result1.html', exp1=exp1)
    else:
      err = "Invalid Expression"
      return render_template('syntax.html', err=err)





@app.route('/parse',methods=['GET','POST'])
def parse():
  if request.method=="GET":
    return render_template("parse.html")
  if request.method=="POST":
    exp=request.form['exp']
    exp1=exp.replace(" ","")
    staticpath="/home/avani/Documents/LP4/static/images/"
    pngi="parse_tree.png"
    parseimagefile=os.path.join(staticpath,pngi)
    parsefile=os.path.join("/home/avani/Documents/LP4/","parse_tree.py")
    result = subprocess.call('rm %s' % (parseimagefile), shell=True)
    result1 = subprocess.call('python %s "%s" > parse_tree.dot && dot -Tpng -o %s parse_tree.dot' % (parsefile, exp1, parseimagefile), shell=True)
    if os.path.isfile(parseimagefile):
      return render_template('result2.html', exp1=exp1)
    else:
      err = "Invalid Expression"
      return render_template('parse.html', err=err)


@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

if __name__ == "__main__":
      app.run(debug=True, port=7000)