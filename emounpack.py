#!/usr/bin/env python2
# -*- coding: utf-8 -*-
 
"""

Emotet layer1 unpacker
Packer uses RC4 crypto with a modulo of 0x12296
Key seems to be located in either the .rdata or .data section

"""

import malduck
import sys

infile = sys.argv[1] 
mod = 0x12296

with open(infile, 'rb') as f:
	a = f.read()
	p = malduck.pe(data=a) 

# Custom RC4 taken from https://gist.github.com/sysopfb/19aa8e0bdecde60662b7adecdc72b11f
def decode_data(data, key, sz): 
    S = list(range(sz)) 
    S = [x&0xff for x in S] 
    j = 0 
    out = []
    for i in range(sz): 
        j = (j + S[i] + ord( key[i % len(key)] )) % sz 
        S[i] , S[j] = S[j] , S[i]
    i = j = 0 
    for char in data: 
        i = ( i + 1 ) % sz 
        j = ( j + S[i] ) % sz 
        S[i] , S[j] = S[j] , S[i] 
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % sz])) 
    return ''.join(out) 


def main():
	get_rsrc = p.resource('RT_RCDATA')
#	key = (p.section('.rdata').get_data()[5592:5626])
	key = (p.section('.data').get_data()[108:142]) + '\x00'
	b =  decode_data(get_rsrc, key, mod)
	with open('decrypted.pe', 'wb') as o:
		o.write(b)
		
		return 0
		
if __name__ == '__main__':
	main()
