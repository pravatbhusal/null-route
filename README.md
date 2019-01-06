# Null Route
A Python null route script that limits connections on ports to prevent DDos attacks.

### Learn more about Null Routing
- https://en.wikipedia.org/wiki/Null_route

# Script's Configuration
Inside the null_route.py file there are a few variables you should configure to match your server's needs.
- The `secure_isp` string should equal to your security service's ISP
  - If you do not use a security service, then do not change the variable
- The `ports` dictionary contains the ports you wish to limit the number of connections per IP Address
  - For example, if you want port 47623 to have a maximum connection per IP Address of 100, insert this into the dictionary: `"47623": 100`
- The `ip_list_size` integer is the size of the IP list that the `get_ip_connections` method returns

# Cron Job Configuration
Cron Jobs allow for a server to execute scripts for every specified time.   

For this script, we are going to run a cron job every 10 minutes.
- Execute `crontab -e` and in the bottom of the crontab type this cron job `*/10 * * * * python [PATH_TO_NULL_ROUTE.py]`  
and replace the `[PATH_TO_NULL_ROUTE.py]` to your `null_route.py` file's path  
- Exit and save the cron-job file with `Ctrl + X`

If you wish to modify the cron job timing to your liking, then this tool may help
- https://crontab.guru/every-10-minutes

### Learn more about Cron
- https://en.wikipedia.org/wiki/Cron
