from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Ali"
    age = 20
    return render_template('index.html', n=name, a=age)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/data')
def data():
    users = ['Vali', 'Tom', 'Alex', 'Jack']
    return render_template('data.html', users = users)


if __name__ == "__main__":
    app.run(debug=True)
