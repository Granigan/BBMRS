# TSOHA: [Blood Bowl Match Reporting System](http://bb-mrs.herokuapp.com/)
## Project Description
**This project is a course project for Helsinki University.**

[Blood Bowl](http://bloodbowl.com) is a board game that has two player fielding a team of fantasy races to play each other in a bloodier version of rugby. The Blood Bowl Match Reporting System (BBMRS) allows users ("coaches") to create teams and contests, sign teams for contests, and report matches between teams. Coaches and unathorised users ("fans") can also see participating teams and available contests, as well as seeing match history and statistics of each team.

You can try out the system on [Heroku](http://bb-mrs.herokuapp.com) with the following logins. Note that you can also register a new account. (Logins won't work if someone has deleted the account or changed its password.)

| |Admin	|Coach	
|---|---|---
|username|admin|coach
|password|admin|coach

## Weekly Milestones
[See all the weekly reports here](https://github.com/Granigan/BBMRS/blob/master/documentation/weekly_progress.md)

### FINAL WEEK
When preparing for the demo, couple of issues popped up. These are now fixed, along with some quick improvements.

## Documentation
- [Installation Guide](https://github.com/Granigan/BBMRS/blob/master/documentation/install.md)
- [User's Manual](https://github.com/Granigan/BBMRS/blob/master/documentation/manual.md)
- [User Stories](https://github.com/Granigan/BBMRS/blob/master/documentation/user_stories.md)
- [Weekly Progress Reports](https://github.com/Granigan/BBMRS/blob/master/documentation/weekly_progress.md)
- [SQL Statements](https://github.com/Granigan/BBMRS/blob/master/documentation/SQLstatements.md)
- [Database Diagram (image)](https://github.com/Granigan/BBMRS/blob/master/documentation/images/db_diagram2.png)
- [Trello Board](https://trello.com/b/s6HjD0UO/tsoha-project-match-reporting-system-blood-bowl)


## Project Plan and Definitions
### Scope
In Blood Bowl virtually every team is nearly unique, and tracking the progress of each team, and indeed each of its players is a vital part of the game, such a feature is beyond the scope of this project at this stage. Functionality will be limited to naming the team, choosing its race, and signing it up for the contests.

### Functionality and user stories
- Create and login as a coach
- See a list of your teams
- See a list of contests
- Sign up your team to a contest
- Report a match between two teams
- See various statistics / match history

Also see [User Stories](https://github.com/Granigan/BBMRS/blob/master/documentation/user_stories.md).

### Database plan
There are four main tables:
- Account (CRUD): Accounts can be Created (registered), Read (by admin), Updated (pw update by admin), and Deleted (by admin).
- Team (CRD): Teams can be Created, Read, and Deleted (by admin).
- Contest (CRUD): Contests can be Created, Read, Updated (participating team count is updated on sign up), and Deleted (by admin).
- Match (C): Matches are Created and used for team statistics and history.

Additionally, between Contest and Team tables, a connecting ContestTeam table (C) is required.

![db diagram](https://github.com/Granigan/BBMRS/blob/master/documentation/images/db_diagram2.png)

## Remaining Issues
- Team can face itself in a match
- Teams and Contests can have identical names. (Users cannot.)
- 'Resurrection' rules are not enforced, and practically have no effect.

## (Missing) Features for Future Versions
- Choose race from a selection
- Support for players in the team, including their statistics, ie. team roster
- Match report confirmation/validation from the other team via email
- Race specific team roster validation
- Various contest forms
- Team eligibility validation based on contest rules
- Contest score tracking via reported matches
- Improved team statistics
- Coaching (home) page with teams and statistics
- And so much more! (Check [Trello](https://trello.com/b/s6HjD0UO/tsoha-project-match-reporting-system-blood-bowl)!)
