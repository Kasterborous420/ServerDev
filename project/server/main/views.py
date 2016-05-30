# project/server/main/views.py


#################
#### imports ####
#################
import json
from flask import Flask, url_for, render_template, request, urllib
app = Flask(__name__)

dict['Words'] = response.urllib.urlopen("http://randomword.setgetgo.com/get.php")
gamesWon = 0
gamesLost = 0
################
#### config ####
################




################
#### routes ####
################


##@app.route('/', methods = ['GET', 'POST'])
##def login():
##    if request.method == 'POST' :

@app.route('/')
def hello:
    return render_template(index.html)

@app.route('/new_game', methods = ['POST'])
def new_game:
    if request.method == 'POST':

        dict['word_length'] = len(response.urllib.urlopen("http://randomword.setgetgo.com/get.php"))
        return json.dump(dict)

@app.route('/check_letter', methods = ['POST'])
def check_letter:
    global dict
    if request.method == 'POST';
    dict['letter'] = len(dict["Words"])

@app.route('/score', methods = ['GET'])
def getScore:
    print "Games Won" % gamesWon
    print "Games Lost" % gamesLost

@app.route('/score', methods = ['DELETE'])
def delScore:
    gamesWon = 0
    gamesLost = 0
    print "Games Won" % gamesWon
    print "Games Lost" % gamesLost



if __name__ == '__main__':
    app.run()
