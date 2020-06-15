#Need to install pywifi module first by "pip install pywifi"
import pywifi
import time

SSID_24G_NAME="!!!AP7465-2G"
SSID_24G_PASSWORD="12345678"
SSID_5G_NAME="!!!AP7465-5G"
SSID_5G_PASSWORD="12345678"
WAIT_TIME=20

##################################
##For scanning wifi in neighbor
##################################
def Scan():
    wifi=pywifi.PyWiFi()
    interface=wifi.interfaces()[0]
    interface.scan()
    ssids_scan_result=interface.scan_results()
    for ssid in ssids_scan_result:
        print(ssid.ssid)

##################################
##Show local interface name
##################################
def ShowInterfaceName():
    wifi=pywifi.PyWiFi()
    interfaces=wifi.interfaces()
    for interface in interfaces:
        print(interface.name())
    return

def GetWlan0Interface():
    wifi=pywifi.PyWiFi()
    interfaces=wifi.interfaces()
    for interface in interfaces:
        if "wlan0"==interface.name():
            return interface
    return

##################################
##Do the connection
##################################
def Connect(wifi_ssid_name, wifi_password):
    #wifi=pywifi.PyWiFi()
    #interface=wifi.interfaces()[1]
    interface=GetWlan0Interface()

    interface.disconnect()
    #wait WAIT_TIME after disconnection
    time.sleep(WAIT_TIME)
    profile_info=pywifi.Profile()
    profile_info.ssid=wifi_ssid_name
    profile_info.auth=pywifi.const.AUTH_ALG_OPEN
    profile_info.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
    profile_info.cipher=pywifi.const.CIPHER_TYPE_CCMP
    profile_info.key=wifi_password
    interface.remove_all_network_profiles()
    tmp_profile=interface.add_network_profile(profile_info)
    #wait WAIT_TIME after conneciton
    interface.connect(tmp_profile)
    time.sleep(WAIT_TIME)
    if interface.status()==pywifi.const.IFACE_CONNECTED:
        print("Connected with %s" %wifi_ssid_name)
    elif pywifi.const.IFACE_DISCONNECTED==interface.status():
        print("Disconnected")
    elif pywifi.const.IFACE_SCANNING==interface.status():
        print("Scanning")
    elif pywifi.const.IFACE_INACTIVE==interface.status():
        print("Interface inactive")
    elif pywifi.const.IFACE_CONNECTING==interface.status():
        print("Connecting")
    else :
        print("Unknown")

if __name__ == "__main__":
    #Scan()
    count=1;
    while True:
        #Connect 24G
        print("This is %d time to test" %count)
        print("Trying to connect 24G")
        Connect(SSID_24G_NAME, SSID_24G_PASSWORD)
        #Connect 5G
        print("Trying to connect 5G")
        Connect(SSID_5G_NAME, SSID_5G_PASSWORD)
        time.sleep(WAIT_TIME)
