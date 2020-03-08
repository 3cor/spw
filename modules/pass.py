import secrets
import string

def generate(n=8):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(n))
    return password


def generate_harder(n=8, digit=3):
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(n))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= digit):
            break
    return password

def generate_xkcd(filepath_or_buffer, n=8):
    """Generate an XKCD-style passphrase https://xkcd.com/936/"""
    # On standard Linux systems, use a convenient dictionary file.
    # Other platforms may need to provide their own word-list.
    with open(filepath_or_buffer) as f:
        words = [word.strip() for word in f]
        password = ' '.join(secrets.choice(words) for i in range(4))
    return password

if __name__ == '__main__':
    # TODO Make this a command line program
    import sys
    generate(int(sys.argv[1]))
