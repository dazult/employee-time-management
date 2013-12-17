Employee Time Management
===========

Django Employee Time Management app.

Completed by John Doran as part of Dazult's graduate developer staff training programme.


Overview
===========

The purpose of the timekeeping app is to record employees daily hours worked, 
and store the clock-in and clock-out information in a database. the employee can request 
leave on the basis that a days notice is required for a day off, and a weeks notice is 
required for a week off.

When an employee accesses the application they can:

    - Enter there employee ID, password and Clock-in or Clock-out when authenticated.
    - Constraints:
        ~ If the employee is already logged in they cannot login again until they log out first
        ~ The employee cannot logout, after twelve hours from previous login (must contact manager to log them out)
    - On the holiday request form they can enter there employee ID, password, date and time from/to and request holidays. 

When a manager logs in they are able to:

    - Access the managers area: //mgnt/ 
    - View employees timesheets
    - View, approve, reject or cancel employee holiday requests
    - View employees sick leave
    - Enter employees sick leave
    - Clock-in and Clock-out employees

Dependencies
===========
    * jQuery
    * jQuery-datatables
    * jQuery-timepicker
    * jQuery-ui


