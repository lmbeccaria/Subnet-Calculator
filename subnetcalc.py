import sys

def subnet_calculator():
  masks = [255,254,252,248,240,224,192,128,0]
  mask_in_decimal_octets = [] 
  ipaddress_in_decimal_octets = [] 

  try:
    print "\n"

    while True:
      ip_address = raw_input("Enter an IP address: ")
      ipaddress_in_decimal_octets = ip = split_in_octets(ip_address)

      print ip

      if (len(ip) == 4) and \
          (1 <= int(ip[0]) <= 223) and \
          (int(ip[0]) != 127) and \
          (int(ip[0]) != 169 or int(a[1]) != 254) and \
          (0 <= int(ip[1]) <= 255 and 0 <= int(ip[2]) <= 255 and 0 <= int(ip[3]) <= 255):
        break

      else:
        print "The IP Address is invalid. Please retry\n"
        continue
      

    while True:
      subnet_mask = raw_input("Enter Subnet Mask: ")
      mask_in_decimal_octets = sm = split_in_octets(subnet_mask)
      
      print sm

      if (len(sm) == 4) and (int(sm[0]) == 255) and (int(sm[1]) in masks) and (int(sm[2]) in masks) and (int(sm[3]) in masks) and (int(sm[0]) >= int(sm[1]) >= int(sm[2]) >= int(sm[3])):
        break
      else:
        print "The Subnet Mask is invalid. Please retry!"
        continue

    mask_in_binary = "".join(decimal_to_bin_octet(subnet_mask))
    print "Netmask in binary: " + mask_in_binary

    # calculate the number of hosts in the the subnet
    number_of_zeros = mask_in_binary.count("0")
    number_of_ones = 32 - number_of_zeros
    number_of_hosts = abs(2**number_of_zeros - 2)

    # Get wildcard mask
    wildcard_octets = []
    for w in  mask_in_decimal_octets:
      w_octect = 255 - int(w)
      wildcard_octets.append(str(w_octect))

    wildcard_mask = ".".join(wildcard_octets)
    print "Wildcard Mask: " + wildcard_mask
  
    ipaddress_in_binary = "".join(decimal_to_bin_octet(ip_address)
    print "IP address in binary: " + ipaddress_in_binary

    # Get the network address and broadcast address
    network_address_in_binary = ipaddress_in_binary[:number_of_ones] + "0" * number_of_zeros
    print "Network Address in binary: " + network_address_in_binary

    # Get the broadcast address and broadcast address
    broadcast_address_in_binary = ipaddress_in_binary[:number_of_ones] + "0" * number_of_zeros
    print "Broadcast Address in binary: " + broadcast_address_in_binary

  except KeyboardInterrupt: 
    print "\n\nProgram aborted by user. Exiting...\n"
    sys.exit()


def split_in_octets(string_octets):
  octets = string_octets.split('.')
  return octets

def decimal_to_bin_octet(octets_decimal):
  octet_padded = []
  octets = octets_decimal.split('.')
  
  for octet_id in range(0,len(octets)):
    bin_octet = bin(int(octets[octet_id])).split('b')[1]

    if len(bin_octet) < 8:
      bin_octet = bin_octet.zfill(8)

    octet_padded.append(bin_octet)  

  return octet_padded

subnet_calculator()
