#!/usr/bin/env python3
"""
Author        :Julio Sanz
Website       :www.elarraydejota.com
Email         :juliojosesb@gmail.com
Description   :Generate RAM graph from ram.dat file
Dependencies  :Python 3.x, matplotlib
Usage         :python ram.py
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
# Memory data arrays
free_mem = []
used_mem = []
buffer_mem = []
cached_mem = []

# ======================
# FUNCTIONS
# ======================

def generate_graph():
    with open('data/sa09-ram.csv', 'r') as csvfile:
        data_source = csv.reader(csvfile, delimiter=';')
        hostname = None
        for row in data_source:
            if row[0].startswith('#'):
                continue
            if hostname is None:
                hostname = row[0]
            # [2] column is date-time
            # Convert to datetime data type
            a = datetime.strptime((row[2].split(' ')[1]),'%H:%M:%S')
            x.append((a))
            # The remaining columns contain data
            # 3:kbmemfree 5:kbmemused 7:kbbuffers 8:kbcached
            free_mem.append((int(row[3])/1024)+(int(row[7])/1024)+(int(row[8])/1024))
            used_mem.append((int(row[5])/1024))
            buffer_mem.append(int(row[7])/1024)
            cached_mem.append(int(row[8])/1024)

    # Plot lines
    plt.plot(x,free_mem, label='Free', color='g', antialiased=True)
    plt.plot(x,used_mem, label='Used', color='r', antialiased=True)
    plt.plot(x,buffer_mem, label='Buffer', color='b', antialiased=True)
    plt.plot(x,cached_mem, label='Cached', color='c', antialiased=True)

    # Graph properties
    plt.xlabel('Time',fontstyle='italic')
    plt.ylabel('Memory (MB)',fontstyle='italic')
    plt.title(f'{hostname} RAM usage graph')
    plt.grid(linewidth=0.4, antialiased=True)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fancybox=True, shadow=True)
    plt.autoscale(True)

    # Graph saved to PNG file
    plt.savefig('out/ram.png', bbox_inches='tight')
    #plt.show()

# ======================
# MAIN
# ======================

if __name__ == '__main__':
    generate_graph()
