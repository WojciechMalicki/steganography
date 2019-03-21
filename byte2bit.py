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

def str2bits(data):
    out = ''
    for byte in data:
        out += '{:08b}'.format(ord(byte))
    return(out)

def dec2bits(data):
    return '{:08b}'.format(data)

def dec2hex(data):
    return '{:x}'.format(data)

def bit2dec(data):
    return '{:d}'.format(data)

def main():
    print(bit2dec(0b01000001))

if __name__ == '__main__':
    main()