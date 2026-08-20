import ntcore
# import socket
import time
import requests
#from ntcore import NetworkTables

ntKey = "key"
# unityIP = "127.0.0.1"
# unityPort = 5005
pollRate = 1.0
SupabaseKey = "sb_publishable_67hmsdgmnRODEz3jC6n7Zw_AenHAPSj"
SupabaseUrl = "https://dagjewvtahsggbouguoa.supabase.co/rest/v1/VoltageLogs"
#APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzv0mDyHvPevYPxnvgQIzisyyUdjarHMYAi5okjCaI7r2kVVJxWK-TSF_E83Bzqvh9d/exec"

# As a client to connect to a robot
#NetworkTables.initialize(server='roborio-9477-frc.local')
nt = ntcore.NetworkTableInstance.getDefault()
#table = nt.GetTable("datatable")
nt.startClient4("unity-bridge")
nt.setServerTeam(9477)

voltage_entry = nt.getEntry(ntKey)

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Connecting to robot NT server (team 9477)...")
print(f"Logging '{ntKey}' to Google Sheets at {1/pollRate:.0f}Hz")
print("Press Ctrl+C to stop.\n")

# try:
#     while True:
#         voltage = voltage_entry.getDouble(0.0)
#         message = f"voltage:{voltage:.2f}".encode()
#         sock.sendto(message, (unityIP, unityPort))
#         print(f"Sent: {message.decode()}", end="\r")
#         time.sleep(pollRate)
# except KeyboardInterrupt:
#     print("\nStopped by user.")
# finally:
#     sock.close()
#     nt.stopClient()

try:
    while True:
        voltage = voltage_entry.getDouble(0.0)

        data = {
            "voltage": round(voltage, 2)
        }

        headers = {
            "apikey": SupabaseKey,
            "Authorization": f"Bearer {SupabaseKey}",
            "Content-Type": "application/json"
        }

        print(f"\nSending voltage: {voltage:.2f}V")

        try:
            response = requests.post(
                SupabaseUrl,
                json=data,
                headers=headers,
                timeout=5
            )

            print(
                f"Response: {response.status_code} | "
                f"{response.text}"
            )

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        time.sleep(pollRate)

except KeyboardInterrupt:
    print("\nStopped by user.")

finally:
    nt.stopClient()