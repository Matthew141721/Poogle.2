# This is my first Python project!
# This project is to help individuals (with Fiber) troubleshoot before calling their internet service provider.
print("Welcome to Fiber Internet Support. ")
name = input("Could I have your name please? ")
print("Hello " + name + ", thank you for contacting Fiber Internet Support.")
issue = input("How may I assist you? ")
# if statement for no internet
print("Okay!")
print("Let's start with a few troubleshooting steps. ")
print("Have you payed the internet bill? If yes then continue, if no then contact your internet service provider.")
# ftth needs to be .upper()
print("Note: If you payed bill on due date it may take a business day for ISP office to fix. ")
print("You can power cycle modem/router to resolve issue. ")


print("Great! Our next step would be to identify the lights on the modem/router \n")
print("Here is an example of correct light: \n" + "Power: Green \n" + "Broadband: Green \n" + "Service: Green ")
print("2.4/5ghz: Green \n")

lights = input("Do you have all solid lights? \n" + "NOTE: Please reply with a CAPITOL Y or N: ")
if lights == "Y":
    print("Continue to the next step")
    print("Now that you see no lights flashing or any lights that are Orange/Red ")
    print("If you cannot connect through an ethernet cable try a new cable or different ETH port")
    print("If the issue is with wireless devices try to power off device for 15 seconds")
    print("You can also go into network settings to delete and add the network back to device. ")
    print("If none of this worked you can try troubleshooting through a PC or desktop, otherwise contact your ISP")
    print("If issue is with one device try contacting the manufacturer ")
    import sys
    sys.exit()

elif lights == "N":
    print("If no lights are on check power to outlet")
cords = input("How many cables are plugged into modem/router? ")
if cords == "1":
    print("Check for some other cables ")
    print("Here is an example of some cables: ")
    print("Power cord\n" + "DSL/Phone > Eth WAN\n" + "Eth to connect tv or device")

print("Power cycle the modem/router by unplugging power cord for 30 seconds ")
print("NOTE: If you have a modem and router start with modem first")
print("Some ISP Providers do not advise power cycling modem so you may want to check with them")
print("Also keep in mind that if you hit the reset button it may reset to factory settings\n")

print("Most Fiber customers will have a battery backup")
print("An example of the lights on a battery backup would be as follows")
print("System Status: Green \n" + "Mute: Off \n" + "Battery: Off ")

print("If the battery is Green or Red, then the battery needs replaced. ")
print("If the Mute light is on and making noise then simply unplug Battery Backup.")

print("Now that the power cycle is complete it may take a couple minutes for the lights to come on")
