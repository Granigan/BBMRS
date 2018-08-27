# TSOHA Course Project
## [Blood Bowl Match Reporting System](http://bb-mrs.herokuapp.com/)
Admin user:
```
UN: testi 
PW: testi
```
Normal user:
```
UN: tester
PW: tester
```

## Weekly Milestones
### "Week" 6
[Matches can now be reported](http://bb-mrs.herokuapp.com/match/new), and the new [Team page](http://bb-mrs.herokuapp.com/teams/details_1) shows the match history and statistics for each team.
Database diagram was updated to match the database in use:
![db diagram](https://github.com/Granigan/BBMRS/blob/master/documentation/images/db_diagram2.png)
Additionally there were small fixes here and there, and the documents were updated to better match the project's status.

[See all the weekly reports here](https://github.com/Granigan/BBMRS/blob/master/documentation/weekly_progress.md)


### Project Description
Blood Bowl is a board game that has two players field a team of fantasy races to play each other in a bloodier version of rugby. Team try to score goals during the game, with the team that has more goals scored by the end of the game winning the game.

The Blood Bowl Match Reporting System (BBMRS) allows players ("coaches") to log in, create, update and delete their own team, and to sign it up for any amount of available contests. After signing up a team for a contest, coaches can then report the result of a match they've played with another team in the same contest.

Coaches can also create new contests for teams to sign up for, and different reports of the contests and teams will be available through the web page; e.g. winning percentage, amount of games played, race distribution in a contest, and so forth.

### Functionality and user stories
- Create and login as a coach
- See a list of your teams
- See a list of contests
- Sign up your team to a contest
- Report a match between two teams
- See various statistics / match history

Also see [User Stories](https://github.com/Granigan/BBMRS/blob/master/documentation/user_stories.md).

### Scope
While each team is nearly unique, and tracking the progress of each team, and indeed each of its players is a vital part of the game, such a feature is beyond the scope of this project at this stage. Functionality will be limited to naming the team, choosing its race, and signing it up for the contests.

### Database plan
There are four main tables:
- Account (CRUD)
- Team (CRD)
- Contest (CRUD)
- Match (CR)

Additionally, between a team and a contest, a team/contest table (R) is required.

![db diagram](https://github.com/Granigan/BBMRS/blob/master/documentation/images/db_diagram2.png)

### External Links
[Trello board for the project](https://trello.com/b/s6HjD0UO/tsoha-project-match-reporting-system-blood-bowl)


### Features for future versions
- Choose race from a table
- Support for players in the team, including their statistics, ie. team roster
- Match report confirmation/validation from the other team via email
- Race specific team roster validation
- Various contest forms
