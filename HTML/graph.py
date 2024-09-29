#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

# Path to the data file on the server
DATA_FILE_PATH = 'data.txt'

def main():
    print("Content-Type: image/png\n")

    try:
        # Read the data from the file
        with open(DATA_FILE_PATH, 'r') as file:
            data = file.read().strip().split()
            data = [float(i) for i in data]

        # Create a plot
        x = np.arange(len(data))
        y = np.array(data)

        plt.figure(figsize=(10, 5))
        plt.plot(x, y, marker='o')
        plt.title('Sample Data Plot')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)

        # Save the plot to a PNG image in memory
        img_data = BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)

        # Output the image data
        print(img_data.read())
        
    except Exception as e:
        print("Content-Type: text/html\n")
        print("<html>")
        print("<head>")
        print("<title>Error</title>")
        print("</head>")
        print("<body>")
        print(f"<h1>Error reading file</h1><p>{e}</p>")
        print("</body>")
        print("</html>")

if __name__ == "__main__":
    main()
