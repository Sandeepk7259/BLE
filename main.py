
import asyncio
from bleak import BleakScanner

THRESHOLD = 0.1  # Movement detection threshold

def parse_accelerometer_data(data):
    """Extract accelerometer values from the raw BLE data."""
    # Example extraction based on frame definition
    # Assuming data is hex and accelerometer values are encoded in bytes 9-11
    accel_x = int.from_bytes(data[9:10], byteorder='little', signed=True)
    accel_y = int.from_bytes(data[10:11], byteorder='little', signed=True)
    accel_z = int.from_bytes(data[11:12], byteorder='little', signed=True)
    return accel_x, accel_y, accel_z

def calculate_magnitude(accel_data):
    """Calculate the vector magnitude of accelerometer data."""
    x, y, z = accel_data
    return (x**2 + y**2 + z**2)**0.5

async def main():
    print("Scanning for BLE devices...")
    scanner = BleakScanner()
    devices = await scanner.discover()

    for device in devices:
        print(f"Device: {device.name}, Address: {device.address}")
        # Assuming specific service data contains accelerometer info
        if device.name == "Target BLE Tag":
            raw_data = device.metadata.get("manufacturer_data")
            accel_data = parse_accelerometer_data(raw_data)
            magnitude = calculate_magnitude(accel_data)

            if magnitude > THRESHOLD:
                print("Device is moving.")
            else:
                print("Device is stationary.")

if __name__ == "__main__":
    asyncio.run(main())
