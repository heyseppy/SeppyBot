# -*- coding: utf-8 -*-

import cryptocompare
from pyfiglet import Figlet
import time

custom_fig = Figlet(font='graffiti')

print(custom_fig.renderText('SEPBOT'))
def get_latest_crypto_price(n):
    valuetext = cryptocompare.get_avg('BTC', curr='USD', exchange='Kraken')
    return  float(valuetext['PRICE'])


#Income Variables:
totalspendingmoney = 0.00000000
totalbuys = 0
pirooozi_bought_price = get_latest_crypto_price(1)
bitcoin_current_price = get_latest_crypto_price(1)
change = 0

#Code Variables
action_number = 1
piroozi_buylist = []
bitcoin_pricelist = []
state = "just_bought"
cansell = True
sellmoment = "neutral"

profit = 0
#Let it Run:

while (1==1):
    
    bitcoin_current_price = get_latest_crypto_price(1)
    change = (bitcoin_current_price - pirooozi_bought_price) / pirooozi_bought_price
    
    #SELLING FOR A PROFIT:
    if (change > 0.00020000 and state != "just_sold" and state!= "I'm not buying yet" and cansell == True):
         profit = bitcoin_current_price - pirooozi_bought_price
         print(">>>> >>> >>> PROFIT MADE: $" +str(profit))
         cansell = False
         state = "just_sold"
         sellmoment = "profit"
         totalspendingmoney += profit
         f = open('profitmargin.txt','a+') # Not using 'with' just to simplify the example REPL session
         f.write(str(totalspendingmoney) + "\n")
         
    #SELLING FOR A LOSS
    elif (change < -0.000030000 and state != "just_sold" and state!= "I'm not buying yet" and cansell == True):
         profit = bitcoin_current_price - pirooozi_bought_price
         print(">>>> >>> >>> LOSS MADE: $" +str(profit))
         cansell = False
         state = "just_sold"
         sellmoment = "loss"
         totalspendingmoney += profit
         f = open('profitmargin.txt','a+') # Not using 'with' just to simplify the example REPL session
         f.write(str(totalspendingmoney) + "\n")
         
    #BUYING BTC AFTER PROFIT
    elif (change <= -0.00010000 and state != "just_bought" and cansell == False and sellmoment != "loss"):
        pirooozi_bought_price = bitcoin_current_price
        piroozi_buylist.append(pirooozi_bought_price)
        print(">>>> >>> >>> PIROOZI BOUGHT BTC FOR " +str(pirooozi_bought_price) + " --> FROM A PRIOR " +str(sellmoment))
        cansell = True
        totalbuys+= 1
        state = "just_bought"
        
    #BUYING BTC AFTER LOSS    
    elif (change >= 0.00001000 and state != "just_bought" and cansell == False and sellmoment == "loss"):     
        pirooozi_bought_price = bitcoin_current_price
        piroozi_buylist.append(pirooozi_bought_price)
        print(">>>> >>> >>> PIROOZI BOUGHT BTC FOR " +str(pirooozi_bought_price) + " --> FROM A PRIOR loss")
        cansell = True
        totalbuys+= 1
        state = "just_bought"
    
    #HOLDING MONEY
    elif (state != "I'm not buying yet" and state!= "just_sold" and cansell == True):
        state = "just_hold"
    
    #CANT BUY    
    elif(cansell == False and state != "just_hold" and state != "just_hold" and state != "just_bought"):
         state = "I'm not buying yet"
         pirooozi_bought_price = bitcoin_pricelist[action_number-2]
         change = (bitcoin_current_price - pirooozi_bought_price) / pirooozi_bought_price
    
    
    
   
    #APPENDING TO ARRAYS
    bitcoin_pricelist.append(bitcoin_current_price)
    print("")
    print("---------------------------------------------------------------------------")
    print("~~ Current Action Number: #" +str(action_number))
    print("~~ Current Bitcoin Price: $" +str(bitcoin_current_price))
    print("~~ Current Seppy Price: $" +str(pirooozi_bought_price))
    print("~~ Total Money Left:  $"     +str(totalspendingmoney))
    print("~~ Change:  %"     +str(change))
    print("~~ Buys:  > "     +str(totalbuys))
    print("~~ Last Move:  > "     +str(sellmoment))
    print("~~ State:  > "     +str(state))
    
    print("---------------------------------------------------------------------------")
    
    print("")
   
    action_number += 1

    profit = 0
    time.sleep(30)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
