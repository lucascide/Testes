### Executada primeiro

# #Run this prior to starting the exercise
# from random import randint as rnd

# memReg = 'members.txt'
# exReg = 'inactive.txt'
# fee =('yes','no')

# def genFiles(current,old):
#     with open(current,'w+') as writefile:
#         writefile.write('Membership No  Date Joined  Active  \n')
#         data = "{:^13}  {:<11}  {:<6}\n"

#         for rowno in range(20):
#             date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
#             writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


#     with open(old,'w+') as writefile:
#         writefile.write('Membership No  Date Joined  Active  \n')
#         data = "{:^13}  {:<11}  {:<6}\n"
#         for rowno in range(3):
#             date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
#             writefile.write(data.format(rnd(10000,99999),date,fee[1]))


# genFiles(memReg,exReg)



### Segunda parte do exercicio
# """
# The two arguments for this function are the files:
#     - currentMem: File containing list of current members
#     - exMem: File containing list of old members
    
#     This function should remove all rows from currentMem containing 'no' 
#     in the 'Active' column and appends them to exMem.
#     """


# def cleanFiles(currentMem, exMem):
#     # TODO: Open the currentMem file as in r+ mode
#     with open("./members.txt", "r+") as activeMembers:
#         # TODO: Open the exMem file in a+ mode
#         with open("./inactive.txt", "a+") as inactiveMembers:
#             # TODO: Read each member in the currentMem (1 member per row) file into a list.
#             # Hint: Recall that the first line in the file is the header.
#             activeMembers.readline()
#             listMembers = activeMembers.readlines()

#             # TODO: iterate through the members and create a new list of the innactive members
#             inactiveMembersList = []
#             activeMembersList = []

#             for member in listMembers:
#                 if "no" in member:
#                     inactiveMembersList.append(member)
#                 else:
#                     activeMembersList.append(member)

#             # Go to the beginning of the currentMem file
#             # TODO: Iterate through the members list.
#             # If a member is inactive, add them to exMem, otherwise write them into currentMem
#             activeMembers.seek(0, 0)
#             activeMembers.truncate()

#             activeMembers.write('Membership No  Date Joined  Active  \n')
            
#             for member in activeMembersList:    
#                 activeMembers.write(member)
#             for member in inactiveMembersList:
#                 inactiveMembers.write(member)

#     pass  # Remove this line when done implementation


# # The code below is to help you view the files.
# # Do not modify this code for this exercise.
# memReg = "members.txt"
# exReg = "inactive.txt"
# cleanFiles(memReg, exReg)


# headers = "Membership No  Date Joined  Active  \n"
# with open(memReg, "r") as readFile:
#     print("Active Members: \n\n")
#     print(readFile.read())

# with open(exReg, "r") as readFile:
#     print("Inactive Members: \n\n")
#     print(readFile.read())
