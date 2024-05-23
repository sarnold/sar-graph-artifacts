#!/usr/bin/env python3
"""
Simple memory utilization plot (data as float).
"""

import csv
from datetime import datetime

import matplotlib.dates
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


plt.rcParams.update({'font.size': 8})
plt.rcParams['lines.linewidth'] = 0.5
time_format = matplotlib.dates.DateFormatter('%H:%M:%S')
plt.gca().xaxis.set_major_formatter(time_format)
plt.gcf().autofmt_xdate()

x = []
mem_used = []


def generate_graph():
    with open('data/sa16-ram.csv', 'r') as csvfile:
        data_source = csv.reader(csvfile, delimiter=';')
        hostname = None
        for row in data_source:
            # hostname;interval;timestamp;kbmemfree;kbavail;kbmemused;%memused;kbbuffers;kbcached ...
            if 'CPU' in row[3] or 'RESTART' in row[3]:
                continue
            if row[0].startswith('#'):
                continue
            if hostname is None:
                hostname = row[0]
            a = datetime.strptime((row[2].split(' ')[1]),'%H:%M:%S')
            x.append((a))
            # %memused
            mem_used.append(row[6])

    plt.plot(x, np.asarray(mem_used, float), label='% Used', color='g', antialiased=True)

    plt.xlabel('Time',fontstyle='italic')
    plt.ylabel('RAM used (%)',fontstyle='italic')
    plt.title(f'{hostname} Memory utilization')
    plt.grid(linewidth=0.4, antialiased=True)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fancybox=True, shadow=True)
    plt.autoscale(True)

    plt.savefig('out/ram.png', bbox_inches='tight')


if __name__ == '__main__':
    generate_graph()
