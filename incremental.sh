# up trivial version
# git q
# ./install.sh

increment_version()
{
    path_file="setup.py"

    # Extract version
    str_version=($(cat $path_file | grep -o "version='.\+'" | grep -o "[0-9]\+"))

    v_major=${str_version[0]}
    v_minor=${str_version[1]}
    v_patch=${str_version[2]}
    v_original=$v_major.$v_minor.$v_patch

    # Increment version
    if [ -z $1 ] || [ $1 == 'patch' ]; then
        v_patch=$((1 + $v_patch))
    elif [ $1 == 'minor' ]; then
        v_minor=$((1 + $v_minor))
    elif [ $1 == 'major' ]; then
        v_major=$((1 + $v_major))
    else    
        echo Invalid incremental target
        exit 1
    fi

    # Replace version
    v_revision=$v_major.$v_minor.$v_patch

    sed -i "s/$v_original/$v_revision/" $path_file
}

push2git()
{
    git q
}

update_pycomar()
{
    pip install --upgrade --no-cache-dir git+https://github.com/KIMGEONUNG/pycomar
}


increment_version 'patch'
push2git
update_pycomar
