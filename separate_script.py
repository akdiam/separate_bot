import praw

misspellings1 = ["seperate", "seperete", "separete"]

def main():
    reddit = praw.Reddit("bot1", user_agent="PySeparate Bot 0.1")
    subreddit = reddit.subreddit("all")

    # check every submission on a page? gotta look it up
    for submission in subreddit.hot():
        process_comment(submission)

def process_comment(submission):
    # don't want to deal with branches off of main comments
    # replace_more(limit=0) destroys every "MoreComments" object in submission
    submission.comments.replace_more(limit=0)
    # for every 'parent' comment in submission...
    for top_level_comment in submission.comments:
        # make entire comment lower-case for easier checking process
        normalized_comment = top_level_comment.body.lower()
        for indiv_misspelling in misspellings1:
            # if there's a misspelling, reply to comment and correct him/her
            if indiv_misspelling in normalized_comment:
                print("Replying to correct spelling")
                if indiv_misspelling + "d" in normalized_comment:
                    top_level_comment.reply("I think you mean s-e-p-a-r-a-t-e-d ;)")
                    break
                elif indiv_misspelling + "ly" in normalized_comment:
                    top_level_comment.reply("I think you mean s-e-p-a-r-a-t-e-l-y ;)")
                    break
                else:
                    top_level_comment.reply("I think you mean s-e-p-a-r-a-t-e ;)")
                    break

if __name__ == "__main__":
    main()