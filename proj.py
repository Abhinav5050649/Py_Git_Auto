import os

"""
Programmer: Abhinav Sharma
"""

#Method for local git related stuff
def local_git(path):
    str = ".git"
    if (str in os.listdir()):
        git_branch_checker()    #Checks for presence of branches
        README_Checker()
        git_add_commit_process()
        print("Committed successfully!")
        print("\n\n")
    else:
        os.system("git init")
        git_branch_checker()    #Check for presence of branches
        README_Checker()
        git_add_commit_process()
        print("Committed successfully!")
        print("\n\n")

#Method to check for presence of branches in local git repo and provides option to switch to different branch
def git_branch_checker():
    os.system("git branch")
    print()
    print("Based on above options, do you want to SWITCH to another branch, if one is present?")
    branch_op_checker = int(input("Enter 1 to SWITCH to another branch. Else, press 0:  "))

    if (branch_op_checker == 0):
        return ""
    else:
        branch_name = input("Enter name of branch: ")
        branch_change_statement = "git checkout " + branch_name
        os.system(branch_change_statement)
        return branch_name


#Checks for presence of a README.md file in the given directory and makes user create one if one not found
def README_Checker():
    files_list = os.listdir()
    if ("README.md" in files_list):
        return
    else:
        print("README.md not found!!! Please create one right now!!!")
        os.system("nano README.md")
        return


#method to check what operation user wants performed
def option():
    x = int(input("Enter 1 to git on system, 2 to push to remote repo:  "))
    return x    


#method for remote git repo related stuff
def remote_git(path):
    str = ".git"
    if (str in os.listdir()):
        os.system("git remote -v")
        print("\n\n")
        print("If you don't see any message, then it means that you haven't connected your local git repo to the remote repo on github.")
        print("\n\n")
        check_var = int(input("Press 2 if no message(s) were observed. Else, press 1:  "))
        print("\n\n")
        if (check_var == 1):
            README_Checker()
            branch_n = git_branch_checker()    #Check for presence of branches
            git_add_commit_process()
            push_branch_n = "git push --set-upstream origin " + branch_n
            os.system(push_branch_n)     #add feature for branch specific work
            print("Pushed successfully!")
            print("\n\n")
        else:
            print("\n\n")
            print("Ok. You will have to follow the documentation given on github.com for this purpose. Then, paste the ssh link on the terminal when prompted.")
            print("\n\n")
            link = input("Enter link:  ")
            ssh_link_for_remote_repo = "git -remote add origin " + link
            os.system(ssh_link_for_remote_repo)
            README_Checker()
            branch_n = git_branch_checker()
            git_add_commit_process()
            push_branch_n = "git push --set-upstream origin " + branch_n
            os.system(push_branch_n)    #add feature for branch specific work
            print("Pushed successfully!")
            print("\n\n")

#method for local commit    
def git_add_commit_process():
    #Add feature to check for README files as well
    number = int(input("Press 1 for limited number of files to be committed. Else, press 2:  "))

    if (number == 1):
        num_of_files = int(input("Enter number of files to commit: "))
        for i in range(num_of_files):
            file_name = input("Enter name of file(with extension): ")
            str_add_to_stage = "git add " + file_name  
            os.system(str_add_to_stage)    

        str_to_commmit = "git commit -m \"added new file(s)\""
        os.system(str_to_commmit)
    else:
        os.system("git add .")
        os.system("git commit -m \"added new files\"")


#main method
def main():
    print("Welcome to the Git Automation Script!\n\nProgrammer: Abhinav Sharma\n\n")
    print("Please enter proper file path!")
    path = input("Enter a path: ")
    print("\n\n")
    os.chdir(path)

    if (option() == 1):
        local_git(path)
    else:
        remote_git(path)

    print("\n\nThank you for using this script. Feel free to suggest any improvements that I can make in the code")

main()