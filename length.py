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

x = 12
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
#git merge --abort for aborting the merge in case of a conflict which we can't resolve now.
#revert is also a way of undoing changes.It is present in the remaining part of noon pdf.
#git rebase <branch_name> brings the base of the branch on the master branch.
#git rebase interactive helps in rebasing between specific commits.
#git remote and git remote -v 
#git remote add <any name> <url-of-remote>.git remote show origin
#We can multiple remote repositories from a single one.
#git remote rename <old name> <new name> for renaming a remote repository.
#For breaking the connection between the local repository and remote repository,use git remote remove origin/remote-forked
#Connection with a remote repository is necessary for using git push.
#git stash pull,git stash list


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