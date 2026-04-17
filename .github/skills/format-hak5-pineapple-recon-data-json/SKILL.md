---
name: format-hak5-pineapple-recon-data-json
description: 'Format and pretty-print Hak5 WiFi Pineapple recon JSON scan files for readability. Use when given a raw or minified recon scan JSON file exported from the WiFi Pineapple.'
argument-hint: 'Path to the recon scan JSON file to format'
---

# Format Hak5 Pineapple Recon

## When to Use
- When you have a raw or minified JSON file exported from the Hak5 WiFi Pineapple Pager
- When a recon scan JSON file is hard to read due to lack of formatting

## Procedure

1. Identify the target JSON file path from the user's request or active editor
2. Run the formatter script against the file:

```bash
python3 Hardware/Hak5/Wifi_Pineapple_Pager/format-hak5-recon-data-json.py <filename>
```

3. Confirm the file has been formatted in place with 2-space indentation

## Script

[format-hak5-recon-data-json.py](../../../Hardware/Hak5/Wifi_Pineapple_Pager/format-hak5-recon-data-json.py)

## Notes
- The script overwrites the input file in place
- Input must be valid JSON or the script will error
