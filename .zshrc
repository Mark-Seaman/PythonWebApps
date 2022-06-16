#!/bin/bash
# Linux Shell Contexts

export p1=$GITHUB/BACS350/01/ProfileApp
export p2=$GITHUB/BACS350/02/ProfileApp
export p3=$GITHUB/BACS350/03/Pages
export p4=$GITHUB/BACS350/04/Gallery
export p5=$GITHUB/BACS350/05/NotePad
export p6=$GITHUB/BACS350/week6/Blog
export p7=$GITHUB/BACS350/week7/News
export p8=$GITHUB/BACS350/extra/BookBuilder12
export p9=$GITHUB/BACS350/week9/ViewWorkshop
export p10=$GITHUB/BACS350/week10/Photogram
export p11=$GITHUB/BACS350/week11/HammerTest
export p12=$GITHUB/BACS350/week12/CourseBuilder
export p13=$GITHUB/BACS350/week13/ProjectPlan
export p14=$GITHUB/BACS350/week14/AppBuilder

alias p1='cd $p1 && l'
alias p2='cd $p2 && l'
alias p3='cd $p3 && l'
alias p4='cd $p4 && l'
alias p5='cd $p5 && l'
alias p6='cd $p6 && l'
alias p7='cd $p7 && l'
alias p8='cd $p8 && l'
alias p9='cd $p9 && l'
alias p10='cd $p10 && l'
alias p11='cd $p11 && l'
alias p12='cd $p12 && l'
alias p13='cd $p13 && l'
alias p14='cd $p14 && l'


# Other projects
# Lessons
# View Workshop
# Hammer Test
# App Builder
# Course Builder
# Page Probe

figlet BACS 350

# alias e="'/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl'"
alias e="code"

export h=~/Hammer
export w=$h/workshop
export t=$h/templates

export DJANGO_SUPERUSER_USERNAME='seaman'
export DJANGO_SUPERUSER_PASSWORD='seaman'
export DJANGO_SUPERUSER_EMAIL='seaman'

alias superuser='pm createsuperuser --no-input  --email "me@here.us"'

l 
