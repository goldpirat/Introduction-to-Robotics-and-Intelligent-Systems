import serial
import matplotlib.pyplot as plt

# Set up serial connection
ser = serial.Serial('COM3', 9600)

def read_serial():
    if ser.in_waiting > 0:
        # Reads a line of data
        data = ser.readline().decode('utf-8').rstrip()
        return data
    return None

def plotmaker(distances):
    # Setting up the graph
    fig, ax = plt.subplots()
    ax.bar(['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4'], distances)
    ax.set_ylim(0, 200)
    ax.set_ylabel('Distance(cm)')
    ax.set_title('Readings from Ultrasonic Sensors')
    plt.show()

# Read data from the serial port
serial_data = read_serial()

if serial_data:
    # Parse the serial data
    # Splits the 4 measurements using
    readings = serial_data.split(',')
    distances = [float(dist) for dist in readings]  # String -> Float
    # Generate the plot
    plotmaker(distances)
else:
    print("****No data received. Check the serial connection.****")

# Close the serial connection
ser.close()
