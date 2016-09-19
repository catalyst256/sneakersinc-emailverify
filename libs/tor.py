import socks
import smtplib
import ConfigParser

conf = ConfigParser.ConfigParser()
conf.read("settings.conf")


def usetor(email, mx):
    try:
        proxy_host = conf.get('tor', 'socks').split(':')[0]
        proxy_port = conf.get('tor', 'socks').split(':')[1]
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy_host, int(proxy_port))
        socks.wrapmodule(smtplib)
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(mx)
        server.helo('Alice')
        server.mail('me@domain.com')
        code, message = server.rcpt(str(email))
        server.quit()
        return code, message, 1
    except Exception as e:
        print '[!] Error connecting to SMTP via Tor: {0}'.format(str(e))
        return 666, str(e)
