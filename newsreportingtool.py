#!/usr/bin/python
import psycopg2
import datetime

db = psycopg2.connect("dbname=news")
# Fetch top 3 articles records from the database.
c = db.cursor()
top3 = "Select articles.title , threetopslugs.hits , \
threetopslugs.article , articles.slug \
FROM articles INNER JOIN threetopslugs \
ON threetopslugs.article = articles.slug \
ORDER BY threetopslugs.hits DESC; "
c.execute(top3)
top3data = c.fetchall()
print ""
# And let's loop over it too:
print "Most popular three articles of all time : Title - Views"
print "---------------------------  "
for row in top3data:
    print row[0], " - ", row[1], "views"
# Fetch most accessed articles records from the database.
mostaccesseddata = "SELECT articles.title,\
mostaccessedarticles.hits, mostaccessedarticles.article, \
articles.slug FROM articles INNER JOIN \
mostaccessedarticles ON articles.slug = mostaccessedarticles.article \
ORDER BY mostaccessedarticles.hits ASC;"
c.execute(mostaccesseddata)
mostaccesseddata = c.fetchall()
# And let's loop over it too:
print " "
print "Most accessed articles of all time : Title - Views"
print "---------------------------  "
for row in mostaccesseddata:
    print row[0], " - ", row[1], "views"
# Fetch most popular author records from the database.
popularauthorsdata = "SELECT authors.name, mostpopularauthor.hitsbyauthor,\
authors.id, mostpopularauthor.author \
FROM authors INNER JOIN mostpopularauthor \
ON authors.id = mostpopularauthor.author \
ORDER BY mostpopularauthor.hitsbyauthor DESC;"
c.execute(popularauthorsdata)
popularauthorsdata = c.fetchall()
# And let's loop over it too:
print ""
print "Most popular authors : Author - Views"
print "---------------------------  "
for row in popularauthorsdata:
    print row[0], " - ", row[1], "views"

# Fetch Failure % records from the database.
failsdata = "SELECT days , pass , fail , float FROM float where float > 1;"
c.execute(failsdata)
failsdata = c.fetchall()
# And let's loop over it too:
print ""
print "Failure % above 1 % by date: Date | Failure %"
print "---------------------------  "
for row in failsdata:
    print row[0], " - ", row[3], "%"

db.close()
print " -----------------------------"
print "Report generated on", datetime.datetime.now()
