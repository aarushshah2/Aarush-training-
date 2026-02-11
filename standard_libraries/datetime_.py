from datetime import datetime, date, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M")) # Format: 2026-02-11 16:47

# timedelta - Date math
yesterday = now - timedelta(days=1)

# strptime - String to Object
date_obj = datetime.strptime("2026-01-01", "%Y-%m-%d")