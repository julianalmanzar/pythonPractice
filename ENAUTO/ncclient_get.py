from device_info import ios_xe1
from ncclient import manager
import xml.dom.minidom
import xmltodict

# NETCONF filter to use
netconf_filter = open("filter-ietf-interfaces.xml").read()

m = manager.connect(host=ios_xe1["address"],
                         port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False)

##Obtener config en prettyxml
# netconf_reply = m.get_config(source="running")
# print(type(netconf_reply.xml))
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())




# Get Configuration and State Info for Interface
netconf_reply = m.get(netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
# # Process the XML and store in useful dictionaries
# intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
# intf_config = intf_details["interfaces"]["interface"]
# intf_info = intf_details["interfaces-state"]["interface"]
# #
# print("")
# print("Interface Details:")
# print("  Name: {}".format(intf_config["name"]))
# print("  Description: {}".format(intf_config["description"]))
# print("  Type: {}".format(intf_config["type"]["#text"]))
# print("  MAC Address: {}".format(intf_info["phys-address"]))
# print("  Packets Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
# print("  Packets Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))