from scipy.stats import norm
import math

print("This assumes you have logged in and collected all rewards.\n----------------------------------------------------------")
hoursremaining, minutesremaining, currentamount, amountpurchased, itemspurchased, refund, currentrefundamount, stdv, min, max, zscoremultiplier= "hi", "hi", "hi", "hi", "hi", False, False, [11.26547571, 11.92012577, 12.55687184, 13.15464308, 13.7195342, 14.26648636, 14.79397229, 15.30287304, 15.7951627, 16.28289954, 16.74643031, 17.19346777, 17.62858847, 18.07176639, 18.51452115, 18.91194576, 19.28731812, 19.7030532, 20.09810867, 20.46520931, 20.85194009, 21.20842074, 21.53045525, 21.91017268, 22.26314065, 22.5803463, 22.91635965, 23.27941487, 23.63328847, 23.89992964, 24.20896237, 24.5595039, 24.8385546, 25.17988853, 25.50120586, 25.74998964, 26.07528606, 26.36149022, 26.66681844, 26.95576282, 27.20197534, 27.52933237, 27.77716647, 28.05745121, 28.33310071, 28.52495791, 28.83015726, 29.10664022, 29.38506521, 29.61923628, 29.91846864, 30.14804451, 30.38978958, 30.63711162, 30.88760571, 31.13421806, 31.41948845, 31.64842714, 31.89644667, 32.15984605, 32.39936286, 32.57406041, 32.84845205, 33.06140972, 33.31472273, 33.52231872, 33.72012966, 33.99482751, 34.21831063, 34.44581622, 34.62277195, 34.91216646, 35.10773759, 35.31342861, 35.54710926, 35.77187536, 35.93622247, 36.17078326, 36.36797076, 36.59549543, 36.82044673, 37.01012848, 37.20745361, 37.38391308, 37.64631048, 37.84421695, 38.03394236, 38.23555423, 38.42491805, 38.6182449, 38.81497643, 39.0453101, 39.27221193, 39.40077936, 39.61606792, 39.81141766, 39.98066215, 40.17698832, 40.3807501, 40.58684032, 40.77099668, 40.95149596, 41.14288352, 41.38710143, 41.4930426, 41.69463034, 41.87955906, 42.08668609, 42.27301021, 42.40351352, 42.64124057, 42.76125725, 42.95064712, 43.16456492, 43.33382584, 43.47960617, 43.72326168, 43.86029686, 44.04145742, 44.23955537, 44.39452208, 44.52465482, 44.72852772, 44.89793997, 45.02277911, 45.22358822, 45.35913082, 45.55002231, 45.73428815, 45.91865122, 46.10958545, 46.24178553, 46.46406637, 46.56383621, 46.78788203, 46.87708452, 47.06556199, 47.24954272, 47.34685117, 47.53286464, 47.72405864, 47.88236992, 48.01768069, 48.1544126, 48.31474053, 48.46563423, 48.61463966, 48.85925228, 48.95158975, 49.09798974, 49.26921135, 49.43364639, 49.5562897, 49.74488633, 49.92041478, 50.05176657, 50.23919718, 50.38811836, 50.5515158, 50.67882996, 50.85689823, 51.00059566, 51.09687637, 51.28040637, 51.39998703, 51.58363929, 51.75479081, 51.84426206], [0, 1, 6, 7, 17, 22, 26, 36, 44, 5055, 64, 78, 82, 85, 90, 107, 115, 122, 134, 138, 146, 152, 166, 173, 172, 196, 202, 211, 221, 232, 232, 246, 259, 265, 264, 281, 287, 297, 308, 310, 317, 335, 329, 340, 361, 375, 349, 384, 403, 339, 423, 428, 437, 445, 455, 465, 467, 487, 491, 504, 508, 517, 532, 536, 550, 563, 565, 585, 585, 596, 604, 616, 626, 638, 638, 623672, 671, 669, 685, 707, 714, 719, 715, 742, 757, 756, 763, 746, 778, 789, 798, 801, 826, 817, 839, 859, 868, 861, 878, 894, 902, 914, 919, 932, 941, 942, 944, 970, 991, 983, 1003, 1008, 1012, 1013, 1038, 1054, 1059, 1073, 1060, 1092, 1096, 1103, 1101, 1122, 1132, 1142, 1150, 1160, 1182, 1183, 1174, 1204, 1206, 1203, 1200, 1230, 1238, 1269, 1266, 1290, 1297, 1277, 1305, 1322, 1309, 1307, 1351, 1355, 1354, 1372, 1388, 1392, 1404, 1430, 1427, 1419, 1428, 1448, 1471, 1461, 1461, 1469, 1522, 1515, 1525, 1482], [30, 51, 70, 86, 100, 114, 127, 143, 157, 172, 182, 198, 212, 228, 230, 251, 261, 273, 287, 298, 309, 328, 343, 348, 355, 373, 385, 396, 410, 423, 438, 444, 457, 467, 482, 501, 508, 521, 534, 545, 555, 562, 587, 595, 603, 612, 629, 641, 656, 670, 675, 685, 698, 714, 734, 725, 740, 747, 763, 776, 796, 805, 824, 824, 842, 854, 869, 874, 888, 907, 905, 920, 943, 954, 956, 962, 990, 1024, 1005, 1002, 1048, 1067, 1053, 1069, 1076, 1104, 1091, 1110, 1115, 1131, 1141, 1168, 1168, 1194, 1188, 1195, 1210, 1227, 1235, 1254, 1257, 1266, 1296, 1290, 1308, 1323, 1323, 1343, 1340, 1355, 1375, 1377, 1392, 1397, 1420, 1426, 1448, 1452, 1485, 1479, 1493, 1506, 1509, 1526, 1550, 1547, 1573, 1561, 1577, 1600, 1621, 1608, 1623, 1639, 1643, 1653, 1665, 1672, 1687, 1704, 1715, 1731, 1739, 1753, 1772, 1783, 1784, 1802, 1801, 1803, 1867, 1842, 1876, 1872, 1872, 1887, 1904, 1893, 1911, 1952, 1937, 1951, 1976, 1962, 1984, 2009, 2018, 2044], [1.91452, 2.60238, 3.06372, 3.71902, 4.29443, 4.75342]
try:
  while type(hoursremaining) == str:
    hoursremaining = input(
        "How many hours are remaining? (in-game timer)\n")
    try:
      hoursremaining = int(hoursremaining)
      if (0 > hoursremaining or hoursremaining > 192):
        print("Please input a valid number of hours.")
        hoursremaining = "Fail"
    except Exception as noninteger:
      print("Please input an integer (whole number) for hours.")
      hoursremaining = "Fail"
  while type(minutesremaining) == str:
    minutesremaining = input(
        "How many minutes are remaining? (in-game timer)\n")
    try:
      minutesremaining = int(minutesremaining)
      if (0 > minutesremaining or minutesremaining >= 60):
        print("Please input a valid number of minutes.")
        minutessRemaining = "Fail"
      if (hoursremaining == 192 and minutesremaining > 0):
        print("You can't have more than 8 days of collection (192 hours).")
        minutesremaining = "Fail"
    except Exception as noninteger:
      print("\nPlease input an integer (whole number) for minutes.")
      minutessRemaining = "Fail"
  while type(currentamount) == str:
    if (refund == True):
      currentamount = input("How many campaign items do you currently have?\nIf the negative number was due to a refund, please type \"refund\" below.\n")
      try:
        if (str.lower(currentamount) != "refund"
            or str.lower(currentamount) != "refund"):
          currentamount = currentrefundamount
      except Exception as nostring:
        refund = False
    else:
      currentamount = input("How many campaign items do you currently have?\n")
    if (refund == False):
      try:
        currentamount = int(currentamount)
        if (currentamount < 0):
          print("Enter a valid amount of items. If this is due to a refund, please type refund.")
          refund, currentrefundamount, currentamount = True, currentamount, "refund?"
      except Exception as noninteger:
        pass
        print("\nPlease input an integer (whole number) for current items.")
        currentamount = "Fail"
  while type(itemspurchased) == str:
    itemspurchased = input("How many items have been spent on rewards?\n")
    try:
      itemspurchased = int(itemspurchased)
    except Exception as noninteger:
      print("\nPlease input an integer (whole number) for items spend on rewards.")
      itemspurchased = "Fail"
    if (hoursremaining < 24
        or (hoursremaining == 24 and minutesremaining == 0)):
      raise GeneratorExit
  while type(amountpurchased) == str:
    amountpurchased = input("How many items from packs or crystals have been purchased?\n")
    try:
      amountpurchased = int(amountpurchased)
    except Exception as noninteger:
      print("\nPlease input an integer (whole number) for items purchased.")
      amountpurchased = "Fail"

  def zcalc(current, hoursleft, day):
    try:
      if (minutesremaining == 0):
        stdvpredicted = stdv[hoursremaining - 1]
      else:
        stdvpredicted = ((stdv[math.ceil(hoursleft) - 1] -stdv[math.floor(hoursleft) - 1]) /(math.ceil(hoursleft) - math.floor(hoursleft))) * (hoursleft - math.floor(hoursleft)) + stdv[math.floor(hoursleft) - 1]
    except Exception as stdvrange:
      pass
      stdvpredicted = 1.05977357360136 * 10 + 6.95546690304286 * 10**(-1) * hoursleft - 1.67571179241219 * 10**(-2) * hoursleft**2 + 5.05383084475387 * 10**(-4) * hoursleft**3 - 1.17803724420283 * 10**(-5) * hoursleft**4 + 1.9390541003977 * 10**(-7) * hoursleft**5 - 2.18168285848933 * 10**(-9) * hoursleft**6 + 1.62938690786485 * 10**(-11) * hoursleft**7 - 7.68703295853448 * 10**(-14) * hoursleft**8 + 2.06664417836592 * 10**(-16) * hoursleft**9 - 2.40708085158142 * 10**(-19) * hoursleft**10
    try:
      if (minutesremaining == 0):
        stdvdone = stdv[(192 - hoursremaining) - 1]
      else:
        stdvdone = ((stdv[math.ceil(168 - hoursleft) - 1] -stdv[math.floor(168 - hoursleft) - 1]) /(math.ceil(168 - hoursleft) - math.floor(168 - hoursleft))) * (hoursleft - math.floor(hoursleft)) + stdv[math.floor(168 - hoursleft) - 1]
    except Exception as stdvrange:
      pass
      stdvdone = 1.05977357360136 * 10 + 6.95546690304286 * 10**(-1) * (168 - hoursleft) - 1.67571179241219 * 10**(-2) * (168 - hoursleft)**2 + 5.05383084475387 * 10**(-4) * (168 - hoursleft)**3 - 1.17803724420283 * 10**(-5) * (168 -hoursleft)**4 + 1.9390541003977 * 10**(-7) * (168 - hoursleft)**5 - 2.18168285848933 * 10**(-9) * (168 - hoursleft)**6 + 1.62938690786485 * 10**(-11) * (168 - hoursleft)**7 - 7.68703295853448 * 10**(-14) * (168 - hoursleft)**8 + 2.06664417836592 * 10**(-16) * (168 - hoursleft)**9 - 2.40708085158142 * 10**(-19) * (168 - hoursleft)**10

    zscorenow = (currentamount - 100 * day - 1774.08 / 168 *(168 - hoursleft)) / stdvdone
    nowprobXlow = norm.cdf(zscorenow)
    nowprobXhigh = 1 - norm.cdf(zscorenow)

    zscorecurr = (current - currentamount + 100 * day -1774.08 / 168 * hoursleft) / stdvpredicted
    currprobXlow = norm.cdf(zscorecurr)
    currprobXhigh = 1 - norm.cdf(zscorecurr)

    zscorezonenow, zscorezonecurr =0, 0
    for i in range(5):
      if (zscorenow >= zscoremultiplier[i]): zscorezonenow = i
      if (zscorecurr >= zscoremultiplier[i]): zscorezonecurr = i
      if (zscorezonenow != i and zscorezonecurr != i): break
      
    return (nowprobXlow, nowprobXhigh, zscorezonenow, currprobXlow, currprobXhigh, zscorezonecurr, stdvpredicted)

  def campaigncalc(hours, minutes, current, Purchased, Spent):
    f2pamount = current - Purchased + Spent
    hoursleft = hours + minutes / 60 - 24
    daynumber = math.ceil(7 - hoursleft / 24)

    estimateaverage = math.floor(current + hoursleft * 10.56 +(7 - daynumber) * 100)
    estimatecurrent = math.floor(current + (f2pamount - daynumber * 100) /(168 - hoursleft) * hoursleft +(7 - daynumber) * 100)

    zstats = zcalc(estimatecurrent - 700, hoursleft,daynumber)

    return (7 - daynumber, estimateaverage, estimatecurrent, zstats, f2pamount - daynumber * 100)

  def output(results, text):
    if(minutesremaining>0):hoursdone=191-hoursremaining
    else:hoursdone=192-hoursremaining
    if(minutesremaining==0):minutesdone=0
    else:minutesdone=60-minutesremaining

    if(amountpurchased>0):money=1
    else:money=0
    if(itemspurchased>0):spant=1
    else:spant=0
    if(results[3][0]>0.5):now=0
    else:now=1
    if(results[3][3]>0.5):curr=0
    else:curr=1
    if(hoursdone<=0):
      if(minutesdone==1):time=text[7][0]
      else:time=text[7][1]
    elif(minutesdone<=0):
      if(hoursdone==1):time=text[6][0]+" into event."
      else:time=text[6][1]+" into event."
    elif(hoursdone==1):
      if(minutesdone==1):time=text[6][0]+" and "+text[7][0]
      else:time=text[7][0]+" and "+text[8][1]
    elif(minutesdone==1):time=text[6][1]+" and "+text[7][0]
    else:time=text[6][1]+" and "+text[7][1]
    if(results[3][2]>0):nowodd=[1,results[3][2]]
    else:nowodd=[0,0]
    if(results[3][5]>0):currodd=[1,results[3][5]]
    else:currodd=[0,0]

    if(results[4]<=0):outputtext=text[0]+text[1][money]+text[2][spant]+str("\n\nPredicted Item Count (average rate): ")+str(results[1])+str(" Items\nPredicted range: ")+str(math.floor(results[1]-results[3][6]))+str("-")+str(math.floor(results[1]+results[3][6]))+str(" Items\n----------------------------------------------------------")+text[5][now]+time+text[8][nowodd[0]]+text[9][nowodd[1]]
    else:outputtext=text[0]+text[1][money]+text[2][spant]+text[3]+text[4][curr]+text[8][currodd[0]]+text[9][currodd[1]]+text[5][now]+time+text[8][nowodd[0]]+text[9][nowodd[1]]

    return(outputtext)
  results = campaigncalc(hoursremaining, minutesremaining, currentamount,amountpurchased, itemspurchased)
  try:
    default1, purchase, spent, default2, currprob, nowprob, hour, minute, oddsdefault,odds=str("\n----------------------------------------------------------\nTime Remaining: ")+str(results[0])+str(" days ")+str(hoursremaining - 24 * results[0] - 24)+str(" hours ")+str(minutesremaining)+str(" minutes\nDaily Loot Remaining: ")+str(100 * results[0])+str(" Items"),["",str("\nTotal items purchased: ")+str(amountpurchased)+str(" Items")],["",str("\nTotal items spent: ")+str(itemspurchased)+str(" Items")],str("\n\nPredicted Item Count (average rate): ")+str(results[1])+str(" Items\nPredicted Item Count (current rate): ")+str(results[2])+str(" Items\nPredicted range: ")+str(math.floor(results[1]-results[3][6]))+str("-")+str(math.floor(results[1]+results[3][6]))+str(" Items\n----------------------------------------------------------\n"),[str("You have a ")+str(round(results[3][3]*100,3))+str("% to be ")+str(results[2])+str(" items or lower by the end of the event."),str("You have a ")+str(round(results[3][4]*100,3))+str("% to be ")+str(results[2])+str(" items or higher by the end of the event.")],[str("\nYou had a ")+str(round(results[3][0]*100,3))+str("% to be ")+str(currentamount)+str(" items or lower at "),
    str("\nYou had a ")+str(round(results[3][1]*100,3))+str("% to be ")+str(currentamount)+str(" items or higher at ")],[str("1 hour"),str(192-hoursremaining)+str(" hours")],[str("1 minute into event."),str(60-minutesremaining)+str(" minutes into event.")],["",str("\n~~These odds are lower than ")],["","rolling the same number on a dice three times in a row.~~","rolling the same number on a dice four times in a row.~~","getting 3 5* in a 10 pull of heroic scrolls.~~","getting injured by a toilet or finding a four-leaf clover.~~","being struck by lightning.~~","truly being 1 in a million.~~"]

    print(output(results,[default1, purchase, spent, default2, currprob, nowprob, hour, minute, oddsdefault,odds]))    

  except Exception as err:
    print("An error has occured\n", err,"\nPlease contact me on reddit or discord with the error above.")
except GeneratorExit as gen:
  print("\n----------------------------------------------------------\nWhats the point of the calculator if the event is over?\nYou already know the values with 100% certainty.\nFinishing Item Count:",currentamount + itemspurchased,"Items")
except Exception as err:
  print("An error has occured\n", err,"\nPlease contact me on reddit or discord with the error above.")