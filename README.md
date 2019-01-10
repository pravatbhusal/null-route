# Null Route
A Python null route program that limits connections on a server to prevent DDos attacks. This program is oriented towards a Unix environment, preferably a Debian-based Linux distribution.

### Learn more about Null Routing
- https://en.wikipedia.org/wiki/Null_route

# Dependencies
Install the dependencies for the project with `pip install -r requirements.txt`

# Configuration
Inside the `config.py` file there are a few variables you should configure to match your server's needs.
- The `run_interval` integer is the interval the null_route.py runs every second
- The `ip_list_size` integer is the size of the IP list that the `get_ip_connections` method returns
- The `limit` integer is the limit to the number of connections per ip address
  
# Running Program
To run the program, execute `nohup python null_route.py`
- The `nohup` package is necessary for the program to run even outside SSH sessions

# Exiting Program
Since the program infinitely runs a loop every `run_interval` seconds, if you wish to see if the process is still running in the background execute `ps -fA | grep python` and check if `null_route.py` appears.  

If you wish to stop or exit the program, execute `pkill -f null_route.py`
