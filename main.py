from scipy.stats import norm
import math

#variable setup
hours, minutes, current, extra, spent, custominput, impsbool, custom= "hi", "hi", "hi", "hi", "hi", "hi", "hi", "none"
refund, currentrefundamount, zero_time_check= False, False, True
newline = "\n----------------------------------------------------------"
stdv= [11.26547571, 11.92012577, 12.55687184, 13.15464308, 13.7195342, 14.26648636, 14.79397229, 15.30287304, 15.7951627, 16.28289954, 16.74643031, 17.19346777, 17.62858847, 18.07176639, 18.51452115, 18.91194576, 19.28731812, 19.7030532, 20.09810867, 20.46520931, 20.85194009, 21.20842074, 21.53045525, 21.91017268, 22.26314065, 22.5803463, 22.91635965, 23.27941487, 23.63328847, 23.89992964, 24.20896237, 24.5595039, 24.8385546, 25.17988853, 25.50120586, 25.74998964, 26.07528606, 26.36149022, 26.66681844, 26.95576282, 27.20197534, 27.52933237, 27.77716647, 28.05745121, 28.33310071, 28.52495791, 28.83015726, 29.10664022, 29.38506521, 29.61923628, 29.91846864, 30.14804451, 30.38978958, 30.63711162, 30.88760571, 31.13421806, 31.41948845, 31.64842714, 31.89644667, 32.15984605, 32.39936286, 32.57406041, 32.84845205, 33.06140972, 33.31472273, 33.52231872, 33.72012966, 33.99482751, 34.21831063, 34.44581622, 34.62277195, 34.91216646, 35.10773759, 35.31342861, 35.54710926, 35.77187536, 35.93622247, 36.17078326, 36.36797076, 36.59549543, 36.82044673, 37.01012848, 37.20745361, 37.38391308, 37.64631048, 37.84421695, 38.03394236, 38.23555423, 38.42491805, 38.6182449, 38.81497643, 39.0453101, 39.27221193, 39.40077936, 39.61606792, 39.81141766, 39.98066215, 40.17698832, 40.3807501, 40.58684032, 40.77099668, 40.95149596, 41.14288352, 41.38710143, 41.4930426, 41.69463034, 41.87955906, 42.08668609, 42.27301021, 42.40351352, 42.64124057, 42.76125725, 42.95064712, 43.16456492, 43.33382584, 43.47960617, 43.72326168, 43.86029686, 44.04145742, 44.23955537, 44.39452208, 44.52465482, 44.72852772, 44.89793997, 45.02277911, 45.22358822, 45.35913082, 45.55002231, 45.73428815, 45.91865122, 46.10958545, 46.24178553, 46.46406637, 46.56383621, 46.78788203, 46.87708452, 47.06556199, 47.24954272, 47.34685117, 47.53286464, 47.72405864, 47.88236992, 48.01768069, 48.1544126, 48.31474053, 48.46563423, 48.61463966, 48.85925228, 48.95158975, 49.09798974, 49.26921135, 49.43364639, 49.5562897, 49.74488633, 49.92041478, 50.05176657, 50.23919718, 50.38811836, 50.5515158, 50.67882996, 50.85689823, 51.00059566, 51.09687637, 51.28040637, 51.39998703, 51.58363929, 51.75479081, 51.84426206, 52.01737166]
#min, max = [0, 1, 6, 7, 17, 22, 26, 36, 44, 5055, 64, 78, 82, 85, 90, 107, 115, 122, 134, 138, 146, 152, 166, 173, 172, 196, 202, 211, 221, 232, 232, 246, 259, 265, 264, 281, 287, 297, 308, 310, 317, 335, 329, 340, 361, 375, 349, 384, 403, 339, 423, 428, 437, 445, 455, 465, 467, 487, 491, 504, 508, 517, 532, 536, 550, 563, 565, 585, 585, 596, 604, 616, 626, 638, 638, 623672, 671, 669, 685, 707, 714, 719, 715, 742, 757, 756, 763, 746, 778, 789, 798, 801, 826, 817, 839, 859, 868, 861, 878, 894, 902, 914, 919, 932, 941, 942, 944, 970, 991, 983, 1003, 1008, 1012, 1013, 1038, 1054, 1059, 1073, 1060, 1092, 1096, 1103, 1101, 1122, 1132, 1142, 1150, 1160, 1182, 1183, 1174, 1204, 1206, 1203, 1200, 1230, 1238, 1269, 1266, 1290, 1297, 1277, 1305, 1322, 1309, 1307, 1351, 1355, 1354, 1372, 1388, 1392, 1404, 1430, 1427, 1419, 1428, 1448, 1471, 1461, 1461, 1469, 1522, 1515, 1525, 1482], [30, 51, 70, 86, 100, 114, 127, 143, 157, 172, 182, 198, 212, 228, 230, 251, 261, 273, 287, 298, 309, 328, 343, 348, 355, 373, 385, 396, 410, 423, 438, 444, 457, 467, 482, 501, 508, 521, 534, 545, 555, 562, 587, 595, 603, 612, 629, 641, 656, 670, 675, 685, 698, 714, 734, 725, 740, 747, 763, 776, 796, 805, 824, 824, 842, 854, 869, 874, 888, 907, 905, 920, 943, 954, 956, 962, 990, 1024, 1005, 1002, 1048, 1067, 1053, 1069, 1076, 1104, 1091, 1110, 1115, 1131, 1141, 1168, 1168, 1194, 1188, 1195, 1210, 1227, 1235, 1254, 1257, 1266, 1296, 1290, 1308, 1323, 1323, 1343, 1340, 1355, 1375, 1377, 1392, 1397, 1420, 1426, 1448, 1452, 1485, 1479, 1493, 1506, 1509, 1526, 1550, 1547, 1573, 1561, 1577, 1600, 1621, 1608, 1623, 1639, 1643, 1653, 1665, 1672, 1687, 1704, 1715, 1731, 1739, 1753, 1772, 1783, 1784, 1802, 1801, 1803, 1867, 1842, 1876, 1872, 1872, 1887, 1904, 1893, 1911, 1952, 1937, 1951, 1976, 1962, 1984, 2009, 2018, 2044]
try:
  print("This assumes you have logged in and collected all rewards.\nAll time uses the in-game time of Campaign event not other events (+24h)."+newline)
  while type(hours) == str and zero_time_check == True:
    hours = input("How many hours are remaining? (in-game timer)\n")
    try:
      hours = int(hours)
      if hours == 192: zero_time_check = False
      elif 0 > hours or hours > 192: print("Please input a valid number of hours. (0-192)")
    except Exception: print("Please input an integer (whole number) for hours.")
  if zero_time_check:
    while type(minutes) == str:
      minutes = input("How many minutes are remaining? (in-game timer)\n")
      try:
        minutes = int(minutes)
        if 0 > minutes or minutes >= 60: print("Please input a valid number of minutes.")
      except Exception: print("\nPlease input an integer (whole number) for minutes.")
    while type(current) == str:
      if refund == True:
        current = input("How many campaign items do you currently have?\nIf the negative number was due to a refund, please type \"refund\" below.\n")
        if current in ["refund","Refund"]: current = currentrefundamount
        else: refund = False
      else:
        current = input("How many campaign items do you currently have?\n")
        try:
          current = int(current)
          if current < 0: refund, currentrefundamount, current = True, current, "refund?"
        except Exception: print("\nPlease input an integer (whole number) for current items.")
    while type(spent) == str:
      spent = input("How many items have been spent on rewards?\n")
      try:
        spent = int(spent)
        if hours < 24 or (hours == 24 and minutes == 0): raise GeneratorExit
      except Exception: print("\nPlease input an integer (whole number) for items spend on rewards.")
    while type(extra) == str:
      extra = input("How many items are from purchased packs, crystals, or other event sources?\nThis includes the additional event rewards from Imp's Adventure.\n")
      try: extra = int(extra)
      except Exception: print("\nPlease input an integer (whole number) for items purchased.")
    while type(custominput) == str:
      custominput = input("Do you want to know the probability to reach a certain number of items?\nIf yes, then type number below. If no, then type \"none\".\n")
      try:
        if custominput in ["none", "None", "No", "no", "0", "2500"]: 
          custominput="none"
          break
        else:
          custominput = int(custominput)
          if custominput < current: 
            print("\nInput number must be greater than current items.\nPlease input an integer (whole number) for custom lookup or type \"none\".")
      except Exception: print("\nPlease input an integer (whole number) for custom lookup or type \"none\".")
  else:
    while type(impsbool)==str:
      impsbool = input("Is Imp's Adventure Giving Campaign Rewards? (Yes/No)\nOutput given will be of F2P Imp's typical progression.\n")
      try:
        if impsbool in ["Yes","yes","Y","y"]: impsbool=True
        elif impsbool in ["No","no","N","n"]: impsbool=False
        else: print("Please input \"Yes\" or \"No\".")
      except Exception: print("Please input \"Yes\" or \"No\".")

  def zcalc(curr, now, hoursleft, day):
    hrfloor, hrceil = math.floor(hoursleft), math.ceil(hoursleft)
    try:
      if (minutes == 0):
        stdvpredicted = stdv[hrfloor - 1]
      else:
        stdvpredicted =(stdv[hrceil - 1] - stdv[hrfloor - 1]) /(hrceil - hrfloor) * (hoursleft - hrfloor) + stdv[hrfloor - 1]
    except Exception:
      stdvpredicted = 1.05977357360136 * 10 + 6.95546690304286 * 10**(-1) * hoursleft - 1.67571179241219 * 10**(-2) * hoursleft**2 + 5.05383084475387 * 10**(-4) * hoursleft**3 - 1.17803724420283 * 10**(-5) * hoursleft**4 + 1.9390541003977 * 10**(-7) * hoursleft**5 - 2.18168285848933 * 10**(-9) * hoursleft**6 + 1.62938690786485 * 10**(-11) * hoursleft**7 - 7.68703295853448 * 10**(-14) * hoursleft**8 + 2.06664417836592 * 10**(-16) * hoursleft**9 - 2.40708085158142 * 10**(-19) * hoursleft**10
    try:
      if (minutes == 0):
        stdvdone = stdv[167 - hrfloor]
      else:
        stdvdone = (stdv[167 - hrfloor] - stdv[168 - hrceil]) /(hrceil - hrfloor) * (hoursleft - hrfloor) + stdv[168 - hrceil]
    except Exception:
      stdvdone = 1.05977357360136 * 10 + 6.95546690304286 * 10**(-1) * (168 - hoursleft) - 1.67571179241219 * 10**(-2) * (168 - hoursleft)**2 + 5.05383084475387 * 10**(-4) * (168 - hoursleft)**3 - 1.17803724420283 * 10**(-5) * (168 -hoursleft)**4 + 1.9390541003977 * 10**(-7) * (168 - hoursleft)**5 - 2.18168285848933 * 10**(-9) * (168 - hoursleft)**6 + 1.62938690786485 * 10**(-11) * (168 - hoursleft)**7 - 7.68703295853448 * 10**(-14) * (168 - hoursleft)**8 + 2.06664417836592 * 10**(-16) * (168 - hoursleft)**9 - 2.40708085158142 * 10**(-19) * (168 - hoursleft)**10
    
    def prob(zscore):
      prob=round(norm.cdf(zscore)*100,3)
      if prob>0.5:return (prob, "or lower")
      elif prob<0.5: return (100-prob, "or higher")
      else: return (50,"")
    def custgoal(goal):return "{:.2f}%".format(round(100*(1-norm.cdf((goal - current + 100 * day - 1774.08 / 168 * hoursleft) / stdvpredicted)),2))
    def multi(zscore):
      multis={6:4.75342, 5:4.29443, 4:3.71902, 3:3.06372, 2:2.60238, 1:1.91452}
      if zscore < multis[1]: return 0
      for i, mult in list(multis.items()): 
        if zscore >= mult: return i

    znow = (now - 100 * day - 1774.08 / 168 * (168 - hoursleft)) / stdvdone
    zcurr = (curr - current + 100 * day -1774.08 / 168 * hoursleft) / stdvpredicted
    nowprob, currprob = prob(znow),  prob(zcurr)
    zonenow, zonecurr=multi(abs(znow)), multi(abs(zcurr))
    
    try:
      custom=custgoal(custominput-700)
    except Exception:custom="none"
    return (nowprob, zonenow, currprob, zonecurr, stdvpredicted, custgoal(1800), custom)

  def campaigncalc():
    f2p = current - extra + spent
    hoursleft = hours + minutes / 60 - 24
    day = math.ceil(7 - hoursleft / 24)

    estavg = math.floor(current + hoursleft * 10.56 + (7 - day) * 100)
    estcurr = math.floor(current + (f2p - day * 100) / (168 - hoursleft) * hoursleft +(7 - day) * 100)
    return ((7 - day, estavg, estcurr, f2p - day * 100), zcalc(estcurr - 700, f2p, hoursleft, day))

  try:
    if zero_time_check:
      odds = {1:"rolling the same number on a dice three times in a row",2:"rolling the same number on a dice four times in a row",3:"getting 3 5* in a 10 pull of heroic scrolls",4:"getting injured by a toilet or finding a four-leaf clover",5:"being struck by lightning",6:"truly being 1 in a million"}
      results, zstat = campaigncalc()
      def timestr(left, name):return f"{f'{left} {name}' if left>0 else ''}{'s' if left>1 else ''}"

      head = f"{newline}\nTime Remaining: {timestr(results[0],'day')} {timestr(hours-24*results[0]-24,'hour')} {timestr(minutes,'minute')}\nDaily Loot Remaining: {100*results[0]} Items"
      money=f"\nTotal items purchased: {extra} Items" if extra>0 else ""
      spend="\nTotal items spent: {spent} Items" if spent>0 else ""

      curr=(f"\nPredicted Item Count (current rate): {results[2]} Items", newline) if results[3]>0 else ("","\n")
      avg2rng=f"\n\nPredicted Item Count (average rate): {results[1]} Items%s\nPredicted range: {math.floor(results[1]-zstat[4])}-{math.floor(results[1]+zstat[4])} Items%s" % (curr)
      miss=f"{newline}\nYou have missed daily rewards this event.\nA current rate will not be given.{newline}"

      prob2500="\nYou have a "+zstat[5]+" chance to reach 2500 items for eminent chest." if current + spent <2500 else ""
      custprob="\nYou have a "+zstat[6]+" chance to reach "+str(custominput)+" items by end of event." if custominput!="none" and current + spent < custominput else ""
      customprobs=f"{prob2500}\n{custprob}" if custprob!=prob2500 else f"{prob2500}{custprob}"

      currperc="\nYou have a {:.3f}% to be {} items {} by the end of the event.".format(zstat[2][0], results[2], zstat[2][1])
      time=f"{timestr(math.floor(192-hours-minutes/60),'hour')}{' and ' if math.floor(192-hours-minutes/60)>0 and minutes%60>0 else ''}{timestr(minutes%60,'hour')} into event."
      nowperc="\nYou have a {:.3f}% to be {} items {} at {}".format(zstat[0][0], results[2], zstat[0][1], time)
      currodd=f"\n~~These odds are lower than {odds[zstat[3]]}.~~\n" if zstat[3]>0 else ""
      nowodd=f"\n~~These odds are lower than {odds[zstat[1]]}.~~" if zstat[1]>0 else ""
      
      if results[3]<0:print( f"{head}{money}{spend}{avg2rng}{customprobs}{miss}" )
      else:print( f"{head}{money}{spend}{avg2rng}{customprobs}{currperc}{currodd}{nowperc}{nowodd}{newline}" )
    
    elif impsbool:
      impschance, impschance2 = [.00478, .24791, .6058, .13849, .00301, .00001], [0,0,.00025, .01799, .16028, .47569, .30333, .04214, .00032]
      def impchance(arr): return [100*(1-norm.cdf((1800 - 1774.08 - 50*i ) / stdv[-1]))*arr[i] for i in range(len(arr))]
      print("\n----------------------------------------------------------\nTime Remaining: 7 days\nDaily Loot Remaining: 700 Items\n\nBase Camapaign (No Imps) - \nPredicted Item Count (average rate): 2474 Items\nPredicted range: 2421-2526 Items\n\nYou have a {:.2f}% chance to reach eminent chest without gems on Imps Adventure.\nYou have a {:.2f}% chance to reach eminent chest with gems on Imps Adventure.\n----------------------------------------------------------\nEvent has not started.\nA current rate will not be given.\n----------------------------------------------------------".format(round(sum(impchance(impschance2)),2), round(sum(impchance(impschance)),2)))
    else:
      print("\n----------------------------------------------------------\nTime Remaining: 7 days\nDaily Loot Remaining: 700 Items\n\nPredicted Item Count (average rate): 2474 Items\nPredicted range: 2421-2526 Items\nYou have a {:.2f}% chance to reach 2500 items for eminent chest.\n----------------------------------------------------------\nEvent has not started.\nA current rate will not be given.\n----------------------------------------------------------".format(round(100*(1-norm.cdf((1800 - 1774.08 ) / stdv[-1])),2)))

  except Exception as err:
    print(f"An error has occured\n{err}\nPlease contact me on reddit or discord with the error above.")
except GeneratorExit:
  if type(current)==str or type(spent)==str:print("\n----------------------------------------------------------\nWhats the point of the calculator if the event is over?\nYou already know the values with 100% certainty.")
  else:print(f"\n----------------------------------------------------------\nWhats the point of the calculator if the event is over?\nYou already know the values with 100% certainty.\nFinishing Item Count: {current+spent} Items")
except Exception as err:
  print(f"An error has occured\n{err}\nPlease contact me on reddit or discord with the error above.")