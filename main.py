from QuantLib import *
from filePrinter import *
import QuantLib as ql
import numpy
from instruments import *
from createInstFromCSV import *


csvFilePath = 'csvFiler/datain-20141006.csv'
today = Date(6, October,2014)


#T = [0.0, 0.0821917808219178, 0.1698630136986301, 0.2493150684931507, 0.3342465753424658, 0.4191780821917808, 0.5013698630136987, 0.5917808219178082, 0.6684931506849315, 0.7534246575342466, 0.8410958904109589, 0.9178082191780822, 1.0027397260273974, 1.084931506849315, 1.16986301369863, 1.252054794520548, 1.336986301369863, 1.4219178082191781, 1.5041095890410958, 1.5890410958904109, 1.6767123287671233, 1.7616438356164383, 1.841095890410959, 1.9232876712328768, 2.0027397260273974, 2.084931506849315, 2.16986301369863, 2.252054794520548, 2.336986301369863, 2.4246575342465753, 2.5095890410958903, 2.591780821917808, 2.6767123287671235, 2.758904109589041, 2.8438356164383563, 2.9287671232876713, 3.010958904109589, 3.0931506849315067, 3.175342465753425, 3.2575342465753425, 3.33972602739726, 3.4246575342465753, 3.506849315068493, 3.589041095890411, 3.673972602739726, 3.756164383561644, 3.8383561643835615, 3.9232876712328766, 4.005479452054795, 4.087671232876712, 4.1726027397260275, 4.254794520547946, 4.336986301369863, 4.421917808219178, 4.504109589041096, 4.589041095890411, 4.673972602739726, 4.756164383561644, 4.838356164383562, 4.923287671232877, 5.005479452054795, 5.087671232876712, 5.1726027397260275, 5.254794520547946, 5.33972602739726, 5.424657534246576, 5.506849315068493, 5.5917808219178085, 5.676712328767123, 5.758904109589041, 5.841095890410959, 5.923287671232877, 6.005479452054795, 6.087671232876712, 6.1726027397260275, 6.254794520547946, 6.33972602739726, 6.424657534246576, 6.506849315068493, 6.5917808219178085, 6.676712328767123, 6.758904109589041, 6.841095890410959, 6.923287671232877, 7.005479452054795, 7.087671232876712, 7.1726027397260275, 7.254794520547946, 7.33972602739726, 7.424657534246576, 7.506849315068493, 7.5917808219178085, 7.67945205479452, 7.764383561643836, 7.8493150684931505, 7.934246575342466, 8.016438356164384, 8.095890410958905, 8.175342465753424, 8.254794520547945, 8.33972602739726, 8.427397260273972, 8.512328767123288, 8.594520547945205, 8.67945205479452, 8.761643835616438, 8.843835616438357, 8.92876712328767, 9.01095890410959, 9.093150684931507, 9.178082191780822, 9.26027397260274, 9.342465753424657, 9.427397260273972, 9.509589041095891, 9.594520547945205, 9.67945205479452, 9.761643835616438, 9.843835616438357, 9.926027397260274, 10.008219178082191, 10.09041095890411, 10.175342465753424, 10.257534246575343, 10.342465753424657, 10.427397260273972, 10.509589041095891, 10.594520547945205, 10.67945205479452, 10.761643835616438, 10.843835616438357, 10.926027397260274, 11.008219178082191, 11.09041095890411, 11.175342465753424, 11.257534246575343, 11.342465753424657, 11.427397260273972, 11.509589041095891, 11.594520547945205, 11.67945205479452, 11.761643835616438, 11.843835616438357, 11.926027397260274, 12.008219178082191, 12.09041095890411, 12.175342465753424, 12.257534246575343, 12.342465753424657, 12.427397260273972, 12.509589041095891, 12.594520547945205, 12.67945205479452, 12.761643835616438, 12.843835616438357, 12.92876712328767, 13.01095890410959, 13.093150684931507, 13.178082191780822, 13.26027397260274, 13.345205479452055, 13.432876712328767, 13.517808219178082, 13.6, 13.684931506849315, 13.767123287671232, 13.852054794520548, 13.936986301369863, 14.01917808219178, 14.101369863013698, 14.183561643835617, 14.265753424657534, 14.347945205479451, 14.432876712328767, 14.515068493150684, 14.597260273972603, 14.682191780821919, 14.764383561643836, 14.846575342465753, 14.931506849315069, 15.013698630136986, 15.095890410958905, 15.180821917808219, 15.263013698630138, 15.345205479452055, 15.43013698630137, 15.512328767123288, 15.597260273972603, 15.682191780821919, 15.764383561643836, 15.846575342465753, 15.92876712328767, 16.01095890410959, 16.09315068493151, 16.17808219178082, 16.26027397260274, 16.345205479452055, 16.43013698630137, 16.512328767123286, 16.5972602739726, 16.682191780821917, 16.764383561643836, 16.846575342465755, 16.931506849315067, 17.013698630136986, 17.095890410958905, 17.18082191780822, 17.263013698630136, 17.34794520547945, 17.432876712328767, 17.515068493150686, 17.6, 17.684931506849313, 17.767123287671232, 17.84931506849315, 17.931506849315067, 18.013698630136986, 18.095890410958905, 18.18082191780822, 18.263013698630136, 18.34794520547945, 18.432876712328767, 18.515068493150686, 18.6, 18.687671232876713, 18.77260273972603, 18.85753424657534, 18.942465753424656, 19.024657534246575, 19.104109589041094, 19.183561643835617, 19.263013698630136, 19.34794520547945, 19.435616438356163, 19.52054794520548, 19.602739726027398, 19.687671232876713, 19.76986301369863, 19.852054794520548, 19.936986301369863, 20.019178082191782, 20.101369863013698, 20.186301369863013, 20.268493150684932, 20.350684931506848, 20.435616438356163, 20.517808219178082, 20.6, 20.684931506849313, 20.767123287671232, 20.84931506849315, 20.934246575342467, 21.016438356164382, 21.0986301369863, 21.183561643835617, 21.265753424657536, 21.350684931506848, 21.435616438356163, 21.517808219178082, 21.602739726027398, 21.687671232876713, 21.76986301369863, 21.852054794520548, 21.934246575342467, 22.016438356164382, 22.0986301369863, 22.183561643835617, 22.265753424657536, 22.350684931506848, 22.435616438356163, 22.517808219178082, 22.602739726027398, 22.687671232876713, 22.76986301369863, 22.852054794520548, 22.934246575342467, 23.016438356164382, 23.0986301369863, 23.183561643835617, 23.265753424657536, 23.350684931506848, 23.435616438356163, 23.517808219178082, 23.602739726027398, 23.687671232876713, 23.76986301369863, 23.852054794520548, 23.934246575342467, 24.016438356164382, 24.0986301369863, 24.183561643835617, 24.265753424657536, 24.350684931506848, 24.435616438356163, 24.517808219178082, 24.602739726027398, 24.69041095890411, 24.775342465753425, 24.85753424657534, 24.942465753424656, 25.024657534246575, 25.106849315068494, 25.19178082191781, 25.273972602739725, 25.356164383561644, 25.44109589041096, 25.523287671232875, 25.605479452054794, 25.69041095890411, 25.77260273972603, 25.854794520547944, 25.93972602739726, 26.02191780821918, 26.104109589041094, 26.18904109589041, 26.27123287671233, 26.353424657534248, 26.438356164383563, 26.52054794520548, 26.605479452054794, 26.69041095890411, 26.77260273972603, 26.854794520547944, 26.936986301369863, 27.019178082191782, 27.101369863013698, 27.186301369863013, 27.268493150684932, 27.353424657534248, 27.438356164383563, 27.52054794520548, 27.605479452054794, 27.69041095890411, 27.77260273972603, 27.854794520547944, 27.936986301369863, 28.019178082191782, 28.101369863013698, 28.186301369863013, 28.268493150684932, 28.353424657534248, 28.438356164383563, 28.52054794520548, 28.605479452054794, 28.69041095890411, 28.77260273972603, 28.854794520547944, 28.93972602739726, 29.02191780821918, 29.104109589041094, 29.18904109589041, 29.27123287671233, 29.356164383561644, 29.44109589041096, 29.523287671232875, 29.60821917808219, 29.695890410958903, 29.78082191780822, 29.865753424657534, 29.95068493150685, 30.03287671232877]

#T = createT(30.0328767123287683,360)
iStartNumbers = getInstrumentIndexes(csvFilePath) # när nytt instrument börjar
currency = getInstrumentCurrencies(csvFilePath)
penalty = getInstrumentPenalties(csvFilePath)
tenors = getInstrumentTenors(csvFilePath)
scaleCon = getInstrumentScaleCon(csvFilePath)
conTransf = getInstrumentConTransf(csvFilePath)
currency2 = getInstrumentCurrency2(csvFilePath)
tenor2 = getInstrumentTenor2(csvFilePath)
currencySet = getCurrencySet(csvFilePath)
tenorSet = getTenorSet(csvFilePath)


# fyll iList med alla instrumentListor i csv filen
iList = []
iList = createInstrumentsFromCSV(csvFilePath)
print("Start Date: " + str(today))
T = createT(iList, today)

# fill uniquePrices with all instrument prices
uniquePrices = []
uniquePrices = createUniquePrices(iList)

#öppna fil
f = open('data.dat', 'a')
f.seek(0)
f.truncate()

f.write("data;\n")

#skriv ut currencySet
f.write("set currencySet := ")
for i in currencySet:
	f.write(str(i) + " ")
f.write(";\n")

#skriv ut tenorSet
f.write("set tenorSet := ")
for i in tenorSet:
	f.write(str(i) + " ")
f.write(";\n")

#print instrument matrixes, each i in iList is a list of the same instrument
print(str(len(iList)) + " instrument types")
for i in range(0,len(iList)):
	printInstrumnetfile(iList[i], iStartNumbers[i], f, T, today)
f.write("\n")

# printing currency2 vector
f.write("param currency2 := ")
for i in range(0,len(currency2)):
	if (currency2[i] != 0):
		f.write(str(i+1) + " " + str(currency2[i]) + " ")
f.write(";\n")

# printing tenor2 vector
f.write("param tsTenor2 := ")
for i in range(0,len(tenor2)):
	if (tenor2[i] != 0):
		f.write(str(i+1) + " " + str(tenor2[i]) + " ")
f.write(";\n")

# printing unique price vector
f.write("param uniquePrice := ")
for i in range(0,len(uniquePrices)):
    f.write(str(i+1) + " " + str(uniquePrices[i]) + " ")
f.write(";\n")

# printing Penalty vector
f.write("param penaltyParam := ")
for i in range(0,len(penalty)):
	f.write(str(i+1) + " " + str(penalty[i]) + " ")
f.write(";\n")

# printing scaleCon vector
f.write("param scaleConParam := ")
for i in range(0,len(scaleCon)):
	f.write(str(i+1) + " " + str(scaleCon[i]) + " ")
f.write(";\n")

# printing conTransf vector
f.write("param conTransf := ")
for i in range(0,len(conTransf)):
	f.write(str(i+1) + " " + str(conTransf[i]) + " ")
f.write(";\n")

# printing Tenors vector
f.write("param tenor := ")
for i in range(0,len(tenors)):
	f.write(str(i+1) + " " + str(tenors[i]) + " ")
f.write(";\n")

# printing currency vector
f.write("param currency := ")
for i in range(0,len(currency)):
    f.write(str(i+1) + " " + str(currency[i]) + " ")
f.write(";\n")

# printing nF vector
f.write("param nF := ")
f.write(str(len(T)-1))
f.write(";\n")

# printing T vector
f.write("param T := ")
for i in range(0,len(T)):
	f.write(str(i) + " " + str(T[i]) + " ")
f.write(";\n")

