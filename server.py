from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 'BB'

@app.route('/')
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1,100)
    print(session['random_num'])
    return render_template('index.html')

@app.route('/wrong', methods=['POST'])
def wrong():
    session['guess'] = int(request.form['guess'])
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')





    # if userinput > random_num:
    #     <h1> "the number is lower"
    # elif userinput < random_num:
    #     <h1> "the number is higher"
    # else:
    #     <h1> "You got it right"


if __name__ == '__main__':
    app.run(debug=True)