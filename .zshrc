#!/bin/bash
# Linux Shell Contexts

export p1=$GITHUB/BACS350/week1/ProfileApp
export p2=$GITHUB/BACS350/week2/ProfileApp
export p3=$GITHUB/BACS350/week3/Pages
export p4=$GITHUB/BACS350/week4/Gallery
export p5=$GITHUB/BACS350/week5/NotePad
export p6=$GITHUB/BACS350/week6/Blog
export p7=$GITHUB/BACS350/week7/News
export p8=$GITHUB/BACS350/extra/BookBuilder12
export p9=$GITHUB/BACS350/week9/ViewWorkshop
export p10=$GITHUB/BACS350/week10/Photogram
export p11=$GITHUB/BACS350/week11/HammerTest
export p12=$GITHUB/BACS350/week12/CourseBuilder
export p13=$GITHUB/BACS350/week13/Sass
export p14=$GITHUB/BACS350/week14/AppBuilder

cd $p7

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
