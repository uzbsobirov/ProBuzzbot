import json
import requests


class Api:
    def __init__(self):
        # API URL
        self.api_url = 'https://smmmain.com/api/v2'

        # Your API key
        self.api_key = '6c0537731fd7225165f4dea6ab4196eb'

    # Add order
    def order(self, data):
        post = {'key': self.api_key, 'action': 'add'}
        post.update(data)
        return self._connect(post)

    # Get order status
    def status(self, order_id):
        post = {'key': self.api_key, 'action': 'status', 'order': order_id}
        return self._connect(post)

    # Get orders status
    def multi_status(self, order_ids):
        post = {'key': self.api_key, 'action': 'status', 'orders': ','.join(map(str, order_ids))}
        return self._connect(post)

    # Get services
    def services(self):
        post = {'key': self.api_key, 'action': 'services'}
        return self._connect(post)

    # Refill order
    def refill(self, order_id):
        post = {'key': self.api_key, 'order': order_id}
        return self._connect(post)

    # Refill orders
    def multi_refill(self, order_ids):
        post = {'key': self.api_key, 'orders': ','.join(map(str, order_ids))}
        return self._connect(post)

    # Get refill status
    def refill_status(self, refill_id):
        post = {'key': self.api_key, 'refill': refill_id}
        return self._connect(post)

    # Get refill statuses
    def multi_refill_status(self, refill_ids):
        post = {'key': self.api_key, 'refills': ','.join(map(str, refill_ids))}
        return self._connect(post)

    # Get balance
    def balance(self):
        post = {'key': self.api_key, 'action': 'balance'}
        return self._connect(post)

    def _connect(self, post):
        response = requests.post(self.api_url, data=post)
        result = response.text
        return json.loads(result) if result else None


# Examples

# services = api.services()  # Return all services
#
# balance = api.balance()  # Return user balance
#
# # Add order
#
# order = api.order(
#     {'service': 1, 'link': 'https://t.me/kayzenuz/61', 'quantity': 100, 'runs': 2, 'interval': 5})  # Default
#
# order = api.order(
#     {'service': 1, 'link': 'https://t.me/kayzenuz/61', 'comments': "good pic\ngreat photo\n:)\n;"})  # Custom Comments
#
# order = api.order({'service': 1, 'link': 'https://t.me/kayzenuz/61'})  # Package
#
# order = api.order(
#     {'service': 1, 'link': 'https://t.me/kayzenuz/61', 'quantity': 100, 'runs': 10, 'interval': 60})  # Drip-feed
#
# # Old posts only
# order = api.order({'service': 1, 'username': 'https://t.me/kayzenuz', 'min': 100, 'max': 110, 'posts': 0, 'delay': 30,
#                    'expiry': '11/11/2022'})  # Subscriptions
# print(order)

# Unlimited new posts and 5 old posts
# order = api.order({'service': 1, 'username': 'username', 'min': 100, 'max':
