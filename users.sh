#!/bin/bash
# Script to read in users from a file and create accounts
# based on the infomartion read
# Author - Cameron Clark 

# Loop through each line of the file
while read LINE; do

    path='/bin/bash'

    #get number of columns in line
    num=$(echo $LINE | tr -s '[:punct:]' ' ' | wc -w)

    # Get first and last name from line
    name=$(echo $LINE | tr -s '[:punct:]' ' ' | awk '{print $1 " " $2}')

    # combie first letter of first name with last name
    username=$(echo $name | awk '{print substr ($2, 0, 1) $1}')
    echo $username

    if [ $num -eq '6' ]; then
        dep=$(echo $LINE | tr -s '[:punct:]' ' ' | awk '{print tolower($6)}')
    else
        dep=$(echo $LINE | tr -s '[:punct:]' ' ' | awk '{print tolower($7)}')
    fi

    #echo $dep
    home='/home/$dep/'
    if [ $dep = 'Engineering' ]; then
        path='/bin/csh'
    fi
    
    useradd $username -d $home -g $dep -s $path
done
