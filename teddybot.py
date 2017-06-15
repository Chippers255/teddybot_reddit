import csv
import praw
import datetime

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("all")

comment_log_file = "teddys_reply_log.csv"

def save_reply(reply):
    with open(comment_log_file, 'a') as f:
        writer = csv.writer(f)
        writer.writeline(reply)
# end def save_reply

for comment in subreddit.stream.comments():
    for name in ['Theodore Roosevelt', 'theodore roosevelt', 'Teddy Roosevelt', 'teddy roosevelt',
                 'Teddy', 'teddy', 'theodore', 'roosevelt', 'rough riders', 'Theodore', 'Roosevelt',
                 'Rough Riders']:
        if name in comment.body:
            teddy_reply = "Did someone say " + name + "?    http://i.imgur.com/XVeG35Z.jpg"
            try:
                comment.reply(teddy_reply)
                reply = [datetime.datetime.now(), comment.id, name, comment.subreddit]
                save_reply(reply)
                print(reply)
            except:
                print("Teddy couldn't do this one!")
            break
