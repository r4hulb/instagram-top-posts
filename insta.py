from instagramy import InstagramUser
import time
from datetime import date

# Information for the script to run
# Put your session id here, refer https://pypi.org/project/instagramy/

sessionId = ""

# Put all the public accounts you are interested here
# can be downloaded from https://www.kaggle.com/datasets/prasertk/top-1000-instagram-influencers
publicAccounts = ["cristiano", "kyliejenner", "leomessi"]

# Time in seconds to sleep between each request
sleepTime = 30

#Maximum number of posts in final result
maxResults = 100

# Consider posts only after this Month and day
todaysDate = (5,31)



def getToday():
    today = date.today()
    return (today.month, today.day)

#comment below line and uncomment next line to read date automatically from computers time
#todaysDate = getToday()

accountData = {}
for account in publicAccounts:
    try:
        user = InstagramUser(account, sessionid=sessionId)
        accountData[account] = user.posts if user else None
        time.sleep(sleepTime)
    except Exception as e:
        print("Error fetching data", e)


topPosts = []
for account in accountData:
    if accountData[account] is None:
        continue
    for post in accountData[account]:
        if (post.taken_at_timestamp.month,post.taken_at_timestamp.day) >= todaysDate:
            topPosts.append((post.likes,post.comments,account,post.post_url))

results = sorted(topPosts,reverse=True)[:maxResults]

for result in results:
    print(result)
