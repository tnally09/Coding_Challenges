from typing import List


def count(data_dict_list: List[dict]):
    """
    Count the number of items of each name in the list of dictionaries

    Expected output:

    A: 3
    B: 2
    C: 4
    """

    # Store output as a dict of characters and their counts
    output = {}

    # Iterate through list of dicts created by provided code
    for i in range(len(data_dict_list)):
        # Check if key already exists for character in question
        # If exists, increment count by 1
        if output.get(data_dict_list[i]['name']):
            output[data_dict_list[i]['name']] += 1
        # If key does not exist, initialize it at count of 1
        else:
            output[data_dict_list[i]['name']] = 1

    return(output)



def main():
    data_dict_list = []

    for a_var in range(3):
        data_object = dict()
        data_object['name'] = 'A'
        data_object['value'] = a_var
        data_dict_list.append(data_object)

    for a_var in range(2):
        data_object = dict()
        data_object['name'] = 'B'
        data_object['value'] = a_var
        data_dict_list.append(data_object)

    for a_var in range(4):
        data_object = dict()
        data_object['name'] = 'C'
        data_object['value'] = a_var
        data_dict_list.append(data_object)

    return(count(data_dict_list))

    


if __name__ == '__main__':
    print(main())