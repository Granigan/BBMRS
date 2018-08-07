# TSOHA course project

## Weekly Milestones
### Week 3
You can now register at [Herokuapp](http://bb-mrs.herokuapp.com/auth/register), or login at [Herokuapp](http://bb-mrs.herokuapp.com/auth/login) with:
UN: test
pwd: test

Users (a.k.a. coaches) are kept in their own table, teams in another. Team information can be created, read, updated, and deleted (CRUD).

Heroku uses PostgreSQL.

### Week 2
Project itself is now live on [Herokuapp](http://bb-mrs.herokuapp.com/). Teams can be added and listed, and their points can be modified. Coach is also listed, but with no functionality yet.
[User Stories](https://github.com/Granigan/BBMRS/blob/master/documentation/user_stories.md) document has also been added.
This README has the concept image for database diagram.

### Week 1
~~Herokuapp is alive at Herokuapp, including the demo page.~~ (Demo no longer available since week 2.)

## [Blood Bowl Match Reporting System](http://bb-mrs.herokuapp.com/)
### Description
Blood Bowl is a board game that has two players field a team of fantasy races to play each other in a bloodier version of rugby. Team try to score goals during the game, with the team that has more goals scored by the end of the game winning the game.

The Blood Bowl Match Reporting System (BBMRS) allows players ("coaches") to log in, create, update and delete their own team, and to sign it up for any amount of available contests. After signing up a team for a contest, coaches can then report the result of a match they've played with another team in the same contest.

Coaches can also create new contests for teams to sign up for, and different reports of the contests and teams will be available through the web page; e.g. winning percentage, amount of games played, race distribution in a contest, and so forth.

### Functionality and user stories
- Create and login as a coach
- See a list of your teams
- See a list of contests
- Sign up your team to a contest
- Report a match result between your team and another team in the same contest
- See various statistics / reports

Also see [User Stories](https://github.com/Granigan/BBMRS/blob/master/documentation/user_stories.md).


### Scope
While each team is nearly unique, and tracking the progress of each team, and indeed each of its players is a vital part of the game, such a feature is beyond the scope of this project at this stage. Functionality will be limited to naming the team, choosing its race, and signing it up for the contests.

### Database plan
There are four main tables:
- Coach (CRU)
- Team (CRUD)
- Contest (CRUD)
- Match (CRU)

Additionally, between a team and a contest, a team/contest table (R) is required.

![First db diagram](https://github.com/Granigan/BBMRS/blob/master/documentation/images/first_db_diagram.jpg)
*First database diagram*


### External Links
[Trello board for the project](https://trello.com/b/s6HjD0UO/tsoha-project-match-reporting-system-blood-bowl)


### Features for future versions
- Choose race from a table
- Support for players in the team, including their statistics, ie. team roster
- Match report confirmation/validation from the other team via email
- Race specific team roster validation
- Various contest forms
