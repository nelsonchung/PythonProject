import os
import time


def Launch_Get_Parameter(OUI, SERIAL_NUMBER, MODEL_NAME, DATA_MODEL):
    os.system("python3 ACS_Interface.py " + OUI + " " + SERIAL_NUMBER + " " + MODEL_NAME + " " + DATA_MODEL)
    return


def Get_WiFi_Statistic():
    Launch_Get_Parameter("5C353B", "342CC447801A", "AP", "Device.WiFi.Radio.")
    Launch_Get_Parameter("5C353B", "342CC447801A", "AP", "Device.WiFi.SSID.")
    return


def Get_GW7557_Test():
    Launch_Get_Parameter("5C353B", "6802B842EC18", "FGW", "Device.DeviceInfo.")
    return


if __name__ == '__main__':
    count = 0
    while 1:
        count += 1
        print("Starting to get wifi statistic via tro09 with %d time" % count)
        Get_GW7557_Test()
        print("wait for 15 seconds")
        time.sleep(15)
