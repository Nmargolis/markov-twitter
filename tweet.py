# import everything we're using!
import markov
import os
import twitter

# Access twitter keys and tokens from shell
api = twitter.Api(
    consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
    consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
    access_token_key=os.environ["TWITTER_ACCESS_TOKEN_KEY"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"])

# print api.VerifyCredentials()

generator = markov.MarkovMachine()
generator.read_files(['green-eggs.txt'])
tweet = generator.make_text()

status = api.PostUpdate(tweet)
print status.text