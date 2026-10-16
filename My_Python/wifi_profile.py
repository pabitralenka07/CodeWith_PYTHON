import subprocess

hardware = subprocess.check_output(
    ["networksetup", "-listallhardwareports"],
    text=True
)

wifi_interface = None

lines = hardware.splitlines()

for i, line in enumerate(lines):
    if "Wi-Fi" in line and i + 1 < len(lines):
        if "Device:" in lines[i + 1]:
            wifi_interface = lines[i + 1].split(":")[1].strip()
            break

if wifi_interface is None:
    print("Wi-Fi interface not found.")
    exit()

print(f"Wi-Fi interface: {wifi_interface}")

result = subprocess.run(
    ["networksetup", "-listpreferredwirelessnetworks", wifi_interface],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("\nSaved Wi-Fi Networks:")
    print(result.stdout)
else:
    print("Could not retrieve Wi-Fi networks.")
    print(result.stderr)
    
    
    
    
    
# import subprocess

# profiles = subprocess.check_output(
#     "netsh wlan show profiles",
#     shell=True
# ).decode(errors="ignore")

# names = [
#     line.split(":", 1)[1].strip()
#     for line in profiles.splitlines()
#     if "All User Profile" in line
# ]

# for i, name in enumerate(names, 1):
#     print(f"[{i}] {name}")

# if not names:
#     print("No saved Wi-Fi profiles found.")
# else:
#     choice = int(input("\nChoose Wi-Fi number: "))

#     if 1 <= choice <= len(names):
#         wifi = names[choice - 1]
#         print(f"\nSelected Wi-Fi: {wifi}")
#     else:
#         print("Invalid Wi-Fi number.")