from flask import Flask, render_template
app = Flask(__name__)
import sys
sys.path.append("C:/Users/user/Documents/GitHub/share_food/templates")


@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug=True)
