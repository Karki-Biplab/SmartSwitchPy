from device_manager import DeviceManager

def main():
    manager = DeviceManager()
    devices = manager.list_devices()

    choice = int(input("Select device number to toggle: ")) - 1
    device = manager.get_device(choice)

    action = input("Type 'on' to turn ON or 'off' to turn OFF: ").lower()
    if action == "on":
        device.power_on()
    elif action == "off":
        device.power_off()
    else:
        print("Invalid action")

if __name__ == "__main__":
    main()
