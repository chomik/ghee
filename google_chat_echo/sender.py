
import http.client
import json

from urllib.parse import urlparse


class Sender:
    def __init__(self, webhook_url):
        self.headers = {'Content-type': 'application/json; charset=UTF-8'}
        self.url = urlparse(webhook_url)
        self.connection = http.client.HTTPSConnection(self.url.netloc)
        
    def send(self, message):
        return self._send(message)
    
    def _send(self, message):
        foo = {'text': message}
        json_data = json.dumps(foo)

        self.connection.request('POST', self.url.geturl(), json_data, self.headers)

        response = self.connection.getresponse()
        print(response.read().decode())


if __name__ == '__main__':
    import sys
    _, url, *message = sys.argv

    message = ' '.join(message)

    print(f'Sending: {message}')
    print(f'via: {url}')
    print(Sender(url).send(message))