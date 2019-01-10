from ipaddress import IPv4Address, IPv4Network
import subprocess


# return ipv4 addresses from cloudflare
def get_cloudflare_ipv4_ranges():
    try:
        ip_ranges_cmd = "curl -s https://www.cloudflare.com/ips-v4"
        ip_ranges = str(subprocess.check_output(ip_ranges_cmd, shell=True).decode('utf-8')).split()
        return ip_ranges
    except Exception as error:
        print("Could not receive the ipv4 addresses from cloudflare! " + error)
        return []


cloudflare_ipv4_ranges = get_cloudflare_ipv4_ranges()


# return if an ip address is in range with cloudflare's ips
def ip_in_cloudflare_range(ip_address):
    try:
        for range in cloudflare_ipv4_ranges:
            net = IPv4Network(range)
            in_range = IPv4Address(ip_address) in net
            if in_range:
                return True
    except:
        return False
    return False
