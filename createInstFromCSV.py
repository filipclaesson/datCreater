import csv
import QuantLib as ql
from instruments import *

#f = open('datain.csv', 'rb')
#myOIS(clcDate, tenor, maturity, calendar, businessDayConvention, terminationDateBusinessDayConvention, dateGeneration)

# Functions for getting raw instrument information from instrumentRow in csv
smallPenalty = 0
bigPenalty = 0

def getInstrumentType(instrumentRow):
	return instrumentRow[0]

def getDate(instrumentRow):
	date = instrumentRow[1]
	year = int("20" + date[0:2])
	month = int(date[3:5])
	day = int(date[6:8])
	return Date(day,month,year)

def getPeriod1(instrumentRow):
	tenor = instrumentRow[2]
	return int(tenor)

def getPeriod2(instrumentRow):
	tenor = instrumentRow[3]
	return int(tenor)

def getMaturity(instrumentRow):
	maturity = instrumentRow[4]
	return int(maturity)

def getCountryCode(instrumentRow):
	return instrumentRow[5]

def getBusinessDayConvention(instrumentRow):
	return instrumentRow[6]

def getTerminationConvention(instrumentRow):
	return instrumentRow[7]

def getDateGeneration(instrumentRow):
	return instrumentRow[8]

def getUniquePrice(instrumentRow):
	uniquePrice = instrumentRow[9]
	uniquePrice = float(uniquePrice.replace(',','.'))
	return float(uniquePrice)

def getCurrency2(instrumentRow):
	return instrumentRow[10]

# Functions for creating instruments

def getInstrumentTypeFunction(instrumentType):
	if instrumentType == "irs":
		return myIRS
	elif instrumentType == "ois":
		return myOIS
	elif instrumentType == "ts":
		return myTS
	elif instrumentType == "ccs":
		return myCCS
	elif instrumentType == "fra":
		return myFRA

def getQLCalendar(instrumentRow):
	countryCode = getCountryCode(instrumentRow)
	
	if (getInstrumentType(instrumentRow) == "ccs"):
		countryCode2 = getCurrency2(instrumentRow)
		cals = []
		cals.append(getCalendar(countryCode))
		cals.append(getCalendar(countryCode2))
		return cals

	cals = getCalendar(countryCode)


	return getCalendar(countryCode)

	

def getCalendar(countryCode):
	if countryCode == "SEK":
		cal = ql.Sweden()
	elif countryCode == "NOK":
		cal = ql.Norway()
	elif countryCode == "USD":
		cal = ql.UnitedStates()
	elif countryCode == "GBP":
		cal = ql.UnitedKingdom()
	elif countryCode == "JPY":
		cal = ql.Japan()
	elif countryCode == "EUR":
		cal = ql.TARGET()
	return cal

def getTenors(instrumentRow):
	return [getPeriod1(instrumentRow), getPeriod2(instrumentRow)]

def getQLDateGeneration(instrumentRow):
	generation = getDateGeneration(instrumentRow)
	if generation == "Forward":
		return ql.DateGeneration.Forward
	elif generation == "Backward":
		return ql.DateGeneration.Backward
	elif generation == "Zero":
		return ql.DateGeneration.Zero
	elif generation == "Twentieth":
		return ql.DateGeneration.Twentieth
	elif generation == "ThirdWednesday":
		return ql.DateGeneration.ThirdWednesday
	elif generation == "Rule":
		return ql.DateGeneration.Rule

def getQLDayConvention(convention):
	if convention == "Following":
		return ql.Following
	elif convention == "ModifiedFollowing":
		return ql.ModifiedFollowing
	elif convention == "Preceding":
		return ql.Preceding
	elif convention == "ModifiedPreceding":
		return ql.ModifiedPreceding
	elif convention == "Unadjusted":
		return ql.Unadjusted
	elif convention == "HalfMonthModifiedFollowing":
		return ql.HalfMonthModifiedFollowing
	elif convention == "Nearest":
		return ql.Nearest





def createInstrumentsFromCSV(filePath):

	csvInstrumentInfo = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentInfo.append(row)

	
	#create the instruments from the instrumentInfo, 
	iterator = iter(csvInstrumentInfo)
	newInstrumentFlag = False
	instrumentSetsList = []
	tempList = []
	for i in range(0, len(csvInstrumentInfo)):
		# if the flag is raised the instrument is of a new type and the list is saved and a new one is created
		if (newInstrumentFlag):
			instrumentSetsList.append(tempList)
			tempList = []
		
		#raise flag if next instrument is of new type
		if i < (len(csvInstrumentInfo)-1):
			if getInstrumentType(csvInstrumentInfo[i+1]) != getInstrumentType(csvInstrumentInfo[i]):
				newInstrumentFlag = True
			else:
				newInstrumentFlag = False

		#create the intrument

		tempInstrumentFunction = getInstrumentTypeFunction(getInstrumentType(csvInstrumentInfo[i]))
		tempList.append(tempInstrumentFunction(getDate(csvInstrumentInfo[i]), getTenors(csvInstrumentInfo[i]),getMaturity(csvInstrumentInfo[i]), getQLCalendar(csvInstrumentInfo[i]), getQLDayConvention(getBusinessDayConvention(csvInstrumentInfo[i])), getQLDayConvention(getTerminationConvention(csvInstrumentInfo[i])), getQLDateGeneration(csvInstrumentInfo[i]), ql.Actual360(), getUniquePrice(csvInstrumentInfo[i])))
		#if it is the last instrument the list is saved
		if i == len(csvInstrumentInfo)-1:
			instrumentSetsList.append(tempList)

	return instrumentSetsList

def getInstrumentIndexes(filePath):
	csvInstrumentInfo = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentInfo.append(row)

	indexes = [1]

	for i in range(0, len(csvInstrumentInfo)):
		#print(csvInstrumentInfo[i])
		if i < (len(csvInstrumentInfo)-1):
			if getInstrumentType(csvInstrumentInfo[i+1]) != getInstrumentType(csvInstrumentInfo[i]):
				indexes.append(i+2)

	return indexes


def getInstrumentCurrencies(filePath):
	csvInstrumentInfo = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentInfo.append(row)

	currencies = []
	for i in csvInstrumentInfo:
		currencies.append(getCountryCode(i))

	return currencies

def getInstrumentTenors(filePath):
	csvInstrumentTenors = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentTenors.append(row)

	tenors = []

	for i in csvInstrumentTenors:
		
		if(getInstrumentType(i)=="ois"):
			tenor = "ON"
		elif(getInstrumentType(i) =="irs"):

			if(getPeriod2(i) == 3):
				tenor = "3M"
			elif(getPeriod2(i) == 6):
				tenor = "6M"
		elif(getInstrumentType(i) =="ccs"):
			if(getPeriod1(i) == 3):
				tenor = "3M"
			elif(getPeriod1(i) == 6):
				tenor = "6M"
		elif(getInstrumentType(i) =="ts"):
			if(getPeriod1(i) == 3):
				tenor = "3M"
			elif(getPeriod1(i) == 6):
				tenor = "6M"
		elif(getInstrumentType(i) =="fra"):
			if(getPeriod2(i)-getPeriod1(i) == 3):
				tenor = "3M"
			elif(getPeriod2(i)-getPeriod1(i) == 6):
				tenor = "6M"
		tenors.append(tenor)
		
	a = list(set(tenors))
	#print(a)

	#print(tenors)

	return tenors


def getInstrumentPenalties(filePath):
	csvInstrumentPenalties = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentPenalties.append(row)

	penalties = []
	for i in csvInstrumentPenalties:
		if (getInstrumentType(i)=="ccs") | (getInstrumentType(i)=="ts"):
			penalty = 100 # borde vara 100ggr större men ty lägre likviditet så tillåter vi lite mer avvikelser
		else:
			penalty = 10

		penalties.append(penalty)
	return penalties


def getInstrumentScaleCon(filePath):
	csvInstrumentScaleCon = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentScaleCon.append(row)
			
	scaleCon = []
	for i in range(0, len(csvInstrumentScaleCon)):
		scaleCon.append(1)

	return scaleCon


def getInstrumentConTransf(filePath):
	csvInstrumentConTransf = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentConTransf.append(row)
			
	conTransf = []
	for i in range(0, len(csvInstrumentConTransf)):
		conTransf.append(1)

	return conTransf

def getInstrumentCurrency2(filePath):
	csvInstrumentCurrency2 = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentCurrency2.append(row)

	currencies = []
	for i in csvInstrumentCurrency2:
		if(i[10]=="-"):
			currency = 0
		else:
			currency = getCurrency2(i)

		currencies.append(currency)
	return currencies


def getInstrumentTenor2(filePath):
	csvInstrumentTenor2 = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentTenor2.append(row)

	tenors = []
	for i in csvInstrumentTenor2:
		if(getInstrumentType(i) != "ts"):
			tenor = 0
		else:
			tenor = str(getPeriod2(i))+"M"

		tenors.append(tenor)
	return tenors



def getCurrencySet(filePath):
	csvInstrumentInfo = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentInfo.append(row)

	currencies = []
	for i in csvInstrumentInfo:
		currencies.append(getCountryCode(i))
	a = list(set(currencies))
	#print(a)

	#print(tenors)
	return a


def getTenorSet(filePath):
	csvInstrumentTenors = []
	#create a list of instrumentInfos - list item is a list of attributes of one instrument
	with open(filePath, 'rt') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader) # to skip the top row
		for row in reader:
			csvInstrumentTenors.append(row)

	tenors = []
	for i in csvInstrumentTenors:
		if(getInstrumentType(i)=="ois"):
			tenor = ""
		elif(getInstrumentType(i)=="ccs"):
			tenor = ""
		elif(getInstrumentType(i)=="fra"):
			tenor = ""
		else:
			if(getPeriod2(i) == 6):
				tenor = "6M"
			elif(getPeriod2(i) == 3):
				tenor = "3M"
		tenors.append(tenor)
	a = list(set(tenors))
	#print(a)

	#print(tenors)
	return a
