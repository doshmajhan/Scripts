# Monitor specified file locations to see if any changes were made
if [ -z "$1" ]
then
    echo "Usage: ./integrity.sh directory"
    exit
fi

location=$1
results="/tmp/integrity.txt"
md5dir="/home/dosh/csec465/lab2/md5sums"

> $results
echo "### Files modified" >> $results

for i in `ls $location`;
do
    tmp="$i.sum"
    tmpdir="$md5dir/$tmp"
    if [ "$(ls $md5dir | grep -c $tmp)" -eq 0 ];
    then
        md5sum $i >> $tmpdir
    else
        r=`md5sum -c $tmpdir`
        echo $r >> $results
        if [ "$(echo $r | grep -c OK)" -eq 0 ];
        then
            md5sum $i >> $tmpdir
        fi
    fi
done

echo "Chec $results for the results of this script."
