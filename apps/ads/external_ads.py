import requests
from requests.exceptions import ConnectionError


class ExternalAd:
    URL = 'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast'

    @classmethod
    def get(cls) -> bytes:
        # TODO
        #  * Handle all possible exceptions and implement a re-try model for Timeout
        #  requests
        #  * Handle all the "bad" responses and return a readable Response
        #  (400+,500+,etc)
        #  * Handle Big responses (e.g. use incremental approach)

        try:
            response = requests.get(cls.URL)
        except ConnectionError:
            return b''

        if response.status_code == 200:
            return response.content

        return b''
