import os

from flask import Flask, request, jsonify, render_template, redirect, url_for,send_file
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant
from werkzeug.utils import secure_filename

app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')

# Add your Twilio credentials
@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID = 'ACdf2eed5b4094a2bb1afd2b26ef41b270'
    TWILIO_SYNC_SERVICE_SID = 'IS8ef1224d80810fc67077ed2cf284f5b9'
    TWILIO_API_KEY = 'SKff11b33a6560a78c27c0a8d1e72706d5'
    TWILIO_API_SECRET = 'd1hWJlWhrXIhT6QF6EHXNTQFvkUZqiam'
    fn=fake.user_name()
    print(fn)


    username = request.args.get('username', fake.user_name())

    # create access token with credentials
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    # create a Sync grant and add to token
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt())

# Write the code here
@app.route('/', methods=['POST'])
def download_text():
    text_from_notepad=request.form['text']
    with open("Downloaded_Document.txt","w") as f:
        f.write(text_from_notepad)
    path="Downloaded_Document.txt"
    return send_file(path,as_attachment=True)


    
        

    

    


if __name__ == "__main__":
    app.run(host='localhost', port='5001', debug=True)
