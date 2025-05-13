import random
import time
from datetime import datetime

def generate_sensor_data():
    # Sıcaklık 15°C - 35°C arasında
    temperature = round(random.uniform(15.0, 35.0), 2)
    # Nem %30 - %90 arasında
    humidity = round(random.uniform(30.0, 90.0), 2)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity
    }

def main():
    print("Sensör simülasyonu başlatıldı...\n")
    try:
        while True:
            data = generate_sensor_data()
            print(f"[{data['timestamp']}] Sıcaklık: {data['temperature']}°C, Nem: {data['humidity']}%")
            time.sleep(2)  # Her 2 saniyede bir veri üret
    except KeyboardInterrupt:
        print("\nSimülasyon durduruldu.")

if __name__ == "__main__":
    main()
