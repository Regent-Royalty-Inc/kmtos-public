import requests
import json
import socket

# Dynamically resolve current host IP
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

OPERATOR_HOST = get_host_ip()
OPERATOR_PORT = 7070
operator = f"http://{OPERATOR_HOST}:{OPERATOR_PORT}/ra-reveal"

print("☉ KmtOS [public] >> Symbolic environment initializing...")
print("Continuum link established. Type commands below.\n")

while True:
    try:
        cmd = input("☉ KmtOS [public] >> ").strip()
        if cmd.lower() in ["exit", "quit"]:
            print("Exiting symbolic environment...")
            break
        if not cmd:
            continue
        payload = {"text": cmd}
        r = requests.post(operator, json=payload)
        print(json.dumps(r.json(), indent=2))
    except KeyboardInterrupt:
        print("\nExiting symbolic environment...")
        break
    except Exception as e:
        print(f"☉ KmtOS [public] >> Error: {e}")

