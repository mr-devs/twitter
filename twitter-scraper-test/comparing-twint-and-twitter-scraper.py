# Testing out Twitter-scraper...

import twitter_scraper as ts
import twint
import pprint

pp = pprint.PrettyPrinter( indent = 4)

###

count = 0

for tweet in ts.get_tweets("ConanOBrien", pages = 10000):
    count += 1
    # pp.pprint(tweet)

print(count)

###

profile = ts.Profile("ConanOBrien")

profile = profile.to_dict()

pp.pprint(profile)

c = twint.Config()
c.Username = "ConanOBrien"
c.Limit = None
c.Store_object = True
c.Hide_output = True

twint.run.Search(c)
tweets = twint.output.tweets_list

print(len(tweets))

c = twint.Config()
c.Username = "ConanOBrien"
c.Limit = None

twint.run.Lookup(c)
