## Your name: Jonathan Bain
## The option you've chosen: 2

# Put import statements you expect to need here!

from itertools import zip_longest
import unittest
import tweepy
import twitter_info
import json
import sqlite3

# Write your test cases here.
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

if __name__ == "__main__":
	unittest.main(verbosity=2)
