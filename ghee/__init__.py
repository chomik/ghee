name = "ghee"
__version__ = '0.0.1-1'


from .ghee import Ghee


def main():
    import sys
    _, url, *message = sys.argv
    message = ' '.join(message)
    print(f'Sending: {message}')
    print(f'Via: {url}')
    echo = Ghee(url)
    print(echo(message))