#!/usr/bin/python3
"""
boot vm notification.py

notifies my laptop of a vm being booted.


By: Calacuda | MIT License | Epoch: Feb 10, 2023
"""


import json
from requests import post
import argparse
from os.path import expanduser


parser = argparse.ArgumentParser(
    prog = 'vm boot notification',
    description = 'notifies my laptop of a proxmox vm being booted via a post request'
)
parser.add_argument('vmid', type=str)
parser.add_argument('phase', type=str)
args = parser.parse_args()
config_file = expanduser("/etc/pve-hooks/config.json")


def get_laptop_ip() -> str:
    """ returns the laptop ip from a config file. """
    with open(config_file, "r") as cfg:
        cfg_data = json.loads(cfg.read())
        return cfg_data.get("laptop_ip"), cfg_data.get("laptop_port")


def send_notif(vmid: str, vm_name: str, phase: str):
    """ sends a notification of a VM booting. """
    data = json.dumps({"vmid": vmid, "vm_name": vm_name, "phase": phase})
    ip, port = get_laptop_ip()
    url = f"http://{ip}:{port}"
    try:
        post(url, data = data, timeout = 5)
    except Exception as e:
        # log error to file in future
        with open("/etc/pve-hooks/errors.log", "a") as f:
            f.writelines(str(e))
            f.writelines("\n")


def get_vm_name(vmid: str) -> str:
    """ returns the name of the VM associated with vmid. """
    vms = {"106": "kali", "116": "shannon"}
    return vms.get(vmid)


def main():
    # if args.phase in ["post-start", "pre-start"]:
    # if args.phase == "post-start":
    name = get_vm_name(args.vmid)
    if name:
        send_notif(args.vmid, name, args.phase)


if __name__ == "__main__":
    main()