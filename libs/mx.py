from dns.resolver import Resolver


def getrecords(email):
    try:
        domain = email.split('@')[1]
        resolve = Resolver()
        records = resolve.query(domain, 'MX')
        mx = records[0].exchange
        mx = str(mx)
        return mx
    except Exception as e:
        print '[!] DNS Resolution Issue: {0}'.format(str(e))
        return 0
