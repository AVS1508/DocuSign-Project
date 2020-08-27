from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/volunteer/')
def volunteer():
    print ('Activated Volunteer Form')
    return render_template('volunteer.html')

@app.route('/donate/')
def donate():
    print ('Activated Donation Form')
    return render_template('donation.html')

if __name__ == '__main__':
  app.run(debug=True)