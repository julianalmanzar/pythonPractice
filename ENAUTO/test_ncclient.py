from device_info import ios_xe1
from ncclient import manager
import xmltodict

netconf_config = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>4</name>
        <description>ME HICIERON CON NETCONF</description>
          <ip>
            <address>
              <primary>
                <address>4.3.2.1</address>
                <mask>255.255.255.255</mask>
              </primary>
            </address>
          </ip>
          <logging>
          <event>
            <link-status/>
          </event>
        </logging>
      </Loopback>
    </interface>
  </native>
</config>
'''

m = manager.connect(host=ios_xe1["address"],
                         port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False)


print(m.edit_config(netconf_config, target='running'))
