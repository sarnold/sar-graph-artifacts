"""
Simple consumer test.
"""

from yaml_tools.utils import text_data_writer, text_file_reader

OPTS = {
    'file_encoding': 'utf-8',
    'output_format': 'yaml',
    'default_csv_hdr': None,
    'preserve_quotes': True,
    'mapping': 4,
    'sequence': 6,
    'offset': 4,
}

# read in some json sysstat data
data = text_file_reader('data/sa09-ram.json', OPTS)

# ret = text_data_writer(data, OPTS)

print(data['sysstat']['hosts'][0]['nodename'])
print(data['sysstat']['hosts'][0]['statistics'][0]['memory']['memused-percent'])

host_sz = data['sysstat']['hosts']
print(f"Size of hosts list: {len(host_sz)}")

stats_sz = data['sysstat']['hosts'][0]['statistics']
print(f"Size of stats list: {len(stats_sz)}")
