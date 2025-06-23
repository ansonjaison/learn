# Code

'''
import subprocess
with open("domains.txt") as file:
    domains = [line.strip() for line in file if line.strip()]
for domain in domains:
    print(f"\nPinging {domain}...")
    try:
        result = subprocess.run(
            ["ping", "-c", "2", domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print(f"{domain} is UP.")
        else:
            print(f"{domain} is DOWN.")
        if result.stdout:
            print(result.stdout.splitlines()[0])
    except subprocess.TimeoutExpired:
        print(f"Timeout: {domain} did not respond.")
    except Exception as e:
        print(f"Error: {e}")
'''

# domains.txt file

'''
github.com
unknowx.awd
discord.com
youtube.com
'''

# Output

'''
anson@DESKTOP-P49CESA:~/learn/week1/code$ python3 ping.py

Pinging github.com...
github.com is UP.
PING github.com (20.207.73.82) 56(84) bytes of data.

Pinging unknowx.awd...
unknowx.awd is DOWN.

Pinging discord.com...
discord.com is UP.
PING discord.com (162.159.138.232) 56(84) bytes of data.

Pinging youtube.com...
youtube.com is UP.
PING youtube.com (142.250.66.14) 56(84) bytes of data.
anson@DESKTOP-P49CESA:~/learn/week1/code$
'''