import requests, json

operator = "http://10.0.0.113:7070/ra-reveal"

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
        print("Error:", e)

