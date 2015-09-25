import sys
import random

def subnet_calculator():
  masks = [255,254,252,248,240,224,192,128,0]
  mask_in_decimal_octets = [] 
  ipaddress_in_decimal_octets = [] 

  try:
    print "\n"

    while True:
      ip_address = raw_input("Enter an IP address: ")
      ipaddress_in_decimal_octets = ip = split_in_octets(ip_address)

      #print ip

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
      
      #print sm

      if (len(sm) == 4) and (int(sm[0]) == 255) and (int(sm[1]) in masks) and (int(sm[2]) in masks) and (int(sm[3]) in masks) and (int(sm[0]) >= int(sm[1]) >= int(sm[2]) >= int(sm[3])):
        break
      else:
        print "The Subnet Mask is invalid. Please retry!"
        continue

    mask_in_binary = "".join(decimal_to_bin_octet(subnet_mask))
    #print "Netmask in binary: " + mask_in_binary

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
    #print "Wildcard Mask: " + wildcard_mask
  
    ipaddress_in_binary = "".join(decimal_to_bin_octet(ip_address))
    #print "IP address in binary: " + ipaddress_in_binary

    # Get the network address and broadcast address
    network_address_in_binary = ipaddress_in_binary[:(number_of_ones)] + "0" * number_of_zeros
    #print "Network Address in binary: ", network_address_in_binary

    # Get the broadcast address and broadcast address
    broadcast_address_in_binary = ipaddress_in_binary[:(number_of_ones)] + "1" * number_of_zeros
    #print "Broadcast Address in binary: ",  broadcast_address_in_binary
    
    # Convert Network, Broadcast addresses from binary to decimal 
    network_address = ".".join(bin_to_decimal_octet(network_address_in_binary))
    broadcast_address = ".".join(bin_to_decimal_octet(broadcast_address_in_binary))

    print "\n\n"
    print "Network Address: %s" % network_address
    print "Broadcast Address: %s" % broadcast_address
    print "Wilcard mask: %s" % wildcard_mask
    print "Hosts per subnet: %s" % number_of_hosts
    print "Mask bits %s" % number_of_ones
    print "\n\n"

  # Generate a random IP address
    while True:
        ask_to_generate = raw_input("Do you wan to generate a random IP address from subnet? (y/n): ")
    
        if ask_to_generate == "y":
          random_ip_octets = generate_random_ipaddress(network_address, broadcast_address)
          random_ip_address = ".".join(random_ip_octets)
          print "\n"
          print "Random IP address: %s" % random_ip_address
          print "Network address: %s" % network_address
          print "Broadcast address: %s" % broadcast_address
          print "\n"
          continue
    
        else:
          print "Exiting...."
          break
    
  except KeyboardInterrupt: 
    print "\n\nProgram aborted by user. Exiting...\n"
    sys.exit()

def generate_random_ipaddress(network_address,broadcast_address):
  random_ip = []
  network_address_oct = network_address.split('.')
  broadcast_address_oct = broadcast_address.split('.')

  '''Random ip address octets will be same where broadcast address and network address octets are the same. 
  In the octets where network and broadcast addresses are different I use the random funtion to generate an integer between the values network address octet and the broadcast address octet. 
  '''
  for broadcast_index,broadcast_octet in enumerate(broadcast_address_oct):
   # print "broadcast: ",broadcast_index, broadcast_octet

    for net_index, net_octet in enumerate(network_address_oct):
    #  print "Network: ", net_index, net_octet

      if broadcast_index == net_index:
        if broadcast_octet == net_octet:
          random_ip.append(broadcast_octet)
        else:
          rand_octet = random.randint(int(net_octet), int(broadcast_octet))
          random_ip.append(str(rand_octet))

  return random_ip

def split_in_octets(string_octets):
  octets = string_octets.split('.')
  return octets

def bin_to_decimal_octet(octets_binary):
  address_in_octets = []
  address_in_decimal = []

  for octect in range(0,len(octets_binary), 8):
    address_octect = octets_binary[octect:octect+8]
    address_in_octets.append(address_octect)
    
  # convert octects in array from bin to decimal
  for bin_octet in address_in_octets:
    decimal_octet = str(int(bin_octet,2))
    address_in_decimal.append(decimal_octet) 

  return address_in_decimal

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
