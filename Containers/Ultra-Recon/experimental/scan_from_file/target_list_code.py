# Run nmap command with targets.txtfile

import docker
from pathlib import Path
import sys

target_file = Path(sys.argv[1])
target_file_full_path = Path.resolve(target_file)
volume_string = [str(target_file_full_path) + ":" + "/targets.txt"]
# print(volume_string)

client = docker.from_env()

if Path.exists(target_file):
    nmap_scan = client.containers.run('sneakerhax/nmap-small', remove=True, command=["--unprivileged", "-iL", "/targets.txt"], volumes=volume_string)
    print(nmap_scan.decode())
else:
    print("[-] target file does not exist")
