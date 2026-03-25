import socket
import time
import math

unityIP = "127.0.0.1"
unityPort = 5005
pollRate = 0.05

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Sending fake voltage to {unityIP}:{unityPort}")
print("Press Ctrl+C to stop.\n")

t = 0

try:
    while True:
        # Simulates voltage oscillating between 11.0 and 13.0
        voltage = 12.0 + math.sin(t) * 1.0
        message = f"voltage:{voltage:.2f}".encode()
        sock.sendto(message, (unityIP, unityPort))
        print(f"Sent: {message.decode()}", end="\r")
        t += pollRate
        time.sleep(pollRate)

except KeyboardInterrupt:
    print("\nStopped.")

finally:
    sock.close()