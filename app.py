from flask import Flask, render_template
from projects import projects

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True, port = 3000, host = "localhost")
