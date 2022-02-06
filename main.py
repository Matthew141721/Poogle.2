# This is my first Python project!
# This project is to help individuals (with Fiber) troubleshoot before calling their internet service provider.
print("Welcome to Fiber Internet Support. ")
name = input("Could I have your name please? ")
print("Hello " + name + ", thank you for contacting Fiber Internet Support.")
issue = input("How may I assist you? ")
print("Okay!" + "Let's start with a few troubleshooting steps.\n ")

bill = input("Have you payed the internet bill?\n" + "NOTE: Please reply with a CAPITOL Y or N: ")
if bill == "N":
    print("Please contact your Internet Service Provider")
    import sys
    sys.exit()

elif bill == "Y":
    print(" ")
print("Note: If you payed bill on due date it may take a business day for ISP office to fix. ")
print("You can power cycle modem/router to resolve issue. ")
print("Continue\n")

print("Great! Our next step would be to identify the lights on the modem/router ")
print("Here is an example of correct lights for an ONT: \n" + "Power: Green \n" + "Optical(Fiber): Green")
print("LAN: Green\n")
print("Here is an example of correct lights for router: \n" + "Power: Green \n" + "Broadband: Green")
print("Service: Green\n" + "2.4/5ghz: Green\n")

lights = input("Do you have all solid lights? \n" + "NOTE: Please reply with a CAPITOL Y or N: ")
if lights == "Y":
    print("Continue to the next step\n")
    print("Now that you see no lights flashing or any lights that are Orange/Red ")
    print("1. If you cannot connect through an ethernet cable try a new cable or different ETH port")
    print("2. If the issue is with wireless devices try to power off device for 15 seconds")
    print("3. You can also go into network settings to delete and add the network back to device. ")
    print("4. If issue is with one device try contacting the manufacturer\n")
    print("If none of this worked you can try troubleshooting through a PC or desktop, otherwise contact your ISP")
    import sys
    sys.exit()

elif lights == "N":
    print(" ")
print("If no lights are on check power to outlet")
cords = input("How many cables are plugged into modem/router? ")
if cords == "1":
    print("Check for other cables ")
    print("Here is an example cable placement: ")
    print("Power cord\n" + "Fiber Optic cord\n"> "Eth WAN\n" + "Eth to connect tv or device")
    print("Make sure all of the cables are secure and not loose. ")
elif cords == "2,3,4,5,6,7":
    print(" ")
    print("Make sure all of the cables are secure and not loose.")
    print("Continue")

print("Power cycle the modem/router by unplugging power cord for 30 seconds ")

print("NOTE: If you have a modem and router start with modem first")
print("NOTE: Some ISP Providers do not advise power cycling modem so you may want to check with them")
print("NOTE: Also keep in mind that if you hit the reset button it may reset to factory settings\n")

reboot = input("Have you unplugged the modem/router yet?\n" + "NOTE: Please reply with a CAPITOL Y or N: ")
if reboot == "Y":
    print("Please proceed to the next steps\n")
elif reboot == "N":
    print("Please power cycle modem/router by unplugging power cord for 30 seconds, then proceed.\n")

print("Most Fiber customers will have a battery backup")
print("An example of the lights on a battery backup would be as follows")
print("System Status: Green \n" + "Mute: Off \n" + "Battery: Off\n ")

print("NOTE: If the battery light is Green or Red, then the battery needs replaced. ")
print("NOTE: If the Mute light is on and making noise then simply unplug Battery Backup.")
print("NOTE: Some battery backups are located outside.\n ")

print("Now that the power cycle is complete it may take a couple minutes for the lights to come on")
