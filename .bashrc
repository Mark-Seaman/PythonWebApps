echo 'Loading settings for BACS350'

# Linux commands
alias b='source $p/.bashrc'
alias l='ls -al'
alias u='d ..'
function d {
    cd $1 && l
}
function c {
    git pull &&
    git add -A .  &&
    git commit -m "$*" &&
    git push
    git status
}

# Git aliases
alias s='git status'
alias pull='git pull'
alias push='git pull && git push'

# Django aliases
alias pm='python manage.py'
alias serve='pm runserver'
alias dt='pm test'
alias qt='pm quick_test'
alias migrate='pm makemigrations && pm migrate'


# Use the appropriate directory on different systems
x=~/BACS350             && [ -d $x ] &&  p=$x
x=~/Github/BACS350      && [ -d $x ] &&  p=$x
x=~/Documents/BACS350   && [ -d $x ] &&  p=$x
export p=$p


# Go to Project Directory
echo "Home Directory = $p"
cd $p/week12/ViewWorkshop

git pull

ls -al
