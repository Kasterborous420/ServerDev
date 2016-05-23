# project/server/main/views.py


#################
#### imports ####
#################

from flask import Flask, url_for
app = Flask(__name__)


################
#### config ####
################




################
#### routes ####
################


##@app.route('/', methods = ['GET', 'POST'])
##def login():
##    if request.method == 'POST' :

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run()

@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")
