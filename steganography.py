#-------------------------------------------------------------------------------
# Name:        steganography
# Purpose:     skrypt przygotowany na oboz ZZP Cieszyn'2018
#
# Author:      Wojciech
#
# Created:     2.07.2018
# Copyright:   (c) Wojciech 2018
# Licence:     Za darmo w celach edukacyjnych
#-------------------------------------------------------------------------------
filename_in = 'wiele.raw'
filename_out = 'wiele_code.raw'
plain_text = 'TAJNE'

with open(filename_in, 'rb') as raw_file:
    contents = bytearray(raw_file.read())

with open(filename_out, 'wb') as output_file:
    index_of_letter = 0
    index_of_bit = 7
    length_of_string = len(plain_text)
    for content in range(len(contents)):
        if (ord(plain_text[index_of_letter]) & 1 << index_of_bit):
            contents[content] = contents[content] | 0b00000001
        else:
            contents[content] = contents[content] & 0b11111110
        if (index_of_bit == 0):
            index_of_bit = 7
            index_of_letter += 1
            if (index_of_letter == length_of_string):
                index_of_letter = 0
        else:
            index_of_bit -=1
    output_file.write(bytearray(contents))