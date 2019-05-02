News reporting is a text report that was written to answer the following question.

Please create the below views before running newsreportingtool.py
--Copy below--
CREATE VIEW threetopslugs as
SELECT
  COUNT (log.path) as hits,
  RIGHT(path, -9) as article
FROM
  log
WHERE
  path != '/'
GROUP BY
  log.path
ORDER BY
  hits desc
LIMIT
  3;

CREATE VIEW mostaccessedarticles AS
SELECT
  COUNT (log.path) as hits,
  RIGHT(log.path, -9) as article
FROM
  log
WHERE
  log.status = '200 OK'
GROUP BY
  log.path
ORDER BY
  hits desc;


CREATE VIEW popularauthorbyarticle AS
SELECT
  articles.authors,
  articles.slug,
  articles.title,
  mostaccessedarticle.hits,
  mostaccessedarticle.article
FROM
  articles
  INNER JOIN mostaccessedarticle ON articles.slug = mostaccessedarticle.article;


CREATE VIEW mostpopularauthor AS
SELECT
  popularauthorbyarticle.author,
  SUM (popularauthorbyarticle.hits) AS hitsbyauthor
FROM
  popularauthorbyarticle
GROUP BY
  popularauthorbyarticle.author;
--Copy below--
CREATE VIEW passbydays as
SELECT
  COUNT (status) as value,
  DATE (time) as days
FROM
  log
WHERE
  status = '200 OK'
GROUP BY
    days;

CREATE VIEW failbydays as
SELECT
  COUNT (status) as value,
  DATE (time) as days
FROM
  log
WHERE
  status != '200 OK'
GROUP BY
  days;

CREATE VIEW passfailbydate as
SELECT
    passbydays.days,
    passbydays.value as pass,
    failbydays.value as fail
FROM
    failbydays
    INNER JOIN passbydays ON failbydays.days = passbydays.days;

CREATE VIEW float as
SELECT
    days,
    pass,
    fail,
    fail * 100 / pass as float
FROM
    passfailbydate;

--- Copy above ---

Once the view are created place newsreportingtool.py in your python environment then run python newsreportingtool in the terminal and you should see the output below:


Most popular three articles of all time : Title - Views
---------------------------
Bad things gone, say good people  -  170098 views
Bears love berries, alleges bear  -  253801 views
Candidate is jerk, alleges rival  -  338647 views

Most accessed articles of all time : Title - Views
---------------------------
Candidate is jerk, alleges rival  -  338647 views
Bears love berries, alleges bear  -  253801 views
Bad things gone, say good people  -  170098 views
Goats eat Google's lawn  -  84906 views
Trouble for troubled troublemakers  -  84810 views
Balloon goons doomed  -  84557 views
There are a lot of bears  -  84504 views
Media obsessed with bears  -  84383 views

Most popular authors : Author - Views
---------------------------
Markoff Chaney  -  84557 views
Rudolf von Treppenwitz  -  423457 views
Ursula La Multa  -  507594 views
Anonymous Contributor  -  170098 views

Failure % above 1 % by date: Date | Failure %
---------------------------
2016-07-17  -  2 %
 -----------------------------
Report generated on 2019-05-02 16:54:56.520479
