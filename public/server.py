
from flask import Flask, render_template, jsonify
import threading
import serial
import time
import json

app = Flask(__name__)

# Replace 'COM3' with your Gateway's actual COM port if different
PORT = 'COM3'
BAUD = 115200

# Global dictionary to store the latest sensor readings from nodes
latest_telemetry = {
    "ESP_NODE_1": {"dist": 80.0, "temp": 24.5, "rain": 4095, "vib": 1.0},
    "ESP_NODE_2": {"dist": 120.0, "temp": 26.1, "rain": 4095, "vib": 0.8}
}

def read_serial():
    global latest_telemetry
    while True:
        try:
            ser = serial.Serial(PORT, BAUD, timeout=1)
            print(f"Connected to gateway on {PORT}")
            while True:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line.startswith("{") and line.endswith("}"):
                    try:
                        data = json.loads(line)
                        node_id = data.get("node_id") or data.get("node")
                        if node_id in latest_telemetry:
                            latest_telemetry[node_id] = data
                            print(f"Updated data for {node_id}: {data}")
                    except json.JSONDecodeError:
                        pass
        except Exception as e:
            print(f"Serial error: {e}. Reconnecting in 2 seconds...")
            time.sleep(2)

# Start serial reader in a background thread
serial_thread = threading.Thread(target=read_serial, daemon=True)
serial_thread.start()

@app.route('/')
def index():
    # This loads your original full HTML file from a 'templates' folder
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    return jsonify(latest_telemetry)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
