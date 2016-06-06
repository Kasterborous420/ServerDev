# project/server/main/views.py


#################
#### imports ####
#################
import json
from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import urllib
app = Flask(__name__)


gamesWon = 0
gamesLost = 0
bad_guesses = 0
game_state = ""
return_string  = ""
dict['Words']
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
        global dict
        dict['Words'] = urllib.urlopen("http://randomword.setgetgo.com/get.php").read()
        l['word_length'] = {'word_length': len(dict['Words'])}

        game_state = "ONGOING"

        for i in range (0, l):
            word_state = word_state + "_"


        return json.dump(l)

    @app.route('/check_letter', methods = ['POST'])
    def check_letter:
        global dict
        json_request = json.loads(request.data)
        guessLetter = json_request["guess"]
        length = len(string)
        return_string = ""

        wrong_guess = False
        #set the return string to a bunch of underscores
        #for c in string :
        #    if c == json :
        #        return_string = return_string + text
        #    else :
        #        return_string = return_string + "_"

        # when the request comes in, handle it in a st
        # Loop through the
        if game_state == "ONGOING":
            for i in range(0, length):
                if word_state[i] == '_':
                    if guessLetter == dict['Words'][i]:
                        return_string[i] = guessLetter
                        wrong_guess = False
                    else:
                        return_string[i] = '_'
                        wrong_guess = True
                else:
                    return_string[i] = word_state[i]
            word_state = return_string
            if word_state == dict['Words']:
                game_state = "WIN"

            if wrong_guess = true:
                bad_guesses += 1

            if bad_guesses == 8:
                game_state = "LOSE"

        elif game_state == "LOSE" :
            state['answer'] = dict['words']

state['word_state'] = word_state
    return json.dumps(state)
            # Check if  word_state[i] is '_'
                # Check if at this [i] in the dict['words'][i] == guessLetter
                    # if so, return_string[i] = guessLetter
                #else
                    # return_string[i] = '_'
            #else
                # return_string[i] = word_state[i]

        # word_state = return_string
        #json dumpsthingyamagijhi








@app.route('/score', methods = ['GET', 'DELETE'])
def score:
    if request.method == 'DELETE' :
        gamesWon = 0
        gamesLost = 0
    return_response = {'games_won' : gamesWon, 'games_lost' : gamesLost}
    return json.dumps(return_response)



if __name__ == '__main__':
    app.run()
