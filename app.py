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
app.config['MAIL_USERNAME'] = 'sif.getintouch@gmail.com'
app.config['MAIL_PASSWORD'] = 'quib hqxx gspa pvel'
app.config['MAIL_DEFAULT_SENDER'] = 'sif.getintouch@gmail.com'

mail = Mail(app)

@app.route('/contact-us', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        organisation = request.form.get('org')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message_content = request.form.get('message')

        msg = Message(
            subject=f'Message from SIF Contact Form: {subject}',
            recipients=['SIF.ICBS.official@outlook.com'])
        msg.html = f"""
<p>New message from <strong>{first_name} {last_name}</strong></p>

<p><strong>Organisation:</strong> {organisation}<br>
<strong>Email:</strong> {email}</p>

<p>{message_content}</p>

<p style="font-size: 8px; color: gray;">
  sif.getintouch@gmail.com email recovery information:<br><br
  Recovery emails of SIF.ICBS.official@outlook.com <br>
  and Sofia Hueffer (2025) email and phone number (smhueffer@gmail.com)<br><br>

  10 backup codes:<br>
  SAVE YOUR BACKUP CODES<br>
  Keep these backup codes somewhere safe but accessible.

    1. 2233 9077         6. 4310 8937
    2. 7584 4556         7. 4694 6238
    3. 3495 0154         8. 7526 2673
    4. 3682 0656         9. 6313 9293
    5. 7312 8776        10. 9575 6267

    (sif.getintouch@gmail.com)

    * You can only use each backup code once.
    * Need more? Visit https://g.co/2sv
    * These codes were generated on: May 31, 2025.
</p>
"""
        try:
            mail.send(msg)
            flash('Message sent! Thanks for reaching out.', 'success')
        except Exception as e:
            flash(f'Could not send message: {str(e)}', 'danger')

        return redirect(request.referrer or url_for('index'))

    return render_template('contact.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
