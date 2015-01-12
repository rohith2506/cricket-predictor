'''
This Script will crawl through espncricinfo.com website and gets you all required data
Things to do:-
1) Parsing HTML table is done. need to build table.
'''
import math
import os
import urllib2
import requests
import sqlite3
from bs4 import BeautifulSoup
from settings import *

class CricketStats:
	def __init__(self, db,  url):
		self.db = db
		self.url = url
	

	def combine_all_params(self, params):
		'''Combine all parameters and serve them as meta data into espn stats site'''
		parameters = ""		
		for k,v in params.items():
			if type(v) is list:
				parameters = parameters + ';'.join(["%s=%s" %(k,str(val)) for val in v])
				parameters = parameters + ";"
			else:
				parameters = parameters + (k + "=" + str(v))
				parameters = parameters + ";"
		return parameters


	def parse_values_from_html(self, html):
		''' Parse values from html using BeautifulSoup '''
		#IGNORE ASCII VALUES
		soup = BeautifulSoup(html.encode('utf-8','ignore'))
		tables = soup.find_all('table',attrs={'class':'engineTable'})
		rows = tables[2].find_all('tr',attrs={'class':'data1'})
		match_data = []
		for i in range(0, len(rows)):
			data = rows[i].find_all('td')
			for j in range(0, len(data)):
				data[j] = data[j].get_text()
			match_data.append(data)
		return match_data


	def push_data_to_database(self, batting_data, bowling_data):
		''' 
			parse the data into right values and push it into cricket database 
			Team, Score, Overs, RPO, Inns, Result, Opposition, Ground, Date -- Details from espn
			Team id, team, opponent, runs_1, wickets_1, overs(balls), runs_2, wickets_2, \
				overs(balls), win/loss, home/away/neutral -- Details for table
		'''
		pass





	def crawl_espn(self):	
		'''
		Crawler will crawl through all team's data available and store it in cricket.db
		1) Time line must be added
		2) Batting team (or) Bowling team must be selected
		3) For every team, take last 100 matches.
		4) Parameters in database:- TEAM ID, TEAM, OPPONENT, RUNS_1, WICKETS_1, OVERS(BALLS), RUNS_2, WICKETS_2, \
						OVERS(BALLS), WIN/LOSS, HOME/AWAY/NEUTRAL
		'''
		conn = sqlite3.connect(DATABASE)
		for k in range(1, 5): # Number of pages
			for i in range(0, len(venues)): # Decide Venues
				params = {"class":ODI_MATCHES, 
			  			  "type": TEAM,
			  			  "team": INDIA,
			  			  "template": RESULTS,
			  			  "view":  INNINGS,
			  			  "order_by": "start",
			  			  "orderby": "start",
			  			  "spanmax1": "01+JAN+2014",
			  			  "spanmin1": "01+JAN+2013",
			  			  "spanval1": "span1",
						  "orderbyad": "reverse"}
				params["home_or_away"] = venues[i]
				batting_data = []
				bowling_data = []
				for i in range(0, len(views)):
					if views[i] == "bowl":
						params["team_view"] = views[i]
					parameters = self.combine_all_params(params)
					main_url = self.url + "?" + parameters
					print main_url
					resp = requests.get(main_url)
					html = resp.text
					match_data = self.parse_values_from_html(html)
					if i == 0:
						batting_data.append(match_data)
					else:
						bowling_data.append(match_data)
					print len(match_data)


	def display(self):
		print self.db, self.country, self.url


if __name__ == "__main__":
	obj = CricketStats(DATABASE, BASE_URL)
	obj.crawl_espn()
