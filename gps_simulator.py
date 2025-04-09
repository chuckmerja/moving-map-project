
# gps_simulator.py
import time
import serial
import random
import threading

# Configure the GPS simulator
PORT = '/dev/ttyUSB0'  # Change to your virtual port
BAUD = 9600
SIMULATION_INTERVAL = 1  # In seconds

# NMEA sentences for simulated GPS data
NMEA_SENTENCES = [
    "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47",  # GGA
    "$GPRMC,123519,A,4807.038,N,01131.000,E,000.0,054.7,230394,003.1,W*6A",  # RMC
    "$GPGSV,3,1,12,01,40,083,41,02,45,215,42,03,43,150,43,04,41,073,42*70"   # GSV
]

# Open serial port
ser = serial.Serial(PORT, BAUD, timeout=1)

def send_nmea_sentence():
    while True:
        sentence = random.choice(NMEA_SENTENCES)
        ser.write(sentence.encode('ascii') + b'\r\n')
        time.sleep(SIMULATION_INTERVAL)

# Run the simulator in a separate thread to simulate GPS data
thread = threading.Thread(target=send_nmea_sentence)
thread.daemon = True
thread.start()

print(f"GPS Simulator running on {PORT}...")
while True:
    time.sleep(1)  # Keep the main thread running
