# Null Route
A Python null route program that limits connections on ports to prevent DDos attacks. This program is oriented towards a Unix environment, specifically a Debian-based Linux distribution.

### Learn more about Null Routing
- https://en.wikipedia.org/wiki/Null_route

# Dependencies
Install the dependencies for the project with `pip install -r requirements.txt`

# Configuration
Inside the `config.py` file there are a few variables you should configure to match your server's needs.
- The `run_interval` integer is the interval the null_route.py runs every second
- The `ip_list_size` integer is the size of the IP list that the `get_ip_connections` method returns
- The `ports` dictionary contains the ports you wish to limit the number of connections per IP Address
  - For example, if you want port 47623 to have a maximum connection per IP Address of 100, insert this into the dictionary: `"47623": 100`
- The `secure_isp` string should equal to your security service's ISP
  - If you do not use a security service, then do not change the variable
  
# Exiting Program
Since the program infinitely runs a loop every `run_interval` seconds, if you wish to see if the process is still running in the background execute `ps -fA | grep python` and check if `null_route.py` appears.  

If you wish to stop or exit the program, execute `pkill -f /path/to/null_route.py`
