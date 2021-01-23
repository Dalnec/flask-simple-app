from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return 'Home Page'
    return render_template('home.html')

@app.route('/about')
def about():
    # return 'Home Page'
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) #para q el servidor ser reinice auto debug=True
