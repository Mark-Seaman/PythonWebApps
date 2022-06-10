#!/bin/bash
# Linux Shell Contexts

export p1=$GITHUB/BACS350/week1/ProfileApp
export p2=$GITHUB/BACS350/week2/ProfileApp
export p3=$GITHUB/BACS350/week3/Pages
export p4=$GITHUB/BACS350/week4/Gallery
export p5=$GITHUB/BACS350/week5/NotePad
export p6=$GITHUB/BACS350/week6/Blog
export p7=$GITHUB/BACS350/week7/BookBuilder
export p8=$GITHUB/BACS350/week8/Photogram
export p9=$GITHUB/BACS350/week9/Lessons
export p10=$GITHUB/BACS350/week10/Photogram
# View Workshop
# Hammer Test
# App Builder
# Course Builder
# Page Probe
cd $p7

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
