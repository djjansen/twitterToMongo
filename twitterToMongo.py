from pymongo import MongoClient
client = MongoClient()

db = client.demTweets
collection = db.twitterUsers

def addTwitterUser(userDocument):
	collection.insert_one(userDocument)

users = [{'firstName':'Bernie',
	'lastName':'Sanders',
	'occupation':'Senator',
	'twitterHandle':'@BernieSanders'},
	{'firstName':'Elizabeth',
	'lastName':'Warren',
	'occupation':'Senator',
	'twitterHandle':'@ewarren'},
	{'firstName':'Pete',
	'lastName':'Buttigieg',
	'occupation':'Mayor',
	'twitterHandle':'@PeteButtigieg'},
	{'firstName':'Tom',
	'lastName':'Steyer',
	'occupation':'Hedge Fund Manager',
	'twitterHandle':'@TomSteyer'},
	{'firstName':'Amy',
	'lastName':'Klobuchar',
	'occupation':'Senator',
	'twitterHandle':'@amyklobuchar'},
	{'firstName':'Tulsi',
	'lastName':'Gabbard',
	'occupation':'U.S. Representative',
	'twitterHandle':'@TulsiGabbard'},
	{'firstName':'Michael',
	'lastName':'Bloomberg',
	'occupation':'Businessman/Mayor',
	'twitterHandle':'@MikeBloomberg'},
	{'firstName':'Joe',
	'lastName':'Biden',
	'occupation':'Senator/Vice President',
	'twitterHandle':'@JoeBiden'}]

for user in users:
	addTwitterUser(user)
