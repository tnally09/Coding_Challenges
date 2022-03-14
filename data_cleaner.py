from typing import List


def clean_data(drive_list: List[dict]):
    """
    Clean issues in the data.

    SSD drives should have a speed of 50000
    SATA drives should have a speed of 5200 (if not provided)
    Fibre drives may be spelled Fiber

    Create a field in the drive for free_GiB (size_GiB - used_GiB)
    Create a field in the drive for free_percent (free_GiB / total_GiB)

    :param drive_list:
    :return:
    """
    
    # Iterate through list of dicts create by provided code
    # Each list index contains a dict of specific HD info
    for i in range(len(drive_list)):
        # Apply clean-up conditions for SSD, SATA, and fibre drives
        if drive_list[i]['type'] == 'SSD':
            drive_list[i]['speed'] = 50000
        if drive_list[i]['type'] == 'SATA':
            if not drive_list[i].get('speed'):
                drive_list[i]['speed'] = 5200
        if drive_list[i]['type'] == 'Fibre':
            drive_list[i]['ty]e'] = 'Fiber'
        # ASSUMPTION: Slot shows an error in drive size. Since 1000 GiB are
        # Used, assume that size_GiB is also 1000 GiB (b/c drive size cannot 
        # be 0)
        if drive_list[i]['size_GiB'] == 0:
            drive_list[i]['size_GiB'] = drive_list[i]['used_GiB']

        # Add requested fields (free_Gib and free_percent)
        drive_list[i]['free_GiB'] = drive_list[i]['size_GiB'] - drive_list[i]['used_GiB']
        drive_list[i]['free_percent'] = drive_list[i]['free_GiB']/drive_list[i]['size_GiB']
    
    return drive_list


def print_summary(drive_list: List[dict]):
    """
    Print the following information for the drives.

    Count of drives of each type (Fibre, SATA, SAS)

    Average free space (in GiB)
    Average free space (in percent)

    Weighted average latency (weighted by iops)

    :param drive_list:
    :return:
    """

    fibre_drive_count = 0
    sas_drive_count = 0
    sata_drive_count = 0
    average_free_space = 0
    average_free_space_percent = 0.0
    weighted_average_latency = 0.0

    for i in range(len(drive_list)):
        if drive_list[i]['type'] == 'Fiber' or drive_list[i]['type'] == 'Fibre':
            fibre_drive_count += 1
        if drive_list[i]['type'] == 'SSD':
            # Despite  not being explicitly named SSD, SAS is a type of solid
            # State drive
            sas_drive_count += 1
        if drive_list[i]['type'] == 'SATA':
            sata_drive_count += 1
        
        # Append to totals for averages
        average_free_space += drive_list[i]['free_GiB']
        average_free_space_percent += drive_list[i]['free_percent']
        # Since avg latency is specified as weighted by iops, multiply
        # The two figures together for weighted latency
        weighted_average_latency += drive_list[i]['iops'] * drive_list[i]['latency']

    # Take average once all totals are completed
    average_free_space = average_free_space/len(drive_list)
    average_free_space_percent = average_free_space_percent/len(drive_list)
    weighted_average_latency = weighted_average_latency/len(drive_list)
        

    print(f'Drive Count: Fibre {fibre_drive_count}  SATA {sata_drive_count}  SAS {sas_drive_count}')
    print(f'Average Free space (GiB): {average_free_space}')
    print(f'Average Free space (%): {average_free_space_percent}')
    print(f'Weighted average latency: {weighted_average_latency}')


def main():
    drive_list = []

    drive = dict()
    drive['slot'] = 1
    drive['speed'] = 10000
    drive['type'] = 'Fibre'
    drive['used_GiB'] = 824.37
    drive['size_GiB'] = 1000
    drive['iops'] = 999
    drive['latency'] = 3.9
    drive_list.append(drive)

    drive = dict()
    drive['slot'] = 2
    drive['speed'] = 10000
    drive['type'] = 'Fiber'
    drive['used_GiB'] = 987.52
    drive['size_GiB'] = 1000
    drive['iops'] = 12
    drive['latency'] = 45.2
    drive_list.append(drive)

    drive = dict()
    drive['slot'] = 3
    drive['speed'] = 10000
    drive['type'] = 'Fibre'
    drive['used_GiB'] = 216.9
    drive['size_GiB'] = 1000
    drive['iops'] = 2180
    drive['latency'] = 2.4
    drive_list.append(drive)

    drive = dict()
    drive['slot'] = 4
    drive['type'] = 'SSD'
    drive['used_GiB'] = 1000
    drive['size_GiB'] = 0
    drive['iops'] = 8560
    drive['latency'] = 1.4
    drive_list.append(drive)

    drive = dict()
    drive['slot'] = 5
    drive['type'] = 'SATA'
    drive['used_GiB'] = 685.39
    drive['size_GiB'] = 1000
    drive['iops'] = 3423
    drive['latency'] = 5.6
    drive_list.append(drive)

    drive = dict()
    drive['slot'] = 5
    drive['speed'] = 7200
    drive['type'] = 'SATA'
    drive['used_GiB'] = 685.39
    drive['size_GiB'] = 1000
    drive['iops'] = 240
    drive['latency'] = 5.8
    drive_list.append(drive)


    clean_data(drive_list)
    print(drive_list)
    print_summary(drive_list)


if __name__ == '__main__':
    main()