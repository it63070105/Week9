import os
from flask import Flask, render_template

app = Flask(__name__,template_folder="")


@app.route('/')
def home():
   
   env_var_image = os.environ['APP_IMAGE']
   
   return render_template("index.html", image="building.jpg")
    

@app.route('/<string:name>')
def template(name):
    return render_template("index.html", image=name)
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8081")

