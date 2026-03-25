import ntcore
import socket
import time
#from ntcore impo'rt NetworkTables

ntKey = "key"
unityIP = "127.0.0.1"
unityPort = 5005
pollRate = 0.05

# As a client to connect to a robot
#NetworkTables.initialize(server='roborio-9477-frc.local')
nt = ntcore.NetworkTableInstance.getDefault()
#table = nt.GetTable("datatable")
nt.startClient4("unity-bridge")
nt.setServerTeam(9477)

voltage_entry = nt.getEntry(ntKey)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Connecting to robot NT server (team 9477)...")
print(f"Forwarding '{ntKey}' to {unityIP}:{unityPort} at {1/pollRate:.0f}Hz")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        voltage = voltage_entry.getDouble(0.0)
        message = f"voltage:{voltage:.2f}".encode()
        sock.sendto(message, (unityIP, unityPort))
        print(f"Sent: {message.decode()}", end="\r")
        time.sleep(pollRate)
    


except KeyboardInterrupt:
    print("\nStopped by user.")

finally: 
    sock.close()
    nt.stopClient()