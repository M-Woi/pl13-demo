def ips_between(start, end):

    start_octets = start.split('.')
    end_octets = end.split('.')
    # resultatem splita jest List of strings więc rzutowanie na ints
    int_start_octets = []
    int_end_octets = []

    for i in start_octets:
        int_start_octets.append(int(i))
    for i in end_octets:
        int_end_octets.append(int(i))

    # obliczenia na reprezentacji w integerach
    num_addresses = (int_end_octets[0] - int_start_octets[0]) * 256 ** 3
    num_addresses += (int_end_octets[1] - int_start_octets[1]) * 256 ** 2
    num_addresses += (int_end_octets[2] - int_start_octets[2]) * 256
    num_addresses += (int_end_octets[3] - int_start_octets[3])
    return num_addresses