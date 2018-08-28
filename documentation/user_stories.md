# User Stories

## Simplified User Stories

- [x] As coach, I want to create my team and sign it for a contest.
- [x] As fan, I want to see the winning percentage of a team.
- [x] As fan, I want to see what contests are available
- [x] As tournament organiser, I want to create a new contest.
- [x] As a winning coach, I want to report my team's victory over another team.
- [x] As admin, I need to delete erroneously created teams, contests, and user accounts.


## User Groups
- [x]Admin
- [x]Tournament organiser/Coach
- [x]Fan (unauthorised user)


## Specific User Stories with Related SQLs

### As fan, I want to see how a team is doing.
*I find the team in the team listing, click on its name and see the team's page, with the match history and total games played, won, and lost, as well as the winning percentage.*

Match history:
```
SELECT m.date_created AS date, w.name AS winner, l.name AS loser
	FROM match AS m
	LEFT JOIN team AS w ON m.winner_id = w.id
	LEFT JOIN team AS l ON m.loser_id = l.id
	WHERE m.winner_id = :id OR m.loser_id = :id order by date
```
Winning percentage:
```
SELECT (count(winner_id)* 100.0 /
	(SELECT count(*) FROM match
	WHERE winner_id = :id OR loser_id = :id))
	FROM match WHERE winner_id = :id
```

### As a fan, I want to see what contests are available.
*I check the contest listing page, and see all the contests, with details on how many teams each can have and already has signed up for, as well as who's running the contest.*

Contest listing:
```
SELECT contest.name, contest.acronym, contest.resurrect
	contest.number_of_teams, contest.maximum_slots, account.name, contest.id
	FROM contest LEFT JOIN account ON account.id = account_id
	ORDER BY contest.name
```

### As a coach, I want to sign a team to a contest.
*After creating a team (and possibly the contest too), I find the contest in the contest listing, and click on it to see its details. In the contest page, I click on the sign up -link, and get to choose my team from the dropdown menu. The list only shows my teams that are not yet signed up for the contest.*

SELECT team.id, team.name 
	FROM team WHERE team.account_id = :a_id 
	AND team.id NOT IN
	(SELECT team.id FROM team, contestteam 
	WHERE team.id = contestteam.team_id 
	AND contestteam.contest_id = :c_id)



### As an admin, I want to delete an account.
*I open the user management and find the account in question. Clicking the Delete-button removes all teams and contests created by the account, and the account itself.*

Contest deletion:
```
DELETE FROM contestteam
	WHERE contestteam.contest_id = :id
```

Team deletion:
```
DELETE FROM contestteam
	WHERE contestteam.team_id = :id
```

### As an admin, I want to stop a user from accessing the site.
*I don't want to delete the account as that would remove its contests as well. Instead, I find the account in the Account Management, click on its link to see the details, and give it a new password. I can also use this to help a user who's forgotten their password.*

Update password:
```
UPDATE account SET password = :pw WHERE id = :id
```
