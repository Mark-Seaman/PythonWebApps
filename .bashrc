echo 'Loading settings for BACS350'

alias l='ls -al'

alias s='git status'

alias pull='git pull'

alias pm='python manage.py'

alias u='d ..'

function d {
    cd $1 && l
}

export p=~/BACS350/week6/BookBuilder

cd $p

ls -al
