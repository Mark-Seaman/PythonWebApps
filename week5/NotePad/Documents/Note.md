# Note Design Pattern

## Overview

This design pattern displays a simple data record in the database as an HTML page.  Each note has a title
and body. A web page displays the title and body using the current application theme.

The body contains Markdown text that is converted into HTML for 
display.

There are two different views for showing the data records.

* List View - shows all of the data objects
* Details View - shows one of the data objects


### Data

The software planner has a cascade of data (Developer Project Milestone Task Notes).

note/models.py

    This design patten does not require any data models.


### Views

All five views are created to support the interaction with each data model:


note/views.py

templates/theme.html

templates/note.html

templates/notes.html

