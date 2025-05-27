from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'Host'

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/leadership-team')
def leadership():
    return render_template('leadership.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/alumni')
def alumni():
    return render_template('alumni.html')

@app.route('/strategies')
def strategies():
    return render_template('strategies.html')

@app.route('/join-us')
def joinus():
    return render_template('joinus.html')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'smhueffer@gmail.com'
app.config['MAIL_PASSWORD'] = 'jibb zxiy upgq pdzv'
app.config['MAIL_DEFAULT_SENDER'] = 'smhueffer@gmail.com'

mail = Mail(app)

@app.route('/contact-us', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        role = request.form.get('role')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        subject = request.form.get('subject')
        message_content = request.form.get('message')

        msg = Message(
            subject=f'Message from SIF Contact Form: {subject}',
            recipients=['smhueffer@gmail.com'])

        msg.body = f"""
New message from {full_name}

Role: {role}
Email: {email}
Phone Number: {phone_number}

{message_content}
        """
        try:
            mail.send(msg)
            flash('Message sent! Thanks for reaching out.', 'success')
        except Exception as e:
            flash(f'Could not send message: {str(e)}', 'danger')

        return redirect(request.referrer or url_for('index'))

    return render_template('contact.html')

@app.route('/favicon.ico')
@app.route('/favicon.png')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
