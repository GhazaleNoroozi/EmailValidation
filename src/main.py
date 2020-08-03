import re
import smtplib
import dns.resolver
import socket


def regex_validation(email):
    """Match the email with a regex and return a boolean."""
    return bool(re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email))


def smtp_ping(mx_host, email):
    """Initiate a SMTP conversation with the host to see if the email is valid

    :param mx_host: the mail server
    :type mx_host: basestring
    :param email: the email
    :type email: basestring
    :return: a bool indicating whether the email is valid
    """
    print("host", mx_host)
    # Connect to the mx host
    server = smtplib.SMTP()
    server.set_debuglevel(0)
    server.connect(mx_host)

    # Identify sender server and email address
    host = socket.gethostname()
    server.helo(host)
    server.mail('email@domain.com')

    # Identify the recipient email address
    code, message = server.rcpt(email)
    print(message, code)
    server.quit()

    # Check if the email address was valid
    if code == 250:
        return True
    else:
        return False


def smtp_validation(email):
    """Validate the email address

    :param email: the email address
    :type email: string
    :return: a bool indicating whether the email is valid
    """
    # Extract domain
    domain = email.split('@')[-1]
    is_valid = False

    # Find the prior mail server
    try:
        mx_report = dns.resolver.resolve(domain, 'MX')
    except dns.exception.DNSException:
        return False

    records = []
    for rec in mx_report:
        records.append(rec)

    records.sort(key=lambda r: r.preference, reverse=False)
    for rec in records:
        try:
            is_valid = smtp_ping(str(rec.exchange)[:-1], email)
            break
        except TimeoutError:
            print("Connection time out. Check port 25. It might be blocked.")
            exit(-1)
        except Exception as e:
            # print("Exception: ", e)
            continue

    return is_valid


def main():
    """Main method"""
    email = input()
    if regex_validation(email) and smtp_validation(email):
        print("Email was valid")
    else:
        print("Email was not valid")


if __name__ == '__main__':
    main()
