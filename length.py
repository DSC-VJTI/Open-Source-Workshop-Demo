#this file helps in interconverting between different units and scales of length
import argparse    

parser = argparse.ArgumentParser()
parser.add_argument('--inch-to-cm', type=float, dest="inch_to_cm")
parser.add_argument('--cm-to-inch', type=float, dest="cm_to_inch")
# args parser for cm to mm converter
parser.add_argument('--cm-to-mm', type=float, dest="cm_to_mm")
args = parser.parse_args()


def main():
    inch_to_cm_helper()
    cm_to_inch_helper()
    cm_to_mm_helper() 

# helper function for checking args for cm_to_mm function
def cm_to_mm_helper():
    cm_mm = args.cm_to_mm
    if (cm_mm):
        cm_to_mm(cm_mm)

# Helper functions to check if the arg exists or not
def inch_to_cm_helper():
    inch = args.inch_to_cm#
    if inch:
        inch_to_cm(inch)

def cm_to_inch_helper():
    cm = args.cm_to_inch
    if cm:
        cm_to_inch(cm)


# Converter functions
def inch_to_cm(inch):
    print(f'{inch} inch in cm is: {inch*2.54} cm')


def cm_to_inch(cm):
    print(f'{cm} cm in inch is: {cm/2.54} inch')

# function to convert cm to mm
def cm_to_mm(cm_mm):
    print(f'{cm_mm}cm in mm is: {cm_mm*10} mm')


if __name__ == "__main__":
    print("hello, welcome to the world of conversion")
    main()


# i did add some minor changes :>