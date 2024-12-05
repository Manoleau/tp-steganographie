from scripts import decode, encode
import sys
n = int(sys.argv[1])
if len(sys.argv) == 4:
    filename = str(sys.argv[2])
    filename_res = str(sys.argv[3])
    decode(filename, filename_res, n)

elif len(sys.argv) == 5:
    mask = str(sys.argv[2])
    filename = str(sys.argv[3])
    filename_res = str(sys.argv[4])
    encode(mask, filename, filename_res, n)
