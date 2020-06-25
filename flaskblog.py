from flask import Flask, render_template
app = Flask(__name__)
title = "Hello Jeremy"
posts = [
    {
        'author': 'Jeremy Stevens',
        'title': 'blog Post 1',
        'content': 'first post content',
        'date_posted': 'April 20th, 2018'
        },
    {
        'author': 'John Paston',
        'title': 'My First Blog',
        'content': 'My Very First Blog',
        'date_posted': 'March 20th, 1996'
        }
    ]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run(debug=True,port=80)
