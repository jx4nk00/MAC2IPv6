#!/usr/bin/python3
import sys

def hex2bin(hex_value):
	return "{0:08b}".format(int(hex_value, 16))

def bin2hex(bin_value):
	return hex(int(bin_value,2))[2:]

def change7pos(octet):
	invert = "0" if octet[6:7] =="1" else "1"
	newOctet = octet[:6]+invert+octet[7:]
	return newOctet

def makeIPv6(a_MAC):
	ipv6 = "fe80::"+"".join(["".join(a_MAC[i:i+2])+":" for i in range (0,7,2)])[:-1]
	return ipv6

def main():
    if len(sys.argv) != 2:
    	print("Uso: python3",sys.argv[0]," <MAC ADDRESS>")

    MAC = sys.argv[1]
    a_MAC = MAC.split(":")
    print("[*] MAC ADDRESS:",MAC)
    a_MAC.insert(3,"ff")
    a_MAC.insert(4,"fe")
    hex2bin_firstOctet = hex2bin(a_MAC[0])
    hex2bin_firstOctet_edited = change7pos(hex2bin_firstOctet)
    newFirstOctec =  bin2hex(hex2bin_firstOctet_edited)
    a_MAC[0] = newFirstOctec
    ipv6 = makeIPv6(a_MAC)
    print("[*] IPv6:",ipv6)


if __name__ == "__main__":
    main()
