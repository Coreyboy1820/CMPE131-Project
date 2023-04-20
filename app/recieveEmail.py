from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'your-mail-server.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email')
def send_email():
    # Create a new message object
    msg = Message('Test Email Subject',
                  sender='your-email@example.com',
                  recipients=['recipient-email@example.com'])
    # Set the body of the email
    msg.body = 'Hello, this is a test email from Flask!'
    # Send the email
    mail.send(msg)
    return 'Email sent'

if __name__ == '__main__':
    app.run(debug=True)
