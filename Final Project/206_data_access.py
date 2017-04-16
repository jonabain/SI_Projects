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


# Put your tests here, with any edits you now need from when you turned them in with your project plan.

class FinalProjectTests(unittest.TestCase):
	def test_matt_damon_tweets(self):
		self.assertEqual(type(matt_damon_tweets),type([]))
	def test_cache(self):
		f = open("SI206_finalproject_cache.json","r").read()
		self.assertTrue("matt_damon" in f)
	def test_movies_table(self):
		conn = sqlite3.connect('final_project_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Movies');
		result = cur.fetchall()
		self.assertTrue(len(result)>=3, "Testing there are at least 3 Movies in the Movies table.")
		conn.close()
	def test_movies_table_columns(self):
		conn = sqlite3.connect('final_project_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Movies');
		result = cur.fetchall()
		self.assertTrue(len(result[0])==6,"Testing that there are 6 columns in the Movies table.")
		conn.close()
	def test_users_table(self):
		conn = sqlite3.connect('final_project_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Users');
		result = cur.fetchall()
		self.assertTrue(len(result)>=3,"Testing that there are at least 3 distinct users in the Users table.")
		conn.close()
	def test_users_table_columns(self):
		conn = sqlite3.connect('final_project_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Users');
		result = cur.fetchall()
		self.assertTrue(len(result[0])==3,"Testing that there are 3 columns in the Users table.")
		conn.close()
	def test_tweets_table(self):
		conn = sqlite3.connect('final_project_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Tweets');
		result = cur.fetchall()
		self.assertTrue(len(result)>=3,"Testing that there are at least 3 distinct Tweets in the Tweets table.")
		conn.close()
	def test_tweets_table_columns(self):
		conn = sqlite3.connect('final_project_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Tweets');
		result = cur.fetchall()
		self.assertTrue(len(result[0])==6,"Testing that there are 6 columns in the Tweets table.")
		conn.close()

# Remember to invoke your tests so they will run! (Recommend using the verbosity=2 argument.)

if __name__ == "__main__":
	unittest.main(verbosity=2)
