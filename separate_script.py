import praw

#print(curr_dir)
reddit = praw.Reddit("bot1", user_agent="PySeparate Bot 0.1")
#subreddit = reddit.subreddit("Showerthoughts")
print(reddit.user.me())

