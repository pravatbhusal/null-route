import config
import subprocess


# return if an ip address is from an isp
def is_isp_address(ip_address, isp):
    try:
        ip_isp_cmd = "curl -s https://www.whoismyisp.org/ip/" + ip_address + " | grep -oP " + """'\\bisp\">\\K[^<]+'"""
        ip_isp = subprocess.check_output(ip_isp_cmd, shell=True).decode('utf-8')
        return isp in ip_isp
    except Exception as error:
        print("Warning: Could not connect to the WhoIs API service! " + str(error))
        return False


# return the host's public ip address
def get_host():
    try:
        public_ip_cmd = """dig TXT +short o-o.myaddr.l.google.com @ns1.google.com | awk -F'"' '{ print $2}'"""
        public_ip = subprocess.check_output(public_ip_cmd, shell=True).strip()
        return public_ip
    except Exception as error:
        print("Warning: Could not connect to Google's Public IP API Service! " + str(error))
        return "127.0.0.1"


# return connected ips with the most connections in descending order
def get_ip_connections(size):
    list_ips_cmd = "netstat -tn 2>/dev/null " + \
                   "| awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr | head -" \
                   + str(size)
    print(list_ips_cmd)
    ip_addresses = subprocess.check_output(list_ips_cmd, shell=True)

    # return a list of the ip addresses with the number of connections per ip
    return ip_addresses.split()


# null route a malicious ip address
def null_route(ip_address):
    print("Null Routing malicious IP Address " + ip_address + ". If you wish to delete the " +
          "the null route later, execute 'route delete " + ip_address + "'")
    null_route_cmd = "route add " + ip_address + " gw 127.0.0.1 lo"
    subprocess.call(null_route_cmd, shell=True)


# analyze each ip address and its number of connections
def analyze(list_size, limit):
    ip_array = get_ip_connections(list_size)
    index = 1
    while index < len(ip_array):
        connections = int(ip_array[index - 1])
        ip_address = ip_array[index].decode('utf-8')
        is_host = ip_address == host or ip_address == "localhost" or ip_address == "127.0.0.1"

        # each foreign ip address that goes over the limit gets null routed
        if (not is_host) \
                and (not is_isp_address(ip_address, config.secure_isp)) \
                and connections > int(limit):
            print("Detected malicious IP Address " + ip_address + " with " + str(connections) + " connections!")
            null_route(ip_address)

        next_ip_index = 2
        index += next_ip_index


# run this script every "run_interval" seconds from the config.py file
def run_script():
    import time
    print("Null Route script initiated!")
    print("Use Ctrl+C or 'pkill -f /path/to/null_route.py' to stop the script.")
    while True:
        print("Analyzing for malicious IP Addresses...")
        analyze(list_size=config.ip_list_size, limit=config.limit)
        print("Finished analysis. Analyzing again in " + str(config.run_interval) + " seconds.")
        time.sleep(config.run_interval)


host = get_host()
run_script()
