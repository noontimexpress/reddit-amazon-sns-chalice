from chalice import Chalice
from chalice.app import Cron

import boto3
import urllib
import certifi

app = Chalice(app_name="redditsns")

#subreddit = input("Please enter the subreddit you would like here: ")
#voice = input("Please enter the voice you would like here: ")
#num = input("Please enter the number of posts you would like here: ")

client = boto3.client('sns')

subreddit = "worldnews"
voice = "Amy"
num = "5"

url = "https://snvzm17bhj.execute-api.us-east-1.amazonaws.com/api/subredditspeech?voice=" + voice + "&subreddit=" + subreddit + "&numOfEntries=" + num

resp = urllib.request.urlopen(url,cafile=certifi.where())

longstring = str(resp.read())
start = longstring.find("https")
end = longstring.find(".mp3")
mp3string = longstring[start:end+4]

@app.schedule(Cron(0, 17, '*', '*', '?', '*'))
def every_day(event):
    client.publish(PhoneNumber='+13238683811',
                   Message="Here are the daily top 5 posts on https://www.reddit.com/r/worldnews/ this morning: " + mp3string)
    client.publish(PhoneNumber='+13235018349',
                   Message="Hi! Here are the daily top 5 posts on https://www.reddit.com/r/worldnews/ this morning. " + mp3string + " And remember, Derek loves you!")
