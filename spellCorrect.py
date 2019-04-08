from flask import Flask
from pattern.en import suggest
from flask import jsonify
import json
from flask import request

app = Flask(__name__)

@app.route('/spellCorrect', methods=['GET', 'POST']) #allow both GET and POST requests
def spell():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        word = request.form.get('word')
        
        return jsonify({'data':json.dumps(suggest(word))})

    return '''<form method="POST">
                  Word: <input type="text" name="word"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    app.run(debug=True)