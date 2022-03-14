"""
Expected Output:
[{'number': 0, 'TX': '0', 'RX': '0'}, 
{'number': 1, 'TX': '0', 'RX': '0'}, 
{'number': 2, 'TX': '0', 'RX': '0'}, 
{'number': 3, 'TX': '0', 'RX': '0'}, 
{'number': 4, 'TX': '0', 'RX': '0'}, 
{'number': 5, 'TX': '14.8k', 'RX': '2.9k'}, 
{'number': 6, 'TX': '0', 'RX': '0'}, 
{'number': 7, 'TX': '8.7k', 'RX': '46.0k'}, 
{'number': 8, 'TX': '0', 'RX': '0'}, 
{'number': 9, 'TX': '0', 'RX': '0'}, 
{'number': 10, 'TX': '0', 'RX': '0'}, 
{'number': 11, 'TX': '0', 'RX': '0'}, 
{'number': 12, 'TX': '23.2k', 'RX': '24.1k'}, 
{'number': 13, 'TX': '45.9k', 'RX': '600'}, 
{'number': 14, 'TX': '0', 'RX': '0'}, 
{'number': 15, 'TX': '0', 'RX': '0'}, 
{'number': 16, 'TX': '0', 'RX': '0'}, 
{'number': 17, 'TX': '0', 'RX': '0'}, 
{'number': 18, 'TX': '0', 'RX': '0'}, 
{'number': 19, 'TX': '0', 'RX': '0'}, 
{'number': 20, 'TX': '0', 'RX': '0'}, 
{'number': 21, 'TX': '0', 'RX': '0'}, 
{'number': 22, 'TX': '0', 'RX': '0'}, 
{'number': 23, 'TX': '0', 'RX': '0'}]
"""

import re
import pprint
from typing import OrderedDict

text_to_parse = [
    '    0             1             2             3             4             5             6             7',
    '   TX     RX     TX     RX     TX     RX     TX     RX     TX     RX     TX     RX     TX     RX     TX     RX',
    '================================================================================================================',
    '   0      0      0      0      0      0      0      0      0      0     14.8k   2.9k   0      0      8.7k  46.0k',
    '',
    '    8             9            10            11            12            13            14            15',
    '   TX     RX     TX     RX     TX     RX     TX     RX     TX     RX     TX     RX     TX     RX     TX     RX',
    '================================================================================================================',
    '   0      0      0      0      0      0      0      0     23.2k  24.1k  45.9k 600      0      0      0      0',
    '',
    '   16            17            18            19            20            21            22            23',
    '   TX     RX     TX     RX     TX     RX     TX     RX     TX     RX     TX     RX     TX     RX     TX     RX',
    '================================================================================================================',
    '   0      0      0      0      0      0      0      0      0      0      0      0      0      0      0      0'
]


def main():
    port_data = []

    # Compile regex search pattern to find non-white space groups in
    # Provided input data
    search_pattern = re.compile(r"(\S+)")

    # Though the formatting of text_to_parse data above is formatted to
    # Show a "line" of data - each of those "lines" is composed of a
    # List index. Five "lines" makes up one stream of data, therefore 
    # Increment the for loop search by five each time
    for i in range(0, len(text_to_parse), 5):
        # Find all numbers in the first "line"
        numbers = re.findall(search_pattern, text_to_parse[i])
        # Find all values in the fourth "line"
        tx_rx_vals = re.findall(search_pattern, text_to_parse[i+3])

        # Populate a temp dict that is appended to port_data after each
        # Iteration
        for num, val in zip(numbers, range(0, len(tx_rx_vals), 2)):
            temp_idx = {}
            temp_idx['number'] = num
            temp_idx['TX'] = tx_rx_vals[val]
            temp_idx['RX'] = tx_rx_vals[val+1]

            port_data.append(temp_idx)

    # PrettyPrint not necessary, but provides cleaner output 
    # For human digestion
    pp = pprint.PrettyPrinter(indent=1, sort_dicts=False)
    pp.pprint(port_data)


if __name__ == '__main__':
    main()
