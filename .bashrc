echo 'Loading settings for BACS350'

# Linux commands
alias l='ls -al'
alias u='d ..'
function d {
    cd $1 && l
}

# Git aliases
alias s='git status'
alias pull='git pull'
alias push='git pull && git push'

# Django aliases
alias pm='python manage.py'
alias serve='pm runserver'
alias dt='pm test'
alias migrate='pm makemigrations && pm migrate'


# Use the appropriate directory
x=~/BACS350             && [ -d $x ] &&  p=$x
x=~/Github/BACS350      && [ -d $x ] &&  p=$x
x=~/Documents/BACS350   && [ -d $x ] &&  p=$x
export p=$x


# Go to Project Directory
echo "Home Directory = $p"
cd $p/week7/Users

git pull

ls -al
