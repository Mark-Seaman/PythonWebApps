#!/bin/bash
# Linux Shell Context

figlet WEEK 1  Building Web Apps


# Variables
export g=$HOME/Github
export se=$g/UNC-CS-350
export wa=$g/UNC-BACS-350
export p=$g/BACS350


# Linux command context
alias hammer="source ~/Hammer/hammer/zshrc"
alias g='grep --color=auto'
alias l='ls -al'
alias u='d ..'
alias host=hostname
alias h='history 100'
alias p=python

# Git aliases
alias s='git status'
alias gh='d $g'
alias gl='git log --name-only'
alias gd='git diff'
alias gco='git checkout'

# Django aliases
alias pm='python manage.py'
alias serve='pm runserver'
alias dt='pm test'
alias migrate='pm makemigrations && pm migrate'
alias web='open http://localhost:8000'

# Test aliases
alias tst='pm tst run'
alias tlike='pm tst like && tst'
alias tres='pm tst results'
alias treset='pm tst reset'
alias qt='pm tst quick'

# Servers
alias deploy=echo 'NOT IMPLEMENTED'

# UNC
alias wa='. $wa/zshrc'
alias se='. $se/zshrc'

# Linux functions
function d {
    directory=$1
    [ -z "$1" ] && directory="$p"
    [ -z "$1" ] || echo $directory && cd $directory && l
}

function c {
    git pull           &&
    git add -A .       &&
    git commit -m "$*" &&
    git push
    git status
}

function e {
    d=`pwd`         && 
    cd $p           && 
    pm edit $d $*   && 
    cd -
}

function cptree {
    rsync -auv "$1/" "$2"
}



# Python environment
# source ~/.venv/bin/activate
export PATH=$PATH:/Users/seaman/.pyenv/versions/3.10.3/bin
echo "Python environment" -c
echo PYENV = `pyenv which python`
echo PYTHON_PATH = `which python`
pip freeze

# Go to Project Directory
echo "Home Directory = $p"
cd $p
git pull
ls -al

