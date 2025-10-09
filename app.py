from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route ('/portfolio')
def portfolio ():
    return render_template ('portfolio/index.html')

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaofcircle', methods=['GET', 'POST'])
def areaofcircle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            result = math.pi * radius * radius
            result = round(result, 2)  # Round to 2 decimal places
        except ValueError:
            result = "Please enter a valid number"
    return render_template('areaofacircle.html', result=result)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def areaoftriangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            result = 0.5 * base * height
            result = round(result, 2)  # Round to 2 decimal places
        except ValueError:
            result = "Please enter valid numbers"
    return render_template('areaoftriangle.html', result=result)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')
        
        # Here you can process the form data
        # For now, we'll just print it (you can add email sending later)
        print(f"Contact form submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        
        # For now, redirect back to main page with a success message
        # You can add flash messages later for better user feedback
        return f"<h2>Thank you {name}!</h2><p>Your message has been received. I'll get back to you at {email}</p><a href='/'>← Back to Home</a>"
    return "Invalid request method.", 400

if __name__ == "__main__":
    app.run(debug=True)
