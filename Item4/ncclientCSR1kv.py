from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.115",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )


netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>SalvoSilva</hostname>
  </native>
</config>
"""

netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>11</name>
    <description>Loopback 11 ET DRY7122 Salvo Silva</description>
    <ip>
     <address>
      <primary>
       <address>11.11.11.11</address>
       <mask>255.255.255.255</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""




#netconf_reply = m.edit_config(target="running", config=netconf_hostname)
netconf_reply = m.edit_config(target="running", config=netconf_loopback)

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())