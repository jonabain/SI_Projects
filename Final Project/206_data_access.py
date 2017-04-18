###### INSTRUCTIONS ###### 

# An outline for preparing your final project assignment is in this file.

# Below, throughout this file, you should put comments that explain exactly what you should do for each step of your project. You should specify variable names and processes to use. For example, "Use dictionary accumulation with the list you just created to create a dictionary called tag_counts, where the keys represent tags on flickr photos and the values represent frequency of times those tags occur in the list."

# You can use second person ("You should...") or first person ("I will...") or whatever is comfortable for you, as long as you are clear about what should be done.

# Some parts of the code should already be filled in when you turn this in:
# - At least 1 function which gets and caches data from 1 of your data sources, and an invocation of each of those functions to show that they work 
# - Tests at the end of your file that accord with those instructions (will test that you completed those instructions correctly!)
# - Code that creates a database file and tables as your project plan explains, such that your program can be run over and over again without error and without duplicate rows in your tables.
# - At least enough code to load data into 1 of your dtabase tables (this should accord with your instructions/tests)

######### END INSTRUCTIONS #########

# Put all import statements you need here.
from itertools import zip_longest
import unittest
import tweepy
import twitter_info
import json
import sqlite3

# Begin filling in instructions....
####
#### PART 1 - THE LEG WORK
#### SET UP TWEEPY AND CACHING PATTERN
#### WRITE A FUNCTION TO FETCH TWITTER DATA
#### MAKE AN INVOCATION OF THE TWITTER FUNCTION
#### WRITE A FUNCTION TO FETCH MOVIE DATA
# Setup TWEEPY and authenticate twitter (this info in twitter_info file)
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Set up caching pattern
CACHE_FNAME = "SI206_final_project_cache.json"
try:
	cache_file = open(CACHE_FNAME,'r')
	cache_contents = cache_file.read()
	cache_file.close()
	CACHE_DICTION = json.loads(cache_contents)
except:
	CACHE_DICTION = {}

# Define a class Movie

# Define a class TwitterUser

# Define a class Tweet

# Function to get twitter data from search term
def get_user_tweets(key):
	formatted_key = "twitter_{}".format(key)
	if formatted_key in CACHE_DICTION:
		response_list = CACHE_DICTION[formatted_key]
	else:
		response =  api.user_timeline(key)
		CACHE_DICTION[formatted_key] = response
		cache_file = open(CACHE_FNAME, 'w', encoding = 'utf-8')
		cache_file.write(json.dumps(CACHE_DICTION))
		cache_file.close()
		response_list = []
		for r in response:
			response_list.append(r)
	return response_list

# Function to get Twitter data about User

def get_user_twitter_info(key):
	return None

# Function to get movie data
def get_movie_info(key):
	return None

####
#### PART 2 - DATA COLLECTION
####
# Invocations of get_user_tweets
user = "jessicaalba"
user_tweets = get_user_tweets(user)
CACHE_DICTION[user] = user_tweets

# Invocations of get_user_twitter_info

# Invocations of get_movie_info

####
#### PART 3 - STORE/LOAD INFO IN DATABASE
####
# Create a database file

conn = sqlite3.connect('finalproject.db')

# Create tables 

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS Tweets')
table = 'CREATE TABLE IF NOT EXISTS '
table += 'Tweets (tweet_id INTEGER PRIMARY KEY, '
table += 'text TEXT, user_posted TEXT, movie_search TEXT, num_retweets INTEGER, num_favs INTEGER)'
c.execute(table)
c.execute('DROP TABLE IF EXISTS Users')
table = 'CREATE TABLE IF NOT EXISTS '
table += 'Users (user_id INTEGER PRIMARY KEY, '
table += 'screen_name TEXT, num_favs INTEGER)'
c.execute(table)
c.execute('DROP TABLE IF EXISTS Movies')
table = 'CREATE TABLE IF NOT EXISTS '
table += 'Users (id INTEGER PRIMARY KEY, '
table += 'title TEXT, director TEXT, num_languages INTEGER, imdb_rating INTEGER, top_actor TEXT)'
c.execute(table)

# Upload data to database
# Upload User Data
s = 'INSERT INTO Users VALUES (?, ?, ?)'
t = (user_tweets[1]['user']['id'], user_tweets[1]['user']['screen_name'], user_tweets[1]['user']['favourites_count'])
upload = []
upload.append(t)
ids = []
ids.append(user_tweets[1]['user']['id'])
for i in range(len(user_tweets)):
	if len(user_tweets[i]['entities']['user_mentions']) > 0:
		for j in range(len(user_tweets[i]['entities']['user_mentions'])):
			u = api.get_user(user_tweets[i]['entities']['user_mentions'][j]['screen_name'])
			t = (u['id'], u['screen_name'], u['favourites_count'])
			if u['id'] not in ids:
				upload.append(t)
				ids.append(u['id'])
for u in upload:
	c.execute(s, u)
conn.commit()
# Upload Tweet Data

# Upload Movie Data

####
#### PART 4 - PROCESS DATA
####

# Start comparing favorite counts to IMDB ratings


####
#### PART 5 - CREATE AN OUTPUT FILE 
####

# open/or create a txt file to write to
# write findings processed in Part 4






##############################################################
# Put your tests here, with any edits you now need from when you turned them in with your project plan.

class FinalProjectTests(unittest.TestCase):
	def test_matt_damon_tweets(self):
		self.assertEqual(type(matt_damon_tweets),type([]))
	def test_cache(self):
		f = open("SI206_finalproject_cache.json","r").read()
		self.assertTrue("matt_damon" in f)
	def test_movies_table(self):
		conn = sqlite3.connect('final_project.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Movies');
		result = cur.fetchall()
		self.assertTrue(len(result)>=3, "Testing there are at least 3 Movies in the Movies table.")
		conn.close()
	def test_movies_table_columns(self):
		conn = sqlite3.connect('finalproject.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Movies');
		result = cur.fetchall()
		self.assertTrue(len(result[0])==6,"Testing that there are 6 columns in the Movies table.")
		conn.close()
	def test_users_table(self):
		conn = sqlite3.connect('finalproject.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Users');
		result = cur.fetchall()
		self.assertTrue(len(result)>=3,"Testing that there are at least 3 distinct users in the Users table.")
		conn.close()
	def test_users_table_columns(self):
		conn = sqlite3.connect('finalproject.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Users');
		result = cur.fetchall()
		self.assertTrue(len(result[0])==3,"Testing that there are 3 columns in the Users table.")
		conn.close()
	def test_tweets_table(self):
		conn = sqlite3.connect('finalproject.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Tweets');
		result = cur.fetchall()
		self.assertTrue(len(result)>=3,"Testing that there are at least 3 distinct Tweets in the Tweets table.")
		conn.close()
	def test_tweets_table_columns(self):
		conn = sqlite3.connect('finalproject.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Tweets');
		result = cur.fetchall()
		self.assertTrue(len(result[0])==6,"Testing that there are 6 columns in the Tweets table.")
		conn.close()

# Remember to invoke your tests so they will run! (Recommend using the verbosity=2 argument.)

if __name__ == "__main__":
	unittest.main(verbosity=2)
