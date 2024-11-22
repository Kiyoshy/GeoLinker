import serial, time

gps = serial.Serial("/dev/ttyACM0", baudrate=9600)

print(gps)

while True:
    line = gps.readline()
    line_str = line.decode('latin-1')
    # print(line_str)

    if "$GPRMC" in line_str:
        data = line_str.split(',')

        if data[2] == 'A':  # Signal is valid (A) or invalid (V)
            latitude = float(data[3][:2]) + float(data[3][2:]) / 60.0  # Convert to decimal format
            longitude = float(data[5][:3]) + float(data[5][3:]) / 60.0  # Convert to decimal format
            lat_direction = data[4]  # N o S
            long_direction = data[6]  # E o W
            
            # Set latitude and longitude direction
            if lat_direction == 'S':
                latitude = -latitude
            if long_direction == 'W':
                longitude = -longitude

            print("Latitude: {}{} Longitude: {}{}".format(latitude, lat_direction, longitude, long_direction))
            # Generate Google Maps URL
            map_url = f"https://www.google.com/maps?q={latitude},{longitude}"
            print("Google Maps URL:", map_url)
            time.sleep(2)
        else:
            print("Error: Invalid GPS signal")
