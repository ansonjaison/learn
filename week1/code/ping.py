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