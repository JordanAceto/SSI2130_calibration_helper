import argparse
from math import log2

parser = argparse.ArgumentParser()

parser.add_argument(
    '--FA',
    type=float,
    required=True,
    help='the measured frequency with 1v of CV'
)

parser.add_argument(
    '--FB',
    type=float,
    required=True,
    help='the measured frequency with 5v of CV'
)

args = parser.parse_args()

FA = args.FA
FB = args.FB

# see the SSI2130 datasheet for explanation of the steps below
A = log2(FA)
B = log2(FB)

dy = B - A
dx = 5 - 1

I = A - dy/dx

T = I + 5

target_freq = 2**T

hf_target = 16*target_freq

print(f"Adjust the scale trimmer until the freq is: {target_freq:.6}Hz")
print("\nFor HF trim, now inject 9v into the CV input.")
print(f"Adjust the high frequency trim until the freq is: {hf_target:.6}Hz")
