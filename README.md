# 🪲 Bugtracker

When working on any project of reasonable size, bug reports and feature requests are going to come in faster than you can work on them (or keep them in your head).

This bugtracker application has the following features:

* Home page that displays all tickets, arranged in separate sections, according to current ticket status (i.e. New, In Progress, Done, Invalid)
* Custom User Model to replace Django's built-in one.
* Requires users to login. People who aren't logged in _cannot_ create accounts (don't want any random person to see 🪲 in your application!)
* Authenticated users can:
  * File/create tickets
  * Assign tickets
  * Mark a ticket as invalid
  * Mark a ticket as complete
  * Edit tickets (limited to Title and Description)
* Has a User Detail page where you can see:
  * Current tickets assigned to user
  * Ticket creation history
  * Tickets user has completed
* Has a Ticket Detail page

Some technical deets:

`Ticket` model has the following fields:

*   Title: str
*   Time / Date filed: datetime
*   Description: str
*   User who filed ticket: FK (Foreign Key)
*   Status of ticket: str
    *   Possible statuses
        *   New 
        *   In Progress
        *   Done
        *   Invalid
*   User assigned to ticket: FK
*   User who completed the ticket: FK

When a ticket is filed/created, it will have the following settings:

*   Status: New
*   User Assigned: None
*   User who Completed: None
*   User who filed: Person who's logged in

When a ticket is assigned, these change as follows:

*   Status: In Progress
*   User Assigned: person the ticket now belongs to
*   User who Completed: None

When a ticket is Done, these change as follows:

*   Status: Done
*   User Assigned: None
*   User who Completed: person who the ticket used to belong to

When a ticket is marked as Invalid, these change as follows:

*   Status: Invalid
*   User Assigned: None
*   User who Completed: None

Future Updates:

This bugtracker doesn't really get any points for being pretty. It has just enough of a front end to make it function. I'll come back to the styling in the near future.




