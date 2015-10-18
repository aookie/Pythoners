#!/usr/bin/python
# -*- coding: utf-8 -*-

# multi-line-decode.py
# input multi line URL-decoded file
# output multi line print
import fileinput
import sys
import urllib

def decode(input, is_show_log):
    decoded_list = []
    for index, line in enumerate(fileinput.input(input)):
        # TODO: Do you need some checks for URL encoded wordings?
        decoded = urllib.unquote(line)
        if(is_show_log == "1"):
            sys.stdout.write("[" + str(index) + "]" + " from:" + line)
            sys.stdout.write("[" + str(index) + "]" + " to  :" + decoded)
        decoded_list.append(decoded)
    return decoded_list

def output(output, list):
    with open(output, 'w') as fh:
        for line in list:
            fh.write(line)

if __name__ == "__main__":
    if(len(sys.argv) < 4):
        sys.stdout.write("Usage: input parameter insufficient.\n")
        sys.stdout.write(sys.argv[0] + " <input> <output> <is show log:0/1>")
        quit()

    sys.stdout.write(sys.argv[0] + "\n")
    sys.stdout.write("input       :" + sys.argv[1] + "\n")
    sys.stdout.write("output      :" + sys.argv[2] + "\n")
    sys.stdout.write("is show log :" + "show output" if sys.argv[3] == "1" else "no output")
    sys.stdout.write("\n")

    decoded_list = decode(sys.argv[1], sys.argv[3])

    output(sys.argv[2], decoded_list)
