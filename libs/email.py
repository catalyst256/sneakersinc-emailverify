import smtplib
from dns.resolver import Resolver


def getrecords(email):
    try:
        domain = email.split('@')[1]
        resolve = Resolver()
        records = resolve.query(domain, 'MX')
        preferred_mx_record = str(records[0].exchange)
        return preferred_mx_record
    except Exception as e:
        print(str(e))
        return 0


def check_email(email, mail_exchange):
    try:
        with smtplib.SMTP(mail_exchange) as server:
            server.set_debuglevel(0)  # Consider setting this via a function parameter or configuration
            server.helo('example.com')  # Use a meaningful HELO domain
            server.mail('sender@example.com')  # Use a valid email address in your domain
            code, message = server.rcpt(str(email))
            return code, message, 0
    except smtplib.SMTPException as e:
        return 666, str(e), 0
    except Exception as e:
        return 666, str(e), 0


def find_catch_all(email, mail_exchange):
    try:
        domain = email.split('@')[1]
        # Construct a clearly invalid email address to test the catch-all policy
        fake_email = f'thisdoesnotexist1234567890@{domain}'
        response_code, _, _ = check_email(fake_email, mail_exchange)

        # SMTP response 250 indicates the server accepted the email, suggesting a catch-all policy
        return 1 if response_code == 250 else 0
    except Exception as e:
        return 0



def verifyemail(email):
    mx = getrecords(email)
    if mx == 0:
        return {'error': 'Error checking email address'}
    
    fake = 'Yes' if find_catch_all(email, mx) > 0 else 'No'
    results = check_email(email, mx)
    
    if results[0] == 666:
        return {'email': email, 'error': results[1], 'mx': mx, 'status': 'Error'}
    
    status = 'Good' if results[0] == 250 else 'Bad'
    
    return {
        'email': email,
        'mx': mx,
        'code': results[0],
        'message': results[1].decode('utf-8'),
        'status': status,
        'catch_all': fake
    }