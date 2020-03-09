import secrets
import string

def simple(n):
    """Generate a simple password from alphanumeric characters"""
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(n))
    return password


def secure(n, digit):
    """Generate a password with lowercase character,
    uppercase character, digit requirements"""
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(n))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= digit):
            break
    return password

def passphrase(n, filepath):
    """Generate an XKCD-style passphrase https://xkcd.com/936/"""
    with open(filepath) as f:
        words = [word.strip() for word in f]
        password = ' '.join(secrets.choice(words) for i in range(n))
    return password

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Commands available: simple, secure, and passphrase")
    parser.add_argument("-n", "--number", help="Number of characters", type=int, default=8)
    parser.add_argument("-d", "--digit", help="Digits", type=int, default=3)
    parser.add_argument("-f", "--filepath", help="File path or buffer", default='data/words.txt')
    args = parser.parse_args()
    command = args.command
    n = args.number
    digit = args.digit
    filepath = args.filepath

    if command == 'simple':
        output = simple(n)
    elif command == 'secure':
        output = secure(n, digit)
    elif command == 'passphrase':
        output = passphrase(n, filepath)
    else:
        raise ValueError('Wrong command!')

    print(output)
