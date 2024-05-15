#!/usr/bin/env python3
"""
Author        :Julio Sanz
Website       :www.elarraydejota.com
Email         :juliojosesb@gmail.com
Description   :Generate CPU graph from cpu.dat file
Dependencies  :Python 3.x, matplotlib
Usage         :python cpu.py
License       :GPLv3
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import matplotlib.dates

# ======================
# VARIABLES
# ======================

# Aesthetic parameters
plt.rcParams.update({'font.size': 8})
plt.rcParams['lines.linewidth'] = 1.5
time_format = matplotlib.dates.DateFormatter('%H:%M:%S')
plt.gca().xaxis.set_major_formatter(time_format)
plt.gcf().autofmt_xdate()

# Time (column 0)
x = []
# Data arrays
cpu_usage = []
idle_cpu = []

# ======================
# FUNCTIONS
# ======================

def generate_graph():
    with open('data/sa09-cpu.csv', 'r') as csvfile:
        data_source = csv.reader(csvfile, delimiter=';')
        hostname = None
        for row in data_source:
            if 'CPU' in row[3]:
                continue
            if hostname is None:
                hostname = row[0]
            # [2] column is date-time
            # Convert to datetime data type
            a = datetime.strptime((row[2].split(' ')[1]),'%H:%M:%S')
            x.append((a))
            # The remaining columns contain data
            cpu_usage.append(row[4] + row[6])
            idle_cpu.append(row[13])

    # Plot lines
    plt.plot(x,cpu_usage, label='User %', color='r', antialiased=True)
    plt.plot(x,idle_cpu, label='Idle %', color='g', antialiased=True)

    # Graph properties
    plt.xlabel('Time',fontstyle='italic')
    plt.ylabel('CPU %',fontstyle='italic')
    plt.title(f'{hostname} CPU usage graph')
    plt.grid(linewidth=0.4, antialiased=True)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fancybox=True, shadow=True)
    plt.autoscale(True)

    # Graph saved to PNG file
    plt.savefig('out/cpu.png', bbox_inches='tight')
    #plt.show()

# ======================
# MAIN
# ======================

if __name__ == '__main__':
    generate_graph()
