import datetime

while 1:

	doubleClick("1547277479115.png")
	
	if exists(Pattern("download_list.png").similar(0.80), 15):  
		click("download_list.png")
		
	if exists(Pattern("start_all.png").similar(0.80), 5):
		click("start_all.png")

	starttime = time.time()
	endtime = time.time()
	#for x in range(100/3):
	while (endtime - starttime) < 180:
		print(endtime - starttime)
#		print(datetime.datetime.now())
		sleep(1)
		if exists(Pattern("start.png").similar(0.80), 0):  # click all star button
			for start_btm in findAll("start.png"):
				click(start_btm)
			
		if exists(Pattern("free_use.png").similar(0.80), 0):
			print("yes find")
			click("free_use.png")
			
		if exists(Pattern("1547782392607.png").similar(0.80), 0): # free test stop
			print("break")
			sleep(10)
			break
		endtime = time.time()
	
	rightClick("1547277899953.png")
	click("exit_1.png")
	sleep(3)
	
	if exists(Pattern("exit_3.png").similar(0.80), 5):
		click("exit_2.png")
		sleep(3)
	





