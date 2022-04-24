# import the requests library
import requests
import sys

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# use the IP address or hostname of your Cat9300
HOST = '10.10.20.48'

# use your user credentials to access the Cat9300
USER = 'developer'
PASS = 'C1sco12345'


# create a main() method
def main():
    """Main method that retrieves the Interface details from Cat9300 via RESTCONF."""

    # url string to issue GET request
    url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1/".format(h=HOST)
    #url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/hostname".format(h=HOST)
    #url = "https://{h}/restconf/api/config/native/ip/route".format(h=HOST)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    # print the json that is returned
    print(response.text)

if __name__ == '__main__':
    sys.exit(main())