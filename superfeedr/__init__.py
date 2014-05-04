import requests


class Superfeedr:

    def __init__(self, username, password, verify='sync',
                    superfeedr_endpoint='https://push.superfeedr.com'):
        self.username = username
        self.password = password
        self.verify = verify
        self.superfeedr_endpoint = superfeedr_endpoint

    def post_to_superfeedr(self, mode, topic, callback, json=False):
        superfeedr_data = {
            'hub.mode': mode,
            'hub.topic': topic,
            'hub.callback': callback,
            'hub.verify': self.verify,
        }
        if json:
            #Accept: application/json
            return requests.post(self.superfeedr_endpoint, auth=(self.username, self.password),
                                 data=superfeedr_data, headers={'Accept': 'application/json'})
        else:
            return requests.post(self.superfeedr_endpoint, auth=(self.username, self.password),
                                 data=superfeedr_data)

    def get_feed_status(self, url, callback):
        superfeedr_data = {
            'hub.mode': 'status',
            'hub.topic': url,
            'hub.callback': callback
        }
        return requests.get(self.superfeedr_endpoint, auth=(self.username, self.password),
                            data=superfeedr_data)

    def retrieve_feed(self, url):
        #retrieve burns a credit
        superfeedr_data = {
            'hub.mode': 'retrieve',
            'hub.topic': url
        }
        return requests.get(self.superfeedr_endpoint, auth=(self.username, self.password),
                            data=superfeedr_data)

    def add_feed(self, url, callback, json=True):
        return self.post_to_superfeedr('subscribe', url, callback, json=json)

    def remove_feed(self, url, callback):
        return self.post_to_superfeedr('unsubscribe', url, callback)
