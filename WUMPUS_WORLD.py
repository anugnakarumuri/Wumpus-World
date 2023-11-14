title = 'WUMPUS WORLD'

print('Title		: ' + title)

#9=stench
#7=pit
#6=gold
#5=breeze
#-1=wumpus

def learnagent(world,i,j):
		'''Function for an agent to know which position contains which environment objects'''
		if (world[i][j]==9):											
			agi,agj=i,j
			print("\nNow the agent is at "+str(agi)+","+str(agj))
			print("You came across a stench")
			return agi,agj
		elif (world[i][j]==7):
			agi,agj=i,j
			print("\nNow the agent is at "+str(agi)+","+str(agj))
			print("You came across a pit")
			return -5,-5
		elif (world[i][j]==6):
			agi,agj=i,j
			print("\nNow the agent is at "+str(agi)+","+str(agj))
			print("You found glittering gold")
			print("You came across a stench")
			print("You feel breeze")
			return -4,-4
		elif (world[i][j]==5):
			agi,agj=i,j
			print("\nNow the agent is at "+str(agi)+","+str(agj))
			print("You feel breeze")
			return agi,agj
		elif (world[i][j]==-1):
			agi,agj=i,j
			print("\nNow the agent is at "+str(agi)+","+str(agj))
			print("You met wumpus")
			return -5,-5
		else:															#if world environment was empty
			agi,agj=i,j
			print("\nNow the agent is at "+str(agi)+","+str(agj))
			print("You are in safe zone")
			return agi,agj

def checkinp(agi,agj):
	'''Function for checking input going in forward direction to get gold'''
	if(agi==0 and agj==0):
		print("\nyou can go to 	"+str(agi+1)+"	"+str(agj))				#can move downward
		print("you can go to 	"+str(agi)+"	"+str(agj+1))			#can move right
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi+1 and agvj==agj or agvi==agi and agvj==agj+1):
			return agvi,agvj
		else:
			return -5
	elif(agi==3 and agj==0):
		print("\nyou can go to 	"+str(agi-1)+"	"+str(agj))				#can go upward
		print("you can go to 	"+str(agi)+"	"+str(agj+1))			#can go right
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi-1 and agvj==agj or agvi==agi and agvj==agj+1):
			return agvi,agvj
		else:
			return -5
	elif(agi==3 and agj==3):
		print("\nyou can go to 	"+str(agi-1)+"	"+str(agj))				#can go upward
		print("you can go to 	"+str(agi)+"	"+str(agj-1))			#can go left
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi-1 and agvj==agj or agvi==agi and agvj==agj-1):
			return agvi,agvj
		else:
			return -5
	elif(agi==0 and agj==3):
		print("\nyou can go to 	"+str(agi+1)+"	"+str(agj))				#can go downward
		print("you can go to 	"+str(agi)+"	"+str(agj-1))			#can go left
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi+1 and agvj==agj or agvi==agi and agvj==agj-1):
			return agvi,agvj
		else:
			return -5,-5
	elif(agi==1 and agj==0 or agi==2 and agj==0 or agi==3 and agj==0):
		print("\nyou can go to 	"+str(agi+1)+"	"+str(agj))				#can go upward
		print("you can go to 	"+str(agi)+"	"+str(agj+1))			#can move right
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi+1 and agvj==agj or agvi==agi and agvj==agj+1):
			return agvi,agvj
		else:
			return -5,-5
	elif(agi==0 and agj==3 or agi==1 and agj==3 or agi==2 and agj==3 or agi==3 and agj==3):
		print("you can go to 	"+str(agi+1)+"	"+str(agj))				#can go downward
		print("you can go to 	"+str(agi)+"	"+str(agj-1))			#can go left
		agvi=int(input("Enter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi+1 and agvj==agj or agvi==agi and agvj==agj-1):
			return agvi,agvj
		else:
			return -5,-5
	elif(agi==3 and agj==1 or agi==3 and agj==2 or agi==3 and agj==3):
		print("\nyou can go to 	"+str(agi)+"	"+str(agj+1))		#can go right
		print("you can go to 	"+str(agi)+"	"+str(agj-1))		#can go left
		print("you can go to 	"+str(agi-1)+"	"+str(agj))			#can move upward
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi and agvj==agj+1 or agvi==agi and agvj==agj-1 or agvi==agi-1 and agvj==agj):
			return agvi,agvj
		else:
			return -5,-5
	else:
		print("\nyou can go to 	"+str(agi)+"	"+str(agj+1))		#can go right
		print("you can go to	"+str(agi)+"	"+str(agj-1))		#can go left
		print("you can go to 	"+str(agi+1)+"	"+str(agj))			#can move downward
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi and agvj==agj+1 or agvi==agi and agvj==agj-1 or agvi==agi+1 and agvj==agj):
			return agvi,agvj
		else:
			return -5,-5

def checkinpreverse(agi,agj):
	'''Function for checking input going in reverse direction to get back to original position'''
	if(agi==0 and agj==3):
		print("you can go to 	"+str(agi)+"	"+str(agj-1))		#can go left
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi and agvj==agj-1):
			return agvi,agvj
		else:
			return -5,-5
	elif(agi==0 and agj==2 or agi==0 and agj==1):
		print("you can go to 	"+str(agi)+"	"+str(agj+1))		#can go right
		print("you can go to 	"+str(agi)+"	"+str(agj-1))		#can go left
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi and agvj==agj-1 or agvi==agi and agvj==agj+1 ):
			return agvi,agvj
		else:
			return -5,-5
	elif(agi==1 and agj==0 or agi==2 and agj==0):
		print("\nyou can go to 	"+str(agi-1)+"	"+str(agj))			#can go upward
		print("you can go to	"+str(agi)+"	"+str(agj+1))		#can move right
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi-1 and agvj==agj or agvi==agi and agvj==agj+1):
			return agvi,agvj
		else:
			return -5,-5
	elif(agi==1 and agj==3 or agi==2 and agj==3):
		print("you can go to 	"+str(agi-1)+"	"+str(agj))			#can go upward
		print("you can go to 	"+str(agi)+"	"+str(agj-1))		#can go left
		agvi=int(input("Enter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi-1 and agvj==agj or agvi==agi and agvj==agj-1):
			return agvi,agvj
		else:
			return -5,-5
	else:
		print("\nyou can go to	"+str(agi-1)+"	"+str(agj))			#can go upward
		print("you can go to 	"+str(agi)+"	"+str(agj-1))		#can go left
		print("you can go to 	"+str(agi)+"	"+str(agj+1))		#can go right
		agvi=int(input("\nEnter input for row => "))
		agvj=int(input("Enter input for column => "))
		if(agvi==agi-1 and agvj==agj or agvi==agi and agvj==agj-1 or agvi==agi and agvj==agj+1):
			return agvi,agvj
		else:
			return -5,-5

world=[	[0,5,7,5],
		[9,0,5,0],
		[-1,6,7,5],
		[9,0,5,7]	]			#declaration of a world

agi,agj=0,0						#initial agent position
print("\ninitially agent is at "+str(agi)+","+str(agj))
print("\nyou can go to 	"+str(agi+1)+"	"+str(agj))
print("you can go to 	"+str(agi)+"	"+str(agj+1))

agvi=int(input("Enter input for row => "))
agvj=int(input("Enter input for column => "))		#taking row and column values for the next move
if(agvi==1 and agvj==0 or agvi==0 and agvj==1):
	agi,agj=learnagent(world,agvi,agvj)				#if input valid calling learn agent function
else:
	print("Not valid")								
	 
while(agi>=0):
	agvi,agvj=checkinp(agi,agj)
	if(agvi!=-5 and agvj!=-5):
		agi,agj=learnagent(world,agvi,agvj)			
	else:
		print("\n Invalid input")

if(agi==-5):
	print("\nGAME OVER Sorry try next time!!!")
else:
	print("\nYou have unlocked next level move back to your initial position")	#acquired gold

	agi,agj=2,1													#implementation of reverse logic to reach the initial position

	while(agi>=0):
		agvi,agvj=checkinpreverse(agi,agj)
		if(agvi==0 and agvj==0):
			agi,agj=-4,-4
		elif(agvi!=-5 and agvj!=-5):
			agi,agj=learnagent(world,agvi,agvj)
		else:
			print("\nNot valid")

	if(agi==-5):
		print("\nYou were really close but unfortunately you failed!!! Try next time")
	else:
		print("\nCONGRATULATIONS,YOU WON!!!")
		
