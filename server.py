#!/usr/bin/env python

from libs.email import verifyemail
from flask import Flask
from flask_restx import Api, Resource, reqparse
import validators


app = Flask(__name__)
api = Api(app)

# Define a namespace
ns = api.namespace('api/v1', description='Email verification services')

# Setup the request parser
parser = reqparse.RequestParser()
parser.add_argument('q', type=str, required=True, help='The email address to verify', location='args')

@ns.route('/verify')  # Updated to use Flask-RESTx namespace
class VerifyEmail(Resource):
    @ns.expect(parser)  # Expecting arguments as defined in parser
    def get(self):
        # Use the parser to parse the arguments
        args = parser.parse_args()
        addr = args['q']
        
        if not validators.email(addr):
            return {'Error': 'Invalid email address'}, 400
        
        data = verifyemail(addr)
        return data, 200

if __name__ == '__main__':
    app.run(debug=True)
