## SQL STATEMENTS

### CREATE TABLEs
All the tables are created by SQLAlchemy.

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_account_username ON account (username);
```
```
CREATE TABLE team (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	race VARCHAR(144) NOT NULL, 
	resurrect BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (resurrect IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```
```
CREATE TABLE contest (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	acronym VARCHAR(144) NOT NULL, 
	number_of_teams INTEGER, 
	maximum_slots INTEGER NOT NULL, 
	resurrect BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (resurrect IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```
```
CREATE TABLE contestteam (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	team_id INTEGER NOT NULL, 
	contest_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(team_id) REFERENCES team (id), 
	FOREIGN KEY(contest_id) REFERENCES contest (id)
);
```
```
CREATE TABLE "match" (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	winner_id INTEGER NOT NULL, 
	loser_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(winner_id) REFERENCES team (id), 
	FOREIGN KEY(loser_id) REFERENCES team (id)
);
```

### SQL QUERIES
Single line queries are done with SQLAlchemy _Table.query.get(id)_.

Finds details of contests, including the account name of the contest creator.
```
SELECT contest.name, contest.acronym, contest.resurrect
	contest.number_of_teams, contest.maximum_slots, account.name, contest.id
	FROM contest LEFT JOIN account ON account.id = account_id
	ORDER BY contest.name
```

Finds all contests created by a specified account.
```
SELECT contest.id FROM contest
	WHERE contest.account_id = :id
```

Finds all teams signed to a specific contest, including the name of the account that created the team.
```
SELECT team.name, team.race, account.name
	FROM team, contestteam, account
	WHERE contestteam.contest_id = :id
	AND contestteam.team_id = team.id 
	AND account.id = team.account_id
	ORDER BY team.name
```

Finds how many teams are signed to a specific contest.
```
SELECT count(contestteam.id) FROM contestteam
	WHERE contestteam.contest_id = :id
```

Finds all the contests a specific team has signed up for.
```
SELECT contestteam.id FROM contestteam
	WHERE contestteam.team_id = :id
```

Finds match history for a specific team. Produces a list of all matches the team played in (whether won or lost), with team id replaced with team id, ordered by date.
```
SELECT m.date_created AS date, w.name AS winner, l.name AS loser
	FROM match AS m
	LEFT JOIN team AS w ON m.winner_id = w.id
	LEFT JOIN team AS l ON m.loser_id = l.id
	WHERE m.winner_id = :id OR m.loser_id = :id order by date
```

Finds total amount of matches played by a specific team.
```
SELECT count(id) FROM match
	WHERE winner_id = :id OR loser_id = :id
```

Finds total amount of won matches by a specific team.
```
SELECT count(id) FROM match
	WHERE winner_id = :id
```

Finds total amount of lost matches by a specific team.
```
SELECT count(id) FROM match
	WHERE loser_id = :id
```

Finds the win percentage (wins/total games played) of a specific team.
```
SELECT (count(winner_id)* 100.0 /
	(SELECT count(*) FROM match
	WHERE winner_id = :id OR loser_id = :id))
	FROM match WHERE winner_id = :id
```

Finds all teams' information, including the name of the account that created the team.
```
SELECT team.name, team.race,
	team.resurrect, account.name, team.id
	FROM team LEFT JOIN account ON account.id = account_id
	ORDER BY team.name
```

Finds all teams created by a specific account.
```
SELECT team.id FROM team
	WHERE team.account_id = :id
```

### SQL UPDATES
Some updates are made with SQLAlchemy.

Updates the password with the new input.
```
UPDATE account SET password = :pw WHERE id = :id
```


### SQL DELETES
Single deletions are done with SQLAlchemy.

Deletes all contest entries of a specific contest.
```
DELETE FROM contestteam
	WHERE contestteam.contest_id = :id
```

Deletes all contest entries of a specific team.
```
DELETE FROM contestteam
	WHERE contestteam.team_id = :id
```
