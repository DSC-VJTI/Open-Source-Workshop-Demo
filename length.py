import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inch-to-cm', type=float, dest="inch_to_cm")
parser.add_argument('--cm-to-inch', type=float, dest="cm_to_inch")
args = parser.parse_args()


def main():
    inch_to_cm_helper()
    cm_to_inch_helper()


# Helper functions to check if the arg exists or not
def inch_to_cm_helper():
    inch = args.inch_to_cm
    if (inch):
        inch_to_cm(inch)

def cm_to_inch_helper():
    cm = args.cm_to_inch
    if (cm):
        cm_to_inch(cm)


# Converter functions
def inch_to_cm(inch):
    print(f'{inch} inch in cm is: {inch*2.54}cm')


def cm_to_inch(cm):
    print(f'{cm}cm in inch is: {cm/2.54} inch')


if (__name__ == "__main__"):
    main()


# i didn't add any changes :>