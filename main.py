import json
import praw

# Initialize PRAW with your credentials
secrets = json.load(open("secrets.json"))
reddit = praw.Reddit(
    client_id= secrets["client_id"],
    client_secret= secrets["client_secret"],
    user_agent=secrets["user_agent"],
    username=secrets["username"],
    password=secrets["password"]
)

# Fetch your submissions
user = reddit.user.me()
submissions = user.submissions.new(limit=None)

# Loop through each submission
i = 0
for submission in submissions:
    i += 1
    # Uncomment the next line to delete the post
    submission.delete()
    print(f"Processed post: {submission.title}")

# https://praw.readthedocs.io/en/stable/code_overview/other/listinggenerator.html 
# Use NONE to get all of them.  In my case still may need to run this more than once. 
comments = list(user.comments.new(limit=None))
for comment in comments:
            print(f"Deleting comment {comment.id}")
            print(f"Deleting comment {comment.body}")
            comment.delete()

comments = list(user.comments.top(limit=None))
for comment in comments:
            print(f"Deleting comment {comment.id}")
            print(f"Deleting comment {comment.body}")
            comment.delete()

print("Cleanup complete.\n")
print("Note that Messages in your inbox, Private messages, may need to be deleted manually.")