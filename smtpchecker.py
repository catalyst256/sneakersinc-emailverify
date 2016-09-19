#!/usr/bin/env python

from libs.mx import getrecords
from libs.tor import usetor
from libs.email import checkemail, findcatchall
from flask_api import FlaskAPI
import ConfigParser
import validators
from flask import request

conf = ConfigParser.ConfigParser()
conf.read("settings.conf")
tor = int(conf.get('tor', 'enabled'))


def verifyemail(email):
    mx = getrecords(email)
    if mx != 0:
        fake = findcatchall(email, mx)
        if fake > 0:
            fake = 'Yes'
        else:
            fake = 'No'
        if tor == 1:
            results = usetor(email, mx)
        else:
            results = checkemail(email, mx)
        if results[0] == 666:
            return {'email': email, 'error': results[1], 'mx': mx, 'status': 'Error'}
        if results[0] == 250:
            status = 'Good'
        else:
            status = 'Bad'

        data = {'email': email, 'mx': mx, 'code': results[0], 'message': results[1], 'status': status,
                'catch_all': fake, 'tor_enabled': results[2]}
        return data
    else:
        return {'error': 'Error checking email address'}


app = FlaskAPI(__name__)


@app.route('/verify/', methods=['GET'])
def search():
    addr = request.args.get('email')
    if not validators.email(addr):
        return {'Error': 'Invalid email address'}
    data = verifyemail(addr)
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
