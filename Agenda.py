print("* Loading most modules *")
import sys, pickle

Version = 0.3

print()

print("Loading time modules")
print()
import time
LocalTime = time.localtime()
print(LocalTime)

print()
print("* Loading agenda *")
print()

print("extracting info")
print()
try:
	AgendaInfo = pickle.load( open( "SaveInfo.p", "rb"))
except:
	AgendaInfo = []

print(AgendaInfo)

print("Version: " + str(Version))

while True:
	command = input("Command: ")
	if command == "/add":
		DueDate = input("(Day/Month/Year) Date:")
		if DueDate != "/exit":
			Homework = input("(Subject/Description) Homework: ")
			AgendaInfo.append(DueDate)
			AgendaInfo.append(Homework)

	if command == "/see":
		NUM = 0
		print("__________________________________________________________________________")
		print("""CALENDAR""")
		print("__________________________________________________________________________")
		for _ in range(0,int(len(AgendaInfo)/2)):
			print("DueDate: " + AgendaInfo[NUM])
			print("Description: " + AgendaInfo[NUM+1])
			NUM = NUM + 2
			print("__________________________________________________________________________")
		print("Debug way: " + str(AgendaInfo))
	if command == "/exit":
		pickle.dump(AgendaInfo, open( "SaveInfo.p", "wb" ))
		sys.exit()
	if command == "/save":
		pickle.dump(AgendaInfo, open( "SaveInfo.p", "wb" ))
	if command == "/remove":
		Number = 0
		print("-----------------------------")
		Counter = 0
		for _ in range(0,int(len(AgendaInfo)/2)):
			print(str(Counter + 1) + ". " + str(AgendaInfo[Number]) + " | Desc: " + str(AgendaInfo[Number+1]))
			Number = Number + 2
			Counter = Counter + 1
			print("-----------------------------")
		command = input("(Type cancel to cancel) Number you want to remove: ")
		if command != "cancel":
			if int(command) < int(len(AgendaInfo)/2+1):
				command = int(command)
				command -= 1
				command = command * 2
				AgendaInfo.pop(command)
				AgendaInfo.pop(command)
			else:
				print("NOT A VALID NUMBER")
	if command == "/options":
		print("__________________________________________________________________________")
		print("List: \"Agenda Info\"")
		print(AgendaInfo)
		print("__________________________________________________________________________")






sys.exit()