#Loops are structures used to repeat sections of code. THey are useful if you have to do the same thin g more than once or your establish

print("0")
print("1")
print("2")
print("3")
print("4")
print("******************************************************************************")
#This is counted loop. I want you to think about count, check change
#i = 0, 0 <5, TRUE - Run Loop
#i = 1, 1 <5, TRUE - Run Loop
#i = 2, 2 <5, TRUE - Run Loop
#i = 3, 3 <5, TRUE - Run Loop
#i = 4, 4 <5, TRUE - Run Loop
#i = 5, 5 <5, False - Exit and move on

for i in range(4,12,2):
	#Anything tabbed is considered the loop block
	print(i)

print("******************************************************************************")
#
# i = 2, 2 < 6 True print(2*2)
# i = 3, 3 < 6 True print(3*2)
# i = 4, 4 < 6 True print(4*2)
# i = 5, 5 < 6 True print(5*2)
# i = 6, 6 < 6 FALSE EXIT LOOP
#
#
for i in range(2,6,1):
	#Anything tabbed is considered the loop block
	print(i*2)

print("**********************************BACKWARDS***********************************")

for i in range(10,-1,-1):
	#Anything tabbed is considered the loop block
	print(i)

print("******************************************************************************")

print("MOVING ON")

print("*************************PRINTING STRING CHARACTERS***************************")
str = "Monkey!!!!!!!!"

for i in range(0, len(str), 1):
	print(str[i])



print("MOVING ON")

print("******************************************************************************")
str = "Monkey!!!!!!!!"

for i in range(len(str)-1, -1, -1):
	print(str[i])


print("***************PRINT EVERY SECOND LETTER IN STR START AT INDEX****************")
str = "Monkey!!!!!!!!"

for i in range(len(str)-1, -1, -1):
	print(str[i])

