from flask import Flask, redirect, url_for, render_template

app = Flask(__name__,template_folder='template')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')


if __name__ == "__main__":
    app.debug = True
    app.run()

