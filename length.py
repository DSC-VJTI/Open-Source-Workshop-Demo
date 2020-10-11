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


if __name__ == "__main__":
    main()
#notes
#check commit
#git push origin --delete dsc(for deleting branch in remote repository)
#git checkout <branch_name> for changing from current active branch to that branch
#git push -u origin dsc for pushing new created branch of local repository to remote repository.
#For deleting a branch,come outside that branch.Then git branch -d (branch_name).
#git merge topic for fast forward merge.
#git checkout -b topic2 for creating a new branch.

# # args parser for cm to mm converter
# parser.add_argument('--cm-to-mm', type=float, dest="cm_to_mm")

# # helper function for checking args for cm_to_mm function
# def cm_to_mm_helper():
#     cm_mm = args.cm_to_mm
#     if (cm_mm):
#         cm_to_mm(cm_mm)

# # function to convert cm to mm
# def cm_to_mm(cm_mm):
#     print(f'{cm_mm}cm in mm is: {cm*10} mm')