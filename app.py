from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compose', methods=['GET', 'POST'])
def compose():
    if request.method == 'POST':
        sender_email = request.form.get('sender_email')
        recipient_email = request.form.get('recipient_email')
        message = request.form.get('message')
        deliver_at = request.form.get('deliver_at')

        if not all([sender_email, recipient_email, message, deliver_at]):
            flash('All fields are required.')
            return redirect(url_for('compose'))

        # Salvataggio nel database — prossimo step
        flash('Your message has been sealed.')
        return redirect(url_for('confirmed'))

    return render_template('compose.html')

@app.route('/confirmed')
def confirmed():
    return render_template('confirmed.html')

if __name__ == '__main__':
    app.run(debug=True)
