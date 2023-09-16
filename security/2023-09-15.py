#!/usr/bin/env python3

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

text='HQEOTFNMKPELTELUEZSIKTFYGSTNMEGNDGLPUJCHQWFEXFEEPRPGKZYEHHQVPSRGNYGYSLEDBRXLWKPEZMYPUEWLFGLESVRPGJLYQJGNYGYSLEXVWYPSRGFYKECFVXGFMVZEGKTLQOZELVIKSFYLXKHQWGILF'

digraphs = dict()

#count of digraphs

for i in range(len(text) - 7):
    digraphs[text[i:i+8]] = text.count(text[i:i+8])
    if digraphs[text[i:i+8]] > 1:
        print(i+1, text[i:i+8], digraphs[text[i:i+8]])

for i in range(len(text)):
    if i % 3 == 0:
        print(bcolors.OKBLUE + text[i], end='')
    elif i % 3 == 1:
        print(bcolors.OKGREEN + text[i], end='')
    else:
        print(bcolors.WARNING + text[i], end='')
print()
# position of each digraph

# for i in range(len(text) - 1):
#     print(i, text[i:i+2])