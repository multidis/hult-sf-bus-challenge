# Reddit data collection

[Reddit](https://www.reddit.com/) provides a [public API](https://www.reddit.com/dev/api/) that can be accessed for free (with certain data volume and query frequency limits). The [PRAW](https://github.com/praw-dev/praw) Python package streamlines interaction with the Reddit API and provides several useful functions for data queries.

In order to access the Reddit API, you need to register as a developer. Please follow the sequence below to be able to query user content at Reddit.

## Register a Reddit application to get access credentials

- Go to `reddit.com` and sign in (sign up for an account if you do not already have one). Please note that you could create a separate account for API access using an `.edu` or `.com` email address. Take a note of your username.

- Go to `https://www.reddit.com/prefs/apps/` and press the "are you a developer? create an app..." button. Choose an app name (e.g., "HultBusChallXX" changing "XX" to your initials) and select "Script" as the app type. You can leave the "description" and "about url" fields blank. Enter `http://www.example.com/unused/redirect/uri` into the "redirect url" field and finally press the "create app" button.

- Record the App ID (a string displayed after the "personal use script" text) and the App Secret (you should also receive a confirmation email with the App Name and App ID, but not the app secret).

- Save your app's credentials in the `reddit_config.py` file (replace the "*"-strings).

## Setup your python environment

Install the `praw` Python package (a side note - as you probably already know, it is a good practice to use separate [Python environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for different projects to reduce package version conflicts etc.):

```sh
conda install -c conda-forge praw
```

Make sure the file with your Reddit credentials, `reddit_config.py`, is in your current Python working folder.

Verify your credentials are properly functioning:

```sh
python reddit_access_verify.py
```

If you see `True` as the output, you are all set for Reddit access in Python.

## Query a specific subreddit

Follow the code in the `reddit_collect_content.ipynb` notebook. Modify the subreddit and the number of posts requested as you see fit. If you experience 500-server errors, that likely means you are requesting too much data from Reddit right away - try reducing the number of posts.

The data collected will be saved in `raw_post_comment_data.json` which you can inspect in a web browser or most text editors and proceed with the analysis (for instance, reading it into a pandas DataFrame).


## Collected posts and comments analysis

Starter example `reddit_explore_starter.ipynb`.


# Reddit archives

Download from [Photon-Reddit archives](https://arctic-shift.photon-reddit.com/download-tool) specifying the subreddit you want and a date range. Note that even one-month interval files can reach several hundred megabytes in size for active subreddits.

Starter analysis example `reddit_explore_archive_starter.ipynb`.

