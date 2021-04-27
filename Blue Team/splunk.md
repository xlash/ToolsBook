# Find first occurences :
| stats earliest(time) as e_time by environment | eval c_time=strftime(e_time "%Y-%m-%d %H:%M:%S.%f" | table c_time, environment
