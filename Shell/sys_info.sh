# Find basic system info
echo "###############"
echo "# System Info #"
echo "###############"
echo ""

# SYSTEM BANNERS
echo "Banners:"
motd_banner=`cat /etc/motd`
echo -e "\tMOTD: $motd_banner"
ssh_banner=`cat /etc/ssh/sshd_config | grep banner`
echo -e "\tSSH: $ssh_banner"
ftp_banner=`cat /etc/vsftpd/vsftpd.conf | grep ftpd_banner`
echo -e "\tFTP: $ftp_banner"
echo -e "\n"


# OS INFORMATION
lsb_release -a
headers=$(uname -a)
echo "Kernel Version: $headers"


# AUTOMATICCALY EXECUTING SCRIPTS
echo -e "\nAutomatically Executed Scripts:"
for i in `ls /etc/init.d | grep -v 'functions\|README'`; 
do
    echo -e "\t$i"
done


# SET GID/UID APPLICATIONS
echo -e "\nSet GID/UID Applications:"
for i in `find / -xdev -type f \( -perm -4000 -o -perm -2000 \) 2> /dev/null`;
do
    echo -e "\t$i"
done


# SUDO USERS
echo -e "\nSudo Users:"
for i in `grep '^wheel:.*$' /etc/group | cut -d: -f4`;
do
    echo -e "\t$i"
done


# WEAK PERMISSIONS ON FILES
array=('/etc/passwd' '/etc/shadow' '/etc/profile' '/var/log/wtmp' '/etc/bashrc' '/etc/group')
echo -e "\nWeak File Permissions:"
for i in "${array[@]}";
do
    permissions=`stat -c "%a" $i`
    permissions=${permissions: -1}
    if [[ $permissions -gt 4 ]]
    then
        echo -e "\t$i - Incorrect Permissions"
    else
        echo -e "\t$i - Correct Permissions"
    fi
done


#OPEN PORTS
echo -e "\nOpen Ports:"
echo -e "\n\tPort\tProgram"
echo -e "\t----\t-------"
for i in `netstat -tunalp | awk '{print $4}'`;
do
    if [[ $i =~ ":" ]]
    then
        port=$(echo $i | awk -F":" '{print $NF}')
        program=$(netstat -tunalp | grep -m 1 $port | awk '{print $7}')
        echo -e "\t$port\t$program" 
    fi
done


# PATH VARIABLES
echo -e "\nPATH Variables:"
#ldconfig -p
IFS=': ' read -r -a array <<< `echo $PATH`
for i in "${array[@]}";
do
    echo -e "\t$i"
done


# IDLE ACCOUNTS
echo -e "\nIdle Accounts:"
time=`date +"%T"`
time=$(echo ${time: : -3})
time=$(echo ${time//:})
count=0
IFS=$'\n'
for i in `who`;
do
    login_time=$(echo $i | awk '{print $4}')
    login_time=$(echo ${login_time//:})
    diff=`expr $time - $login_time`
    if [[ $diff -ge 500 ]]
    then
        user=$(echo $i | awk '{print $1}')
        echo -e "\t$user"
        count=`expr $count + 1`
    fi
done
if [[ count -eq 0 ]]
then
    echo -e "\tAll accounts have logged in within the 5 hours"
fi


# WTMP FILE/MONTHLY LOGINS
echo -e "\nMonth's Logins:"
month=$(date | awk '{print $2}')
IFS=$'\n'
for i in `last | grep 'tty' | grep $month`;
do
    echo -e "\t$i"
done

