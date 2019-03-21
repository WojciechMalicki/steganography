#-------------------------------------------------------------------------------
# Name:        steganography
# Purpose:     skrypt przygotowany na oboz ZZP Cieszyn'2018
#
# Author:      Wojciech
#
# Created:     5.07.2018
# Copyright:   (c) Wojciech 2018
# Licence:     Za darmo w celach edukacyjnych
#-------------------------------------------------------------------------------

filename_in = 'wiele_code.raw'
filename_out = 'message.txt'

with open(filename_in, 'rb') as raw_file:
    raw_data = bytearray(raw_file.read())

id_bit = 7
letter = 0

with open(filename_out, 'w') as plaintext_file:
    for data in range(len(raw_data)):
        if raw_data[data] % 2 == 1:
            letter += 2**id_bit
        id_bit -= 1
        if id_bit < 0:
            id_bit = 7
            plaintext_file.write(chr(letter))
            letter = 0