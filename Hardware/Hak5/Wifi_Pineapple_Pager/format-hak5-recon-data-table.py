import json
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <filename>")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    data = json.load(f)

header = f"{'SSID':<35} {'BSSID':<20} {'CH':>3} {'Signal':>7} {'WPS':>4} {'Hidden':>6}"
print(header)
print("-" * len(header))

for ap in data['APResults']:
    ssid = ap['ssid'] if ap['ssid'].strip() else '(hidden)'
    wps = 'Yes' if ap['wps'] else 'No'
    hidden = 'Yes' if ap['hidden'] else 'No'
    print(f"{ssid:<35} {ap['bssid']:<20} {ap['channel']:>3} {ap['signal']:>7} {wps:>4} {hidden:>6}")
