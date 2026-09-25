import requests

class APIUtils:

    @staticmethod
    def post_request(url, payload, headers=None):
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )
        return response