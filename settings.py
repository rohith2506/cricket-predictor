'''
This contains all meta data and configuration settings which can be used by script
'''

BASE_URL = "http://stats.espncricinfo.com/ci/engine/stats/index.html"
DATABASE = "/Users/rohspeed/Documents/work/Distributed_systems/projects/cricket/db/cricket.db"

# First Type of cricket(i.e.. class = 1 (or) 2 (or) 3 ...)
TEST_MATCHES = 1
ODI_MATCHES  = 2
T20_MATCHES  = 3
ALL	     = 4


#Type of statistics you need (i.e.. type = "batting" (or) "bowling")
BATTING   = "batting"
BOWLING   = "bowling"
FIELDING  = "fielding"
ALL_ROUND = "allround"
TEAM	  = "team"
AGGREGATE = "aggregate"


# TEAM NAME AND THEIR ID (voila. same ID's for oppositions too.)(i.e.. team/opposition/host = 40 (or) 2..)
AFGHANISTHAN = 40
AUSTRALIA    = 2
BANGLADESH   = 25
INDIA        = 6
IRELAND      = 29
NETHERLANDS  = 15
NEW_ZEALAND  = 5
PAKISTHAN    = 7
SCOTLAND     = 30
SOUTH_AFRICA = 3
SRI_LANKA    = 8
UAE          = 27
WEST_INDIES  = 4
ZIMBAMBWE    = 9
ALL_TEAMS = [AFGHANISTHAN, AUSTRALIA, BANGLADESH, INDIA, NETHERLANDS, NEW_ZEALAND,\
		PAKISTHAN, SCOTLAND, SOUTH_AFRICA, SRI_LANKA, UAE, WEST_INDIES, ZIMBAMBWE]

# VENUE TYPE ( i.e.. home_away = 1 (or) 2 (or) 3..)
HOME_GND 	= 1
OPPOSITION_GND  = 2
NEUTRAL_GND 	= 3


#MATCH RESULT ( i.e.. result = 1 (or) 2 (or) 3..)
MATCH_WON  = 1
MATCH_LOST = 2
MATCH_TIE  = 3
MATCH_NR   = 4


#MATCH OVERALL FIGURES (i.e.. view = "innings" (or) "results" ..)
OVERALL_RESULT  = ""
INNINGS         = "innings"
RESULTS         = "results"
SERIES_AVERAGES = "series"
GND_AVERAGES    = "ground"
HOST		= "host"
OPPOSITION 	= "opposition"
EXTRAS		= "extras"
EXTRAS_BY_INNINGS = "extras_innings"

# TEAM VIEW
views = ["bat","bowl"]
