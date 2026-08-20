import ntcore
import time
import math

ntKey = "key"
pollRate = 1.0

nt = ntcore.NetworkTableInstance.getDefault()
nt.startServer()

publisher = nt.getEntry(ntKey)

print(f"NT server running. Publishing fake voltage to '{ntKey}' at {1/pollRate:.0f}Hz")
print("Press Ctrl+C to stop.\n")

t = 0

try:
    while True:
        # Simulates voltage oscillating between 11.0 and 13.0
        voltage = 12.0 + math.sin(t) * 1.0
        publisher.setDouble(voltage)
        print(f"Published: {voltage:.2f}V", end="\r")
        t += pollRate
        time.sleep(pollRate)

except KeyboardInterrupt:
    print("\nStopped.")

finally:
    nt.stopServer()
