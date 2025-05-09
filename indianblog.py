import socket
import requests
from urllib.parse import urlparse
def checker(urlink):
    """
    Check if the URL is a valid Indian blog URL.
    """
    url = urlink
# Extract domain
    domain = urlparse(url).netloc
    try:
        # Get IP address
        ip_address = socket.gethostbyname(domain)
        print(f"IP address of {domain}: {ip_address}")

        # Use ipinfo.io for IP geolocation (no API key needed for limited use)
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")

        if response.status_code == 200:
            data = response.json()
            country = data.get("country", "Unknown")
            print(f"Server is located in: {country}")

            if country == "IN":
                print("Running code because server is in India...")
                return True
            else:
                print("Server is not in India. Code will not run.")
        else:
            print(f"Failed to get location. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    return False

def cli():
    import argparse
    parser = argparse.ArgumentParser(description="Check if a blog is hosted in India.")
    parser.add_argument("url", help="The blog URL to check")
    args = parser.parse_args()
    
    if checker(args.url):
        print(" Hosted in India.")
    else:
        print(" Not hosted in India.")
