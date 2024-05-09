from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Tata Divine',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 9, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 9, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


# if I don't want to use environment variables I can add this line
if __name__ == '__main__':
    app.run(debug=True)