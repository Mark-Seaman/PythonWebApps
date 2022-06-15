# Document Design Pattern

## Overview

This design pattern display a document file as an HTML page.  The file is located in the "Documents" 
directory in the app project source code.  It contains Markdown text that is converted into HTML for 
display.

### Data

The software planner has a cascade of data (Developer Project Milestone Task Notes).

doc/models.py

    This design patten does not require any data models.


### Views

All five views are created to support the interaction with each data model:


doc/views.py

templates/theme.html

templates/document.html

