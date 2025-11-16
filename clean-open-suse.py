from getpass import getpass
from tqdm import tqdm

passwd = getpass("enter sudo pass: ")

debian_hosts = [
    # "misc",
    # "shannon",
    # "kube-ctl",
    # "jellyfin",
    # "misc",
    # "minecraft-admin",
    # "nextcloud",
    # "kali-pmx",
    # "rev-proxy",
    # "kali-ct",
    "pi-hole",
    "blade",
    "dew-drop",
]

from os import system

for host in tqdm(debian_hosts):
    # print(f'ssh {host} "echo \"{passwd}\" | sudo -S rm -f /etc/apt/sources.list.d/shells\*" ')
    # print()
    system(f'ssh {host} "echo \"{passwd}\" | sudo -S rm -f /etc/apt/sources.list.d/shells*" > /dev/null')
    system(f'ssh {host} "echo \"{passwd}\" | sudo -S rm -f /etc/apt/trusted.gpg.d/shells_zsh-us*" > /dev/null')
    system(f'ssh {host} "echo \"{passwd}\" | sudo -S apt update" > /dev/null')
