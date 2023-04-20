from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Email Open Contact List'

if __name__ == '__main__':
    app.run(debug=True)






from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # Save name and email to a database or file
    return 'Thank you for submitting your information!'

if __name__ == '__main__':
    app.run(debug=True)


import sqlite3

conn = sqlite3.connect('email_contacts.db')
c = conn.cursor()

c.execute('''CREATE TABLE contacts
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

conn.commit()
conn.close()


import sqlite3

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    conn = sqlite3.connect('email_contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    return 'Thank you for submitting your information!'



