import re
import smtplib
import dns.resolver
import socket


def regex_validation(email):
    return re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)


def smtp_validation(email):
    # Extract domain
    domain = email.split('@')[-1]

    # Find the prior mail server
    answer = dns.resolver.resolve(domain, 'MX')
    records = []
    for rec in answer:
        records.append(rec)
    records.sort(key=lambda r: r.preference, reverse=False)
    mx_report = str(records[0].exchange)[:-1]

    print(mx_report)
    # Connect to the mx host
    server = smtplib.SMTP(port=25)
    server.set_debuglevel(0)
    server.connect(mx_report)

    # Identify sender server and email address
    host = socket.gethostname()
    server.helo(host)
    server.mail('ghazalnoroozi27@gmail.com')

    # Identify the recipient email address
    code, message = server.rcpt(email)
    print(message, code)
    server.quit()

    # Check if the email address was valid
    if code == 250:
        return True
    else:
        return False


if __name__ == '__main__':
    email = input()
    if regex_validation(email) and smtp_validation(email):
        print("Email was valid")
    else:
        print("Email was not valid")
