#!/usr/bin/env python

from libs.mx import getrecords
from libs.email import checkemail, findcatchall
from flask_api import FlaskAPI
import validators
from flask import request


def verifyemail(email):
    mx = getrecords(email)
    if mx != 0:
        fake = findcatchall(email, mx)
        if fake > 0:
            fake = 'Yes'
        else:
            fake = 'No'
        results = checkemail(email, mx)
        if results[0] == 666:
            return {'email': email, 'error': results[1], 'mx': mx, 'status': 'Error'}
        if results[0] == 250:
            status = 'Good'
        else:
            status = 'Bad'

        data = {'email': email, 'mx': mx, 'code': results[0], 'message': results[1], 'status': status,
                'catch_all': fake}
        return data
    else:
        return {'error': 'Error checking email address'}


app = FlaskAPI(__name__)


@app.route('/api/v1/verify/', methods=['GET'])
def search():
    addr = request.args.get('q')
    if not validators.email(addr):
        return {'Error': 'Invalid email address'}
    data = verifyemail(addr)
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
