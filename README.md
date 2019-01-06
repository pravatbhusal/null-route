# Null Route
A Python null route script that limits connections on ports to prevent DDos attacks.

# Script's Configuration
Inside the null_route.py file there are a few variables you should configure to match your server's needs.
- The `secure_isp` string should equal to your security service's ISP
  - If you do not use a security service, then do not change the variable
- The `ports` dictionary contains the ports you wish to limit the number of connections per IP Address
  - For example, port 47623 has a maximum connection per IP Address of 100, so it's defined in the dictionary as `"47623": 100`
- The `ip_list_size` integer is the size of the IP list that the `get_ip_connections` method returns
