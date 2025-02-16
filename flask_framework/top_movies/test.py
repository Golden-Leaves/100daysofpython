import os
import string
env_path = r"C:\Users\PC\Desktop\Programming\python_projects\100daysofpython\flask_framework\top_movies\.env"

# Manually load key-value pairs
with open(env_path, "r") as f:
    for line in f:
        key, value = line.strip().split("=", 1)
        os.environ[key] = value

# Test if it's available now
print(f"Access Token (Manual Load): {os.getenv('ACCESS_TOKEN')}")
print(string.ascii_lowercase)