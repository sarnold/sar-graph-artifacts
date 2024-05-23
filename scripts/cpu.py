#!/usr/bin/env python3
"""
Simple CPU utilization plot.
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
cpu_percent_usage = []
idle_percent = []


def generate_graph():
    with open('data/sa16-cpu.csv', 'r') as csvfile:
        data_source = csv.reader(csvfile, delimiter=';')
        hostname = None
        prev_total = 0
        prev_idle = 0
        for row in data_source:
            # hostname;interval;timestamp;CPU;%usr;%nice;%sys;%iowait;%steal;%irq;%soft;%guest;%gnice;%idle
            if 'CPU' in row[3] or 'RESTART' in row[3]:
                continue
            if row[0].startswith('#'):
                continue
            if hostname is None:
                hostname = row[0]
            a = datetime.strptime((row[2].split(' ')[1]),'%H:%M:%S')
            x.append((a))
            # CPU usage needs more calculation using deltas
            # idle = %idle + %iowait
            cpu_idle = float(row[7]) + float(row[13])
            # non_idle = %user + %nice + %system + %irq + %softirq + %steal
            non_idle = float(row[4]) + float(row[5]) + float(row[6]) + float(row[9]) + float(row[10]) + float(row[8])
            cpu_total = cpu_idle + non_idle
            cpu_delta = cpu_total - prev_total
            idle_delta = cpu_idle - prev_idle
            cpu_use = cpu_delta - idle_delta
            cpu_usage = (100 * cpu_use / cpu_delta)
            cpu_percent_usage.append(cpu_usage)
            idle_percent.append(100 * idle_delta / cpu_delta)

    plt.plot(x, np.asarray(idle_percent, float), label='% Idle', color='g', antialiased=True)
    plt.plot(x, np.asarray(cpu_percent_usage, float), label='% Used', color='r', antialiased=True)

    plt.xlabel('Time',fontstyle='italic')
    plt.ylabel('CPU used (%)',fontstyle='italic')
    plt.title(f'{hostname} CPU utilization')
    plt.grid(linewidth=0.4, antialiased=True)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fancybox=True, shadow=True)
    plt.autoscale(True)

    plt.savefig('out/cpu.png', bbox_inches='tight')


if __name__ == '__main__':
    generate_graph()
