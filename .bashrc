echo 'Loading settings for BACS350'

alias l='ls -al'

alias s='git status'

alias pull='git pull'

alias pm='python manage.py'
alias serve='pm runserver'
alias dt='pm test'
alias migrate='pm makemigrations && pm migrate'

alias u='d ..'

function d {
    cd $1 && l
}

export p=~/BACS350/week7/Users

cd $p || {
    echo 'MAC'
    export p=~/Github/BACS350/week7/Users
    cd $p
}

git pull

ls -al
