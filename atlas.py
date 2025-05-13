import requests
from requests.auth import HTTPDigestAuth

class Atlas:
    def __init__(self, public_key, private_key):
        self.cookieJar = requests.cookies.RequestsCookieJar()
        self.session = requests.Session()
        self.headers = {
            'Content-type': 'application/json', 
            'Accept': 'application/vnd.atlas.2024-08-05+json' 
        }
        self.base = 'https://cloud.mongodb.com/api/atlas/v2'
        self.auth = HTTPDigestAuth(public_key, private_key)
    
    def call(self, method, path, json={}, params={}):
        url = f'{self.base}{path}'
        if method == 'GET':
            return self.session.get(url, auth=self.auth, params=params ,headers=self.headers, cookies=self.cookieJar)
        elif method == 'POST':
            return self.session.post(url, auth=self.auth, params=params, json=json, headers=self.headers, cookies=self.cookieJar)
        elif method == 'PATCH':
            return self.session.patch(url, auth=self.auth, params=params, json=json, headers=self.headers, cookies=self.cookieJar)
        elif method == 'PUT':
            return self.session.put(url, auth=self.auth, params=params, json=json, headers=self.headers, cookies=self.cookieJar)
        elif method == 'DELETE':
            return self.session.delete(url, auth=self.auth, params=params, json=json, headers=self.headers, cookies=self.cookieJar)
        else:
            return 'Error: The specified method is invalid!'

def main():
    pass

if __name__ == '__main__':
    main()