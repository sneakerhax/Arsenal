# Recon Database

Command for reading the recon.db

```bash
sqlite3 recon/recon.db
```

load recon database

```sql
.table
```

List all tables

```sql
SELECT ssid FROM ssid WHERE TRIM(ssid) != '' AND UNICODE(ssid) != 160 AND UNICODE(ssid) !=10 AND UNICODE(ssid) !=13;
```

List captured ssids