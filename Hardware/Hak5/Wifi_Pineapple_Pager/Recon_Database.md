# Recon Database

Command for reading the recon.db

```bash
sqlite3 recon/recon.db
```

load recon database

```sql
.table
hak5              hostap_chalresp   scan            
handshake         hostap_client     ssid            
hostap_basic      hostap_handshake  wifi_device 
```

List all tables (current firmware 1.08-stable has the listed tables)

```sql
PRAGMA table_info(table_name);
```

List table column names

```sql
SELECT ssid FROM ssid WHERE TRIM(ssid) != '' AND UNICODE(ssid) != 160 AND UNICODE(ssid) !=10 AND UNICODE(ssid) !=13;
```

List captured ssids

```sql
select name from scan where TRIM(name) != '' AND UNICODE(name) != 160 AND UNICODE(name) !=10 AND UNICODE(name) !=13;
```

List captured clients (Probe requests)

```sql
SELECT DISTINCT ssid FROM ssid WHERE encryption = 0;
```

List open ssid (no encryption)


