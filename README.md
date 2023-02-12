# Simple command line script for calibrating SSI2130 VCO chips

See the datasheet for an explanation: https://www.soundsemiconductor.com/downloads/ssi2130datasheet.pdf

The code is a straight mapping of the "Tuning Process" outlined in the datasheet.

Steps:
- Inject 1.000v into the VCO
- Turn the VCO frequency fairly low, somewhere around 30Hz ~ 100Hz 
- Measure the VCO frequency, this is FA
- Inject 5.000v into the VCO
- Measure the new VCO frequency, it is FB
- Run this script with the values for FA and FB that you just found
    - to run the example from the datasheet: `$python ssi2130_cal_helper.py --FA=30 --FB=522`
- Adjust the scale trim potentiometer until you read the frequency that the script tells you
- Don't touch any knobs or the CV input while you're doing this

You can also do the optional HF trim, the steps are:
- Starting from where we just left off above (don't change anything)
- Inject 9.000v into the CV input
- Adjust the High Freq trimmer until the high frequency target is reached

Once you're done with the above steps you can adjust the base frequency trimmer to taste
