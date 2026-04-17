---
name: format-hak5-pineapple-recon-data-table
description: 'Display Hak5 WiFi Pineapple recon scan data as a formatted table. Use when given a recon scan JSON file exported from the WiFi Pineapple and you want to view APs in a readable table format.'
argument-hint: 'Path to the recon scan JSON file to display as a table'
---

# Format Hak5 Pineapple Recon Data Table

## When to Use
- When you have a recon scan JSON file from the Hak5 WiFi Pineapple and want a human-readable table
- When you want to view SSID, BSSID, channel, signal strength, WPS, and hidden status at a glance

## Procedure

1. Identify the target JSON file path from the user's request or active editor
2. Run the table script against the file:

```bash
python3 Hardware/Hak5/Wifi_Pineapple/format-hak5-recon-data-table.py <filename>
```

3. Output is printed to the terminal — it does not modify the file

## Script

[format-hak5-recon-data-table.py](../../../Hardware/Hak5/Wifi_Pineapple/format-hak5-recon-data-table.py)

## Notes
- The script reads the file but does not modify it
- Input must be valid Pineapple recon JSON with an `APResults` key
- Hidden networks are shown as `(hidden)` in the SSID column
