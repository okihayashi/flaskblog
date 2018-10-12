from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Oki Hayashi',
        'title': 'Blog Post1',
        'content': 'First post',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Oki Hayashi',
        'title': 'Blog Post2',
        'content': 'Second post',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
        return render_template('home.html', posts = posts) 

@app.route("/about")
def about():
        return render_template('about.html', title='About') 

if __name__ == '__main__':
    app.run(debug=True)
