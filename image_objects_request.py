'''
A script to display the images in the sqlite3 database using 
bottle to handle the http request.  Also serves the html page

kawandeep virdee
@kawantum
'''


import sqlite3
from bottle import route, run, debug

#global var
links = {}
num_images = 10;


#initially pull from db 
@route('/inspiration/data/:start')
def display_data(start):
	con = sqlite3.connect('images.db')
	c=con.cursor()
	c.execute("select count(link) from images")
	num_entries = c.fetchall()
	num_entries = int(num_entries[0][0])-int(start)
	c.execute("select * from images where rowid < "+str(int(num_entries)+1)+" and rowid > "+str(int(num_entries)-num_images)+"")
	result = c.fetchall()	
	c.close()
	for i in xrange(len(result)): links[i] = result[len(result)-1-i][0]
	#result = {}
	#for i in xrange(num_images): result[i]=links[i]
	return links
	#return ''.join(str(i) for i in html)


@route('/inspiration')
def get_index():
	html = open('website.html','r')
	return html
debug(True)	
run(host='localhost', port=9999, reloader=True)


