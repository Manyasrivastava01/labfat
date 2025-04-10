from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to my Python Web Application!</h1>"

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        # Get the user's name from the form
        name = request.form.get('name', 'Guest')
        return f"<h1>Hello, {name}!</h1>"
    return '''
        <form method="POST" action="/greet">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
