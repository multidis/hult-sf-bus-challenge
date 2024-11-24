## Verifying the validity of Reddit API credentials.
import praw
import config_reddit

reddit = praw.Reddit(user_agent    = f"Content exploration by {config_reddit.app_name}",
                     client_id     = config_reddit.app_id,
                     client_secret = config_reddit.app_secret)

# returns True for read-only connection if everything is configured correctly
print(reddit.read_only)

