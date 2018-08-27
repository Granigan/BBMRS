## Weekly Milestones
### "Week" 6
[Matches can now be reported](http://bb-mrs.herokuapp.com/match/new), and the new [Team page](http://bb-mrs.herokuapp.com/teams/details_1) shows the match history and statistics for each team.
Database diagram was updated to match the database in use:
![db diagram](https://github.com/Granigan/BBMRS/blob/master/documentation/images/db_diagram2.png)
Additionally there were small fixes here and there, and the documents were updated to better match the project's status.

### Week 5
Authentication for Admins is now added. Only admins can:
- Access Account Management
- Delete Contests
- Delete Teams
- Delete Accounts

Some usability considerations were made in an attempt to create feasible pipelines, and more are planned and on the way. Many of these are dependent on the few remaining pages to be added to the application and will be more visible in the future.

Finally, first versions of the [User's Guide](https://github.com/Granigan/BBMRS/blob/master/documentation/manual.md) and the [Installation Guide](https://github.com/Granigan/BBMRS/blob/master/documentation/install.md) are now available.

### Week 4
Due to misunderstanding, full CRUD wasn't implemented last week. Contest table now fills these requirements, including the individual read ability (follow the links from [Contest page](http://bb-mrs.herokuapp.com/contests).

The Contest pages also received the largest advances, with the individual pages having the so far most complex SQL query, which finds details for the teams participating in the contest from team, account, and contestteam tables. With the contestteam table combining information from team and contest tables, deleting teams or contests required an update to ensure contestteam was also accordingly cleaned up.

Basic Bootstrap is now included to make things a touch prettier.

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


