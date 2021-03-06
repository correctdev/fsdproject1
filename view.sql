CREATE VIEW threetopslugs as SELECT COUNT (log.path) as hits, RIGHT(path, -9) as article FROM log WHERE path != '/' GROUP BY log.path ORDER BY hits desc LIMIT 3;

CREATE VIEW mostaccessedarticles AS SELECT COUNT (log.path) as hits, RIGHT(log.path, -9) as article FROM log WHERE log.status = '200 OK' GROUP BY log.path ORDER BY hits desc;

CREATE VIEW popularauthorbyarticle AS SELECT articles.author, articles.slug, articles.title, mostaccessedarticles.hits, mostaccessedarticles.article FROM articles INNER JOIN mostaccessedarticles ON articles.slug = mostaccessedarticles.article;

CREATE VIEW mostpopularauthor AS SELECT popularauthorbyarticle.author, SUM (popularauthorbyarticle.hits) AS hitsbyauthor FROM popularauthorbyarticle GROUP BY popularauthorbyarticle.author;

CREATE VIEW totalbydays as SELECT COUNT (status) as value, DATE (time) as days FROM log GROUP BY days;

CREATE VIEW failbydays as SELECT COUNT (status) as value, DATE (time) as days FROM log WHERE status != '200 OK' GROUP BY days;

CREATE VIEW passfailbydate as SELECT totalbydays.days, totalbydays.value as total, failbydays.value as fail FROM failbydays INNER JOIN totalbydays ON failbydays.days = totalbydays.days;

CREATE VIEW float as SELECT days, total, fail, ((fail+0.0) / (total+0.0))*100.0 as float FROM passfailbydate;
