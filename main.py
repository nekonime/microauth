import time
from flask import Flask, url_for, request
app = Flask(__name__)

auth_username = 'panda'
auth_firstName = 'Andrew'
auth_lastName = 'Pelley'
auth_cryptPwd = '4E9BE86EBDE926770923E7B8C3D07E600FA672CC83AAABBC18D063E8EFAF560BD6935EF4C38D5945390E894CF20DB82E53268F8D7DCB190B625CD4962AA3D47C'

@app.route('/')
def index():
    ts = str(time.time()).split('.')[0]
    return '<!DOCTYPE html><html><img style="margin:5% auto;display:block" src="static/lock.gif?' + ts + '"></html>'

@app.route('/auth', methods=['GET', 'POST'])
def auth_rep():
    post_username = str(request.form.get('username'))
    post_cryptPwd = str(request.form.get('passcode'))
    #return '<!DOCTYPE html><html><h1>w</h1><h2>u</h2><h3>t</h3>' + str(request.values) + '</html>'
    print("User trying to authenticate with username '" + post_username + "' and password hash '" + post_cryptPwd + "'")
    if auth_username.lower() == post_username.lower():
        if auth_cryptPwd.lower() == post_cryptPwd.lower():
            print("User '" + auth_username + "' authenticated successfully.")
            return "{'result': 'success', 'username': '" + auth_username + "', 'full_name': ['" + auth_firstName + "', '" + auth_lastName + "']}"
        else:
            print("Authentication failed. Password mismatch.")
            return "{'result': 'failure', 'reason': 'password_mismatch'}"
    else:
        print("Authentication failed. Username not in database.")
        return "{'result': 'failure', 'reason': 'username_not_found'}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1379)
