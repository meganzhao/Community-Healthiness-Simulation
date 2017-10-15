"""Simulates the spread of a disease in a community of 5000 people over a given number of days.
CS111, Winter 2016
"""


import random
import graphics

class Community:
	"""Creates a dictionary where the keys are ages from 0 to 99 and the values are lists of 
	two numbers."""
	def __init__(self):
		"""Constructor method for class Community"""
		self.masterDict = {}
		for i in range(100):
			self.masterDict[i] = [50,0]
		
	def setValue(self, key, newValue):
		"""Sets the value of a given key to be a new two-number list. key is an integer
		and newValue is a list."""
		self.masterDict[key] = newValue
		
	def getDict(self):
		"""Returns the entire dictionary."""
		return self.masterDict
		
		
class Simulation:
	"""Creates a Community object and a GraphicInterface object and then allows the
	simulation to be run."""
	
	def __init__(self):
		"""Constructor method for class Simulation. Chooses a random individual to be the
		first sick person and updates the dictionary."""
		self.firstPerson = random.randint(0,99)
		self.ourCommunity = Community()
		self.masterDict = self.ourCommunity.getDict()
		self.ourCommunity.setValue(self.firstPerson, [49,1])
		self.interface = GraphicInterface()
		
	def highProbSick(self, age):
		"""Returns health status of individual based on their age with a high probability
		of getting sick. age is an integer."""
		probability = random.random()
		if age <= 18 and probability < 0.25:
			return "sick"
		elif age >= 19 and age <= 60 and probability < 0.5:
			return "sick"
		elif age > 60 and probability < 0.75:
			return "sick"
		else:
			return "healthy"
	
	def lowProbSick(self, age):
		"""Returns health status of individual based on their age with a low probability
		of getting sick. age is an integer."""
		probability = random.random()
		if age <= 18 and probability < 0.1:
			return "sick"
		elif age >= 19 and age <= 60 and probability < 0.3:
			return "sick"
		elif age > 60 and probability < 0.5:
			return "sick"
		else:
			return "healthy"
			
	def highProbHealthy(self, age):
		"""Returns the health status of an individual based on their age with a high
		probability of getting well. age is an integer."""
		probability = random.random()
		if age <= 18 and probability < 0.1:
			return "sick"
		elif age >= 19 and age <= 60 and probability < 0.3:
			return "sick"
		elif age > 60 and probability < 0.5:
			return "sick"
		else:
			return "healthy"	
			
	def lowProbHealthy(self, age):
		"""Returns the health status of an individual based on their age with a high
		probability of getting well. age is an integer."""
		probability = random.random()
		if age <= 18 and probability < 0.25:
			return "sick"
		elif age >= 19 and age <= 60 and probability < 0.5:
			return "sick"
		elif age > 60 and probability < 0.75:
			return "sick"
		else:
			return "healthy"
			
	def goToSchool(self, prob):
		"""Generates a list of all children under 18 and then chooses a random selection
		to possibly be exposed to disease. If a sick person is present at school, each healthy
		child has a possibility of getting sick. Updates the masterDict with health statuses
		and also returns an updated list of children at school that day. prob is an integer
		(either 0 or 1)."""
		schoolList = []
		atSchoolList = []
		for key in self.masterDict:
			if key <= 18:
				value = self.masterDict[key]
				for i in range(value[0]):
					schoolList.append([key,"healthy"])
				for i in range(value[1]):
					schoolList.append([key,"sick"])
		# 950 is the number of children from 0 to 18
		numKid = random.randint(0,950)
		for i in range(numKid):
			randomIndex = random.randint(0, len(schoolList) - 1)
			atSchoolList.append(schoolList[randomIndex])
			# This ensures we won't choose the same child twice
			schoolList = schoolList[:randomIndex] + schoolList[randomIndex + 1:]
		numSick = 0
		for person in atSchoolList:
			if person[1] == "sick":
				numSick += 1
		# Children can only get sick if there is a sick person present that day
		if numSick > 0:
			for person in atSchoolList:
				if person[1] == "healthy":
					self.masterDict[person[0]][0] -= 1
					if prob == 1:
						result = self.highProbSick(person[0])
					else:
						result = self.lowProbSick(person[0])
					if result == "sick":
						self.masterDict[person[0]][1] += 1
						person[1] = "sick"
					else:
						self.masterDict[person[0]][0] += 1
		return atSchoolList
					
		
	def goToWork(self, prob):
		"""Generates a list of all adults between 19 and 60 and choose a random selection 
		to possibly be exposed to disease. If a sick person is present at work, each healhty 
		adult has a possibility of getting sick. Updates the masterDict with health statuses
		and also returns an updated list of adults at work that day. prob is an integer(either
		0 or 1)."""
		workList = []
		atWorkList = []
		for key in self.masterDict:
			if key > 18 and key <= 60:
				value = self.masterDict[key]
				for i in range(value[0]):
					workList.append([key,"healthy"])
				for i in range(value[1]):
					workList.append([key,"sick"])
		#2050 is the number of adults from 19 to 60
		numWork = random.randint(0,2050)
		for i in range(numWork):
			randomIndex = random.randint(0, len(workList) - 1)
			atWorkList.append(workList[randomIndex])
			workList = workList[:randomIndex] + workList[randomIndex + 1:]
		numSick = 0
		for person in atWorkList:
			if person[1] == "sick":
				numSick += 1
		if numSick > 0:
			for person in atWorkList:
				if person[1] == "healthy":
					self.masterDict[person[0]][0] -= 1
					if prob == 1:
						result = self.highProbSick(person[0])
					else:
						result = self.lowProbSick(person[0])
					if result == "sick":
						self.masterDict[person[0]][1] += 1
						person[1] = "sick"
					else:
						self.masterDict[person[0]][0] += 1
		return atWorkList
					
							
	def goToShop(self, prob):	
		"""Generates a list of all community members and choose a random selection to possibly 
		be exposed to disease. If a sick person is present at the shop, each healhty person 
		has a possibility of getting sick. Updates the masterDict with health statuses and 
		also returns an updated list of people at the shop that day. prob is an integer(either
		0 or 1)."""
		shopList = []
		atShopList = []
		for key in self.masterDict:
			value = self.masterDict[key]
			for i in range(value[0]):
				shopList.append([key,"healthy"])
			for i in range(value[1]):
				shopList.append([key,"sick"])
		#5000 is the number of community members.
		numShop = random.randint(0,5000)
		for i in range(numShop):
			randomIndex = random.randint(0, len(shopList) - 1)
			atShopList.append(shopList[randomIndex])
			shopList = shopList[:randomIndex] + shopList[randomIndex + 1:]
		numSick = 0
		for person in atShopList:
			if person[1] == "sick":
				numSick += 1
		if numSick > 0:
			for person in atShopList:
				if person[1] == "healthy":
					self.masterDict[person[0]][0] -= 1
					if prob == 1:
						result = self.highProbSick(person[0])
					else:
						result = self.lowProbSick(person[0])
					if result == "sick":
						self.masterDict[person[0]][1] += 1
						person[1] = "sick"
					else:
						self.masterDict[person[0]][0] += 1
		return atShopList
					
					
	def goToHospital(self, prob):
		"""Generates a list of all sick people and choose a random selection to possibly recover. 
		Updates the masterDict with health statuses and also returns an updated list of people 
		at the hospital that day. prob is an integer(either 0 or 1)."""
		sickList = []
		atHospitalList = []
		for key in self.masterDict:
			value = self.masterDict[key]
			for i in range(value[1]):
				sickList.append([key,"sick"])
		# The number of people who go to the hospital is dependent on the total number of
		# sick people.
		numHospital = random.randint(0, len(sickList))
		for i in range(numHospital):
			randomIndex = random.randint(0, len(sickList) - 1)
			atHospitalList.append(sickList[randomIndex])
			sickList = sickList[:randomIndex] + sickList[randomIndex + 1:]
		for person in atHospitalList:
			self.masterDict[person[0]][1] -= 1
			if prob == 1:
				result = self.highProbHealthy(person[0])
			else:
				result = self.lowProbHealthy(person[0])
			if result == "healthy":
				self.masterDict[person[0]][0] += 1
				person[1] = "healthy"
			else:
				self.masterDict[person[0]][1] += 1
		return atHospitalList
	
	def simulate(self, schoolProb, officeProb, shopProb, hospitalProb):
		"""Ask the user to input the number of days to simulate. Create the images in the
		window and simulate the given number of days, advancing a day when the user clicks.
		Continually update the infomation of the community. schoolProb, officeProb, shopProb
		and hospitalProb are integers (either 0 or 1). Closes when the given number of
		days is complete."""
		self.interface.drawDayString()
		days = int(input("How many days would you like to simulate? "))
		self.interface.dayString.undraw()
		self.interface.drawBackground()
		self.interface.drawSchool()
		self.interface.drawOffice()
		self.interface.drawShop()
		self.interface.drawHospital()
		self.interface.update(self.masterDict)
		self.interface.win.getMouse()
		while days > 0:
			self.interface.updateDay(days)
			atSchoolList = self.goToSchool(schoolProb)
			self.interface.schoolInfo(atSchoolList)
			atWorkList = self.goToWork(officeProb)
			self.interface.officeInfo(atWorkList)
			atShopList = self.goToShop(shopProb)
			self.interface.shopInfo(atShopList)
			atHospitalList = self.goToHospital(hospitalProb)
			self.interface.hospitalInfo(atHospitalList)
			self.interface.update(self.masterDict)
			self.interface.win.getMouse()
			# At the end of each day, the info about the community that day is undrawn.
			self.interface.schoolHealthy.undraw()
			self.interface.schoolSick.undraw()
			self.interface.schoolHealthyString.undraw()
			self.interface.schoolSickString.undraw()
			self.interface.officeHealthy.undraw()
			self.interface.officeSick.undraw()
			self.interface.officeHealthyString.undraw()
			self.interface.officeSickString.undraw()
			self.interface.hospitalHealthy.undraw()
			self.interface.hospitalSick.undraw()
			self.interface.hospitalHealthyString.undraw()
			self.interface.hospitalSickString.undraw()
			self.interface.shopHealthy.undraw()
			self.interface.shopSick.undraw()
			self.interface.shopHealthyString.undraw()
			self.interface.shopSickString.undraw()
			days -= 1
		self.interface.win.close()
			

class GraphicInterface:
	"""GraphicInterface is a graphical interface that creates the graphics for the simulation."""
	
	def __init__(self):
		"""Constructor method for GraphicsInterface that creates a window."""
		self.win = graphics.GraphWin("The Common Code", 800, 800)
		self.win.setCoords(0, 0, 800, 800)
		self.infoBox = None
		self.sickNumber = None
		self.healthyNumber = None
		self.dayBox = None
		self.dayString = None
		self.schoolHealthy = None
		self.schoolSick = None
		self.schoolHealthyString = None
		self.schoolSickString = None
		self.officeHealthy = None
		self.officeSick = None
		self.officeHealthyString = None
		self.officeSickString = None
		self.hospitalHealthy = None
		self.hospitalSick = None
		self.hospitalHealthyString = None
		self.hospitalSickString = None
		self.shopHealthy = None
		self.shopSick = None
		self.shopHealthyString = None
		self.shopSickString = None
	
	def update(self, masterDict):
		"""Count the total numbers of sick and healthy community members and display them 
		in the box. masterDict is a dictionary of community members."""
		# if objects (including text) are drawn onscreen, undraw them
		if self.infoBox:
			self.infoBox.undraw()
		if self.sickNumber:
			self.sickNumber.undraw()
		if self.healthyNumber:
			self.healthyNumber.undraw()
		self.infoBox = graphics.Rectangle(graphics.Point(600, 650), graphics.Point(750, 750))
		self.infoBox.setFill("purple4")
		numHealthy = 0
		numSick = 0
		for key in masterDict:
			numHealthy += masterDict[key][0]
			numSick += masterDict[key][1]
		self.healthyNumber = graphics.Text(graphics.Point(675, 725),"HEALTHY:" + str(numHealthy))
		self.sickNumber = graphics.Text(graphics.Point(675, 675),"SICK:" + str(numSick))
		self.healthyNumber.setSize(20)
		self.sickNumber.setSize(20)
		self.healthyNumber.setStyle("bold")
		self.sickNumber.setStyle("bold")
		self.healthyNumber.setFill("white")
		self.sickNumber.setFill("white")
		self.infoBox.draw(self.win)
		self.healthyNumber.draw(self.win)
		self.sickNumber.draw(self.win)
	
	def updateDay(self, day):
		"""Display the current day in the box. day is an integer"""
		if self.dayBox:
			self.dayBox.undraw()
		if self.dayString:
			self.dayString.undraw()
		self.dayBox = graphics.Rectangle(graphics.Point(625, 525), graphics.Point(725, 625))
		self.dayString = graphics.Text(graphics.Point(675, 575),"DAY: " + str(day))
		self.dayBox.setFill("purple4")
		self.dayString.setSize(26)
		self.dayString.setStyle("bold")
		self.dayString.setFill("white")
		self.dayBox.draw(self.win)
		self.dayString.draw(self.win)
		
	def drawDayString(self):
		"""Display text when the user is asked to input the number of day for the simulation."""
		self.dayString = graphics.Text(graphics.Point(400, 400), "Please input in Terminal \n how many days you would \n like to simulate.")
		self.dayString.setSize(36)
		self.dayString.setStyle("bold")
		self.dayString.setFill("purple4")
		self.dayString.draw(self.win)
		
	def drawBackground(self):
		"""Draw the background image of a map"""
		self.background = graphics.Image(graphics.Point(400,400),"img/map1.gif")
		self.background.draw(self.win)
	
	def drawSchool(self):
		"""Draw the image of a school"""
		self.school = graphics.Image(graphics.Point(600, 150), "img/school.gif")
		self.school.draw(self.win)
		
	def drawHospital(self):
		"""Draw the image of a hospital"""
		self.hospital = graphics.Image(graphics.Point(200, 630), "img/hospital.gif")
		self.hospital.draw(self.win)
		
	def drawShop(self):
		"""Draw the image of a shop"""
		self.shop = graphics.Image(graphics.Point(400, 400), "img/shop.gif")
		self.shop.draw(self.win)
		
	def drawOffice(self):
		"""Draw the image of an office"""
		self.office = graphics.Image(graphics.Point(200, 150), "img/office.gif")
		self.office.draw(self.win)
		
	def schoolInfo(self, atSchoolList):
		"""Display the numbers of healthy and sick people at school that day. atSchoolList 
		is a list of community members at school after goToSchool has been run."""
		numHealthy = 0
		numSick = 0
		for person in atSchoolList:
			if person[1] == "healthy":
				numHealthy += 1
			else:
				numSick += 1
		self.schoolHealthy = graphics.Rectangle(graphics.Point(470, 270), graphics.Point(590, 310))
		self.schoolSick = graphics.Rectangle(graphics.Point(610, 270), graphics.Point(730, 310))
		self.schoolHealthy.setFill("purple4")
		self.schoolSick.setFill("purple4")
		self.schoolHealthyString = graphics.Text(graphics.Point(530, 290),"Healthy: " + str(numHealthy))
		self.schoolSickString = graphics.Text(graphics.Point(670, 290),"Sick: " + str(numSick))
		self.schoolHealthyString.setStyle("bold")
		self.schoolHealthyString.setSize(18)
		self.schoolHealthyString.setFill("white")
		self.schoolSickString.setStyle("bold")
		self.schoolSickString.setSize(18)
		self.schoolSickString.setFill("white")
		self.schoolHealthy.draw(self.win)
		self.schoolSick.draw(self.win)
		self.schoolHealthyString.draw(self.win)
		self.schoolSickString.draw(self.win)
	
	def officeInfo(self, atWorkList):
		"""Display the numbers of healthey and sick people at office that day. atWorkList 
		is a list of community members at office after goToWork has been run."""
		numHealthy = 0
		numSick = 0
		for person in atWorkList:
			if person[1] == "healthy":
				numHealthy += 1
			else:
				numSick += 1
		self.officeHealthy = graphics.Rectangle(graphics.Point(70, 270), graphics.Point(190, 310))
		self.officeSick = graphics.Rectangle(graphics.Point(210, 270), graphics.Point(330, 310))
		self.officeHealthy.setFill("purple4")
		self.officeSick.setFill("purple4")
		self.officeHealthyString = graphics.Text(graphics.Point(130, 290),"Healthy: " + str(numHealthy))
		self.officeSickString = graphics.Text(graphics.Point(270, 290),"Sick: " + str(numSick))
		self.officeHealthyString.setStyle("bold")
		self.officeHealthyString.setSize(18)
		self.officeHealthyString.setFill("white")
		self.officeSickString.setStyle("bold")
		self.officeSickString.setSize(18)
		self.officeSickString.setFill("white")
		self.officeHealthy.draw(self.win)
		self.officeSick.draw(self.win)
		self.officeHealthyString.draw(self.win)
		self.officeSickString.draw(self.win)
		
	
	def hospitalInfo(self, atHospitalList):
		"""Display the numbers of healthy and sick people at hospital that day. atHospitalList
		is a list of community members at hospital after goToHospital has been run."""
		numHealthy = 0
		numSick = 0
		for person in atHospitalList:
			if person[1] == "healthy":
				numHealthy += 1
			else:
				numSick += 1
		self.hospitalHealthy = graphics.Rectangle(graphics.Point(70, 750), graphics.Point(190, 790))
		self.hospitalSick = graphics.Rectangle(graphics.Point(210, 750), graphics.Point(330, 790))
		self.hospitalHealthy.setFill("purple4")
		self.hospitalSick.setFill("purple4")
		self.hospitalHealthyString = graphics.Text(graphics.Point(130, 770),"Healthy: " + str(numHealthy))
		self.hospitalSickString = graphics.Text(graphics.Point(270, 770),"Sick: " + str(numSick))
		self.hospitalHealthyString.setStyle("bold")
		self.hospitalHealthyString.setSize(18)
		self.hospitalHealthyString.setFill("white")
		self.hospitalSickString.setStyle("bold")
		self.hospitalSickString.setSize(18)
		self.hospitalSickString.setFill("white")
		self.hospitalHealthy.draw(self.win)
		self.hospitalSick.draw(self.win)
		self.hospitalHealthyString.draw(self.win)
		self.hospitalSickString.draw(self.win)
		
	def shopInfo(self, atShopList):
		"""Display the numbers of healthy and sick people at shop that day. atShopList is 
		a list of community members at shop after goToShop has been run."""
		numHealthy = 0
		numSick = 0
		for person in atShopList:
			if person[1] == "healthy":
				numHealthy += 1
			else:
				numSick += 1
		self.shopHealthy = graphics.Rectangle(graphics.Point(270, 500), graphics.Point(390, 540))
		self.shopSick = graphics.Rectangle(graphics.Point(410, 500), graphics.Point(530, 540))
		self.shopHealthy.setFill("purple4")
		self.shopSick.setFill("purple4")
		self.shopHealthyString = graphics.Text(graphics.Point(330, 520),"Healthy: " + str(numHealthy))
		self.shopSickString = graphics.Text(graphics.Point(470, 520),"Sick: " + str(numSick))
		self.shopHealthyString.setStyle("bold")
		self.shopHealthyString.setSize(18)
		self.shopHealthyString.setFill("white")
		self.shopSickString.setStyle("bold")
		self.shopSickString.setSize(18)
		self.shopSickString.setFill("white")
		self.shopHealthy.draw(self.win)
		self.shopSick.draw(self.win)
		self.shopHealthyString.draw(self.win)
		self.shopSickString.draw(self.win)
		
	def introScreen(self):
		"""Create a window."""
		self.introScreen = graphics.GraphWin("The Common Code", 800, 800)
		self.introScreen.setCoords(0, 0, 800, 800)
		self.background = graphics.Image(graphics.Point(400, 500), "img/map.gif")
		self.background.draw(self.introScreen)
		self.baseString = graphics.Text(graphics.Point(400, 100),"Please select the probability of getting sick for the school, \nthe office, and the shop, and the probability of recovery for \nthe hospital. Probability is based on age.")
		self.baseString.setStyle("bold")
		self.baseString.setSize(26)
		self.baseString.draw(self.introScreen)
		
	def schoolButton(self):
		"""Create two buttons that allow the user to select the probability of children getting
		sick at school during the simulation."""
		self.schoolString = graphics.Text(graphics.Point(200,400),"SCHOOL")
		self.schoolString.setSize(36)
		self.schoolString.setStyle("bold")
		self.schoolString.setFill("purple4")
		self.schoolLowButton = graphics.Rectangle(graphics.Point(75,350),graphics.Point(175,300))
		self.schoolLowButton.setFill("purple4")
		self.schoolLowString = graphics.Text(graphics.Point(125,325),"LOW")
		self.schoolLowString.setSize(26)
		self.schoolLowString.setFill("white")
		self.schoolHighButton = graphics.Rectangle(graphics.Point(225,350),graphics.Point(325,300))
		self.schoolHighButton.setFill("purple4")
		self.schoolHighString = graphics.Text(graphics.Point(275,325),"HIGH")
		self.schoolHighString.setSize(26)
		self.schoolHighString.setFill("white")
		self.schoolString.draw(self.introScreen)
		self.schoolLowButton.draw(self.introScreen)
		self.schoolLowString.draw(self.introScreen)
		self.schoolHighButton.draw(self.introScreen)
		self.schoolHighString.draw(self.introScreen)
		self.schoolClick = self.introScreen.getMouse()
		while self.schoolClick.getX() < 75 or self.schoolClick.getX() > 175 and self.schoolClick.getX() < 225 or self.schoolClick.getX() > 325 or self.schoolClick.getY() < 300 or self.schoolClick.getY() > 350:
			self.schoolClick = self.introScreen.getMouse()
		if self.schoolClick.getX() < 200:
			return 0
		else:
			return 1
	
	def officeButton(self):
		"""Create two buttons that allow the user to select the probability of adults getting
		sick at office during the simulation."""
		self.officeString = graphics.Text(graphics.Point(600,400),"OFFICE")
		self.officeString.setSize(36)
		self.officeString.setStyle("bold")
		self.officeString.setFill("purple4")
		self.officeLowButton = graphics.Rectangle(graphics.Point(475,350),graphics.Point(575,300))
		self.officeLowButton.setFill("purple4")
		self.officeLowString = graphics.Text(graphics.Point(525,325),"LOW")
		self.officeLowString.setSize(26)
		self.officeLowString.setFill("white")
		self.officeHighButton = graphics.Rectangle(graphics.Point(625,350),graphics.Point(725,300))
		self.officeHighButton.setFill("purple4")
		self.officeHighString = graphics.Text(graphics.Point(675,325),"HIGH")
		self.officeHighString.setSize(26)
		self.officeHighString.setFill("white")
		self.officeString.draw(self.introScreen)
		self.officeLowButton.draw(self.introScreen)
		self.officeLowString.draw(self.introScreen)
		self.officeHighButton.draw(self.introScreen)
		self.officeHighString.draw(self.introScreen)
		self.officeClick = self.introScreen.getMouse()
		while self.officeClick.getX() < 475 or self.officeClick.getX() > 575 and self.officeClick.getX() < 625 or self.officeClick.getX() > 725 or self.officeClick.getY() < 300 or self.officeClick.getY() > 350:
			self.officeClick = self.introScreen.getMouse()
		if self.officeClick.getX() < 600:
			return 0
		else:
			return 1
			
	def shopButton(self):
		"""Create two buttons that allow the user to select the probability of people getting
		sick at shop during the simulation."""
		self.shopString = graphics.Text(graphics.Point(200,700),"SHOP")
		self.shopString.setSize(36)
		self.shopString.setStyle("bold")
		self.shopString.setFill("purple4")
		self.shopLowButton = graphics.Rectangle(graphics.Point(75,650),graphics.Point(175,600))
		self.shopLowButton.setFill("purple4")
		self.shopLowString = graphics.Text(graphics.Point(125,625),"LOW")
		self.shopLowString.setSize(26)
		self.shopLowString.setFill("white")
		self.shopHighButton = graphics.Rectangle(graphics.Point(225,650),graphics.Point(325,600))
		self.shopHighButton.setFill("purple4")
		self.shopHighString = graphics.Text(graphics.Point(275,625),"HIGH")
		self.shopHighString.setFill("white")
		self.shopHighString.setSize(26)
		self.shopString.draw(self.introScreen)
		self.shopLowButton.draw(self.introScreen)
		self.shopLowString.draw(self.introScreen)
		self.shopHighButton.draw(self.introScreen)
		self.shopHighString.draw(self.introScreen)
		self.shopClick = self.introScreen.getMouse()
		while self.shopClick.getX() < 75 or self.shopClick.getX() > 175 and self.shopClick.getX() < 225 or self.shopClick.getX() > 325 or self.shopClick.getY() < 600 or self.shopClick.getY() > 650:
			self.shopClick = self.introScreen.getMouse()
		if self.shopClick.getX() < 200:
			return 0
		else:
			return 1
			
	def hospitalButton(self):
		"""Create two buttons that allow the user to select the probability of sick people getting
		healthy at hospital during the simulation."""
		self.hospitalString = graphics.Text(graphics.Point(600,700),"HOSPITAL")
		self.hospitalString.setSize(36)
		self.hospitalString.setStyle("bold")
		self.hospitalString.setFill("purple4")
		self.hospitalLowButton = graphics.Rectangle(graphics.Point(475,650),graphics.Point(575,600))
		self.hospitalLowButton.setFill("purple4")
		self.hospitalLowString = graphics.Text(graphics.Point(525,625),"LOW")
		self.hospitalLowString.setSize(26)
		self.hospitalLowString.setFill("white")
		self.hospitalHighButton = graphics.Rectangle(graphics.Point(625,650),graphics.Point(725,600))
		self.hospitalHighButton.setFill("purple4")
		self.hospitalHighString = graphics.Text(graphics.Point(675,625),"HIGH")
		self.hospitalHighString.setSize(26)
		self.hospitalHighString.setFill("white")
		self.hospitalString.draw(self.introScreen)
		self.hospitalLowButton.draw(self.introScreen)
		self.hospitalLowString.draw(self.introScreen)
		self.hospitalHighButton.draw(self.introScreen)
		self.hospitalHighString.draw(self.introScreen)
		self.hospitalClick = self.introScreen.getMouse()
		while self.hospitalClick.getX() < 475 or self.hospitalClick.getX() > 575 and self.hospitalClick.getX() < 625 or self.hospitalClick.getX() > 725 or self.hospitalClick.getY() < 600 or self.hospitalClick.getY() > 650:
			self.hospitalClick = self.introScreen.getMouse()
		if self.hospitalClick.getX() < 600:
			return 0
		else:
			return 1
			
	def endScreen(self, masterDict):
		"""Create a window displays the numbers of sick and healthy people for each age group
		along with the images. Close it when the user clicks. masterDict is the dictionary 
		of community members after the entire simulation has been run."""
		self.endScreen = graphics.GraphWin("The Common Code", 800, 800)
		self.endScreen.setCoords(0, 0, 800, 800)
		numSickKid = 0
		numHealthyKid = 0
		numSickAdult = 0
		numHealthyAdult = 0
		numSickElderly = 0
		numHealthyElderly = 0
		for key in masterDict:
			if key <= 18:
				numSickKid += masterDict[key][1]
				numHealthyKid += masterDict[key][0]
			elif key <= 60:
				numSickAdult += masterDict[key][1]
				numHealthyAdult += masterDict[key][0]
			else:
				numSickElderly += masterDict[key][1]
				numHealthyElderly += masterDict[key][0]
		bigString = graphics.Text(graphics.Point(400, 700), "SIMULATION COMPLETE")
		bigString.setSize(36)
		bigString.setStyle("bold")
		bigString.setFill("purple4")
		kidImage = graphics.Image(graphics.Point(400,450),"img/kids.gif")
		adultImage = graphics.Image(graphics.Point(200,150),"img/adult.gif")	
		elderlyImage = graphics.Image(graphics.Point(600,150),"img/elderly.gif")
		kidString = graphics.Text(graphics.Point(400,600),"CHILDREN \n Sick: " + str(numSickKid) + "\n Healthy: " + str(numHealthyKid))
		kidString.setSize(20)
		kidString.setFill("purple4")
		adultString = graphics.Text(graphics.Point(200,300),"ADULTS \n Sick: " + str(numSickAdult) + "\n Healthy: " + str(numHealthyAdult))
		adultString.setSize(20)
		adultString.setFill("purple4")
		elderlyString = graphics.Text(graphics.Point(600,300),"ELDERLY \n Sick: " + str(numSickElderly) + "\n Healthy: " + str(numHealthyElderly))
		elderlyString.setSize(20)
		elderlyString.setFill("purple4")
		bigString.draw(self.endScreen)
		kidImage.draw(self.endScreen)
		kidString.draw(self.endScreen)
		adultImage.draw(self.endScreen)
		adultString.draw(self.endScreen)
		elderlyImage.draw(self.endScreen)
		elderlyString.draw(self.endScreen)
		self.endScreen.getMouse()
		# the window closes when the user clicks 
		self.endScreen.close()

def main():
	"""Call the introScreen and once the user has chosen all of the probabilities, close the 
	introScreen, open the main window and run the simulation. After the simulation is complete, 
	call the endScreen."""
	GraphicInterface.introScreen(GraphicInterface)
	schoolProb = GraphicInterface.schoolButton(GraphicInterface)
	officeProb = GraphicInterface.officeButton(GraphicInterface)
	shopProb = GraphicInterface.shopButton(GraphicInterface)
	hospitalProb = GraphicInterface.hospitalButton(GraphicInterface)
	GraphicInterface.introScreen.close()
	sim = Simulation()
	sim.simulate(schoolProb, officeProb, shopProb, hospitalProb)
	sim.interface.endScreen(sim.masterDict)

if __name__ == "__main__":
	main()
		

	


	
		
		