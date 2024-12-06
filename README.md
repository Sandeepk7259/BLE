
# BLE Accelerometer Movement Detection

This project ingests accelerometer data from a BLE tag and determines if the tag is moving or stationary. The solution includes BLE scanning, data parsing, and movement detection, implemented in Python, and packaged using Docker.

---

## Features

- Scans BLE devices for accelerometer data.
- Detects whether the BLE tag is moving or stationary based on accelerometer readings.
- Handles exceptions for robustness.
- Dockerized for ease of deployment.

---

## Requirements

### Software
- Python 3.9+
- Docker (for containerized deployment)

### Hardware
- Laptop with a Bluetooth adapter.
- BLE tag with an accelerometer.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

### 4. Dockerized Setup
#### Build the Docker Image
```bash
docker-compose build
```

#### Run the Application
```bash
docker-compose up
```

---

## How It Works

1. **BLE Scanning:**
   The application scans for BLE devices and identifies the target BLE tag broadcasting accelerometer data.
   
2. **Data Parsing:**
   Raw BLE packets are parsed to extract accelerometer readings.

3. **Movement Detection:**
   The magnitude of accelerometer data is calculated to determine if the tag is moving or stationary.

4. **Threshold-based Detection:**
   - **Moving:** If magnitude exceeds a defined threshold.
   - **Stationary:** If magnitude is within the threshold.

---

## Code Structure

```
├── main.py            # Main script for BLE scanning and detection.
├── requirements.txt   # Python dependencies.
├── Dockerfile         # Docker image definition.
├── docker-compose.yml # Docker Compose configuration.
└── README.md          # Project documentation (this file).
```

---

## Example Output

When you run the script, it will display output similar to:

```
Scanning for BLE devices...
Device: BLE_Tag, Address: XX:XX:XX:XX:XX:XX
Device is stationary.
```

---

## Notes

- Adjust the `THRESHOLD` in `main.py` to fine-tune movement detection sensitivity.
- Ensure Bluetooth is enabled on your laptop.

---

## Troubleshooting

- **Bluetooth adapter not found:** 
  Check if your laptop's Bluetooth is enabled and accessible.
- **BLE tag not detected:**
  Ensure the BLE tag is powered on and broadcasting within range.

---

## Author

- **Your Name**
- Email: your.email@example.com

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
