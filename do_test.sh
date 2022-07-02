#!/bin/sh

set -e

if [ -z $1 ]; then
    echo Fail: No argument
    echo Hint: Choose a target file name or use \'all\' argument
    exit 1
fi

if [ $1 = 'all' ]; then
    for p in ./tests/*.py; do
        p=${p##*/}
        p=${p%%.py}

        if [ ${p} = '__init__' ] ||
           [ ${p} = 'gen_predef' ] || 
           [ ${p} = 'main' ]; then
            continue
        fi
        echo Test name is $p
        python -m tests.$p
    done
    exit 0
fi

for p in $@; do
    echo Test name is $p
    python -m tests.$p
done
