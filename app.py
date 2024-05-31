from basic_morse import Decoder
from basic_morse import Encoder
# print(Decoder.def_Decode("--- --- --. .-   -... --- --- --. .-"))
# print(Encoder.def_Encode("Ooga booga"))

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    user_inp = request.form['EncInp']
    return Encoder.def_Encode(user_inp)

if __name__ == '__main__':
    app.run(debug=True)