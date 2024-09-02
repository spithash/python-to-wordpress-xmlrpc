from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.posts import GetPosts
import configparser
import collections

# This fixes AttributeError: module 'collections' has no attribute 'Iterable'
collections.Iterable = collections.abc.Iterable

cfg = configparser.ConfigParser(inline_comment_prefixes=('#', ';'))
cfg.read('configuration.ini')

wp_url = cfg.get('Credentials', 'WP_URL')
wp_username = cfg.get('Credentials', 'WP_USERNAME')
wp_password = cfg.get('Credentials', 'WP_PASSWORD')

wp = Client(wp_url, wp_username, wp_password)

# Get all shop orders
shop_orders = wp.call(GetPosts({'post_type': 'shop_order', 'post_status': 'any', 'number': 30}))

# Print all orders retrieved
print(f"Total orders retrieved: {len(shop_orders)}")
for post in shop_orders:
    print(f"OrderID: {post.id}, Status: {post.post_status}, Date: {post.date}, Terms: {post.terms}")

# Filter for completed orders
completed_orders = [post for post in shop_orders if post.post_status == 'wc-completed' ]
print("Completed Orders:")

for post in completed_orders:
    print(f"OrderID: {post.id}, Status: {post.post_status}, Date: {post.date}, Terms: {post.terms}")
