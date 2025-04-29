import json
import tinytuya

class SmartDevice:
    def __init__(self, name, device_id, ip, key, version="3.3"):
        self.name = name
        self.device = tinytuya.OutletDevice(device_id, ip, key)
        self.device.set_version(float(version))

    def power_on(self):
        print(f"[+] Turning ON {self.name}")
        self.device.turn_on()

    def power_off(self):
        print(f"[-] Turning OFF {self.name}")
        self.device.turn_off()

class DeviceManager:
    def __init__(self, config_path='config.json'):
        with open(config_path) as f:
            config = json.load(f)
        self.devices = [
            SmartDevice(**dev) for dev in config.get('devices', [])
        ]

    def list_devices(self):
        for idx, dev in enumerate(self.devices):
            print(f"{idx+1}. {dev.name}")
        return self.devices

    def get_device(self, index):
        return self.devices[index]
