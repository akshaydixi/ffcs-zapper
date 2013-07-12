import MySQLdb
import sys
import requests


#Creating connection to database--------------
conn = MySQLdb.connect(host = "127.0.0.1", user = "dronna_admin", passwd = "!january58", db="dronna")
cursor = conn.cursor()


#Arguments--------------
id = sys.argv[1]
ip = sys.argv[2]
#----------------------

ipurl = 'http://freegeoip.net/json/'+str(ip) #FreeGeoIP provides an API which returns a JSON object containing location details of the IP address
response = requests.get(ipurl)
location_json = response.json()
location = '' #The string in which we will store our location


if location_json['city']:
	location +=location_json['city']
if location_json['region_name']:
	location+= ','+location_json['region_name']
if location_json['country_code']:
	location+= ','+location_json['country_code']

#Updating the row with 'location'
try:
	cursor.execute("""
		UPDATE qr_track 
		SET location = '"""+str(location)+"""' WHERE id = """+str(id))
	cursor.connection.commit()
except Exception,e:
	print '[-] Error: ',str(e)

