import subprocess
import requests
import json

# the security ISP your server uses for DDoS protection; do not change if the server is not using a security ISP
secure_isp = "Cloudflare, Inc."

# ports to limit using a maximum number of connections
ports = {"47623": 20, "47624": 20, "5432": 20, "22": 20, "8080": 20}

# size of each ip list
ip_list_size = 10


# return if an ip address is from an isp
def is_isp_address(ip_address, isp):
    try:
        ip_info = requests.get("http://ip-api.com/json/" + ip_address).content
        ip_info = json.loads(ip_info)
        ip_isp = ip_info["isp"]
        return ip_isp == isp
    except:
        return False


# return if an ip address is the host
def is_host(ip_address):
    try:
        public_ip_cmd = """dig TXT +short o-o.myaddr.l.google.com @ns1.google.com | awk -F'"' '{ print $2}'"""
        public_ip = subprocess.check_output(public_ip_cmd, shell=True).strip()
        return ip_address == "127.0.0.1" or ip_address == "localhost" or ip_address == public_ip
    except:
        return False


# return connected ips with the most connections in descending order
def get_ip_connections(port, size):
    list_ips_cmd = "netstat -tn 2>/dev/null | " + "grep :" + str(port) + " | " + \
                   "awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr | head -" \
                   + str(size)
    ip_addresses = subprocess.check_output(list_ips_cmd, shell=True)

    # return a list of the ip addresses with the number of connections per ip
    return ip_addresses.split()


# null route a malicious ip address
def null_route(ip_address):
    null_route_cmd = "route add " + ip_address + " gw 127.0.0.1 lo"
    subprocess.call(null_route_cmd, shell=True)
    # NOTE: if you wish to delete the null route later, execute "route delete ip_address"


# analyze each ip address and its number of connections
def analyze(port, list_size, limit):
    ip_array = get_ip_connections(port, list_size)
    index = 1
    while index < len(ip_array):
        connections = int(ip_array[index - 1])
        ip_address = ip_array[index]

        # each foreign ip address that goes over the limit gets null routed
        if (not is_host(ip_address)) \
                and (not is_isp_address(ip_address, secure_isp)) \
                and connections > int(limit):
            null_route(ip_address)

        next_ip_index = 2
        index += next_ip_index


# analyze each port from the ports dictionary
for key in ports:
    analyze(port=key, list_size=ip_list_size, limit=ports[key])
