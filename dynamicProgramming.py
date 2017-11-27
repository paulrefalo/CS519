from pprint import pprint

masterList = []

def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
   for cents in range(change + 1):
      coinCount = cents
      newCoin = 1
      coinList = [c for c in coinValueList if c <= cents]

      for coin in coinList:    #[c for c in coinValueList if c <= cents]:
          print('minCoins[cents - coin]/index:' + str(minCoins[cents - coin]) + '/' + str(cents-coin) +  ' and coin:' +  str(coin) + ' and coinCount:' + str(coinCount))

          if minCoins[cents - coin] + 1 < coinCount:   # minCoins[cents - j] + 1 < coinCount
            coinCount = minCoins[cents - coin] + 1
            newCoin = coin

      minCoins[cents] = coinCount
      print(minCoins)
      #coinsUsed[cents] = newCoin
      masterList.append(newCoin)

   return minCoins[change]


def printCoins(coinsUsed, change):
   coin = change
   print("Change in print function is: " + str(change))
   print("coinsUsed in print function is ")
   print(coinsUsed)
   while coin > 0:
      #print(str(coinsUsed[coin]) + " coinsUsed[coin]")
      thisCoin = coinsUsed[coin]
      print(thisCoin)

      coin = coin - thisCoin

def main():
    amnt = 16 #63
    clist = [1,5,9,12,25]
    coinsUsed = [0]*(amnt + 1)
    coinCount = [0]*(amnt + 1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")

    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    coinsUsed = masterList
    print(masterList)

    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    # t = type(coinsUsed)
    # print(str(t))


main()



# coins = [1, 5, 10, 12, 25]
# cents = 63
# for c in coins if c <= cents:

# x = [i for i in range(10) if i % 2 == 0]
# print(x)


'''
Fibonacci example
def fib(n):
	fibValues = [0, 1]
	for i in range(2, n + 1):
		fibValues.append(fibValues[i-1] + fibValues[i-2])
	return fibValues[n]
	
Original
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
   for cents in range(change + 1):
      coinCount = cents
      newCoin = 1
      coinList = [c for c in coinValueList if c <= cents]
      print(coinList)
      for j in coinList:    #[c for c in coinValueList if c <= cents]:
          #print(minCoins[cents - j])
          print(minCoins[cents - j] + 1, cents - j + 1)
          if minCoins[cents - j] + 1 < coinCount:   # minCoins[cents - j] + 1 < coinCount
            coinCount = minCoins[cents - j] + 1
            newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   print(coinsUsed)
   print(minCoins[change])
   print(minCoins)
   return minCoins[change]
   
   
Modified
# print('*  cents:' + str(cents))
# print(coinList)
# print(minCoins[cents - j])
# print('minCoins[cents - j]:' + str(minCoins[cents - j]) +  ' and j:' +  str(j) + ' and coinCount:' + str(coinCount))

def mc3(coinValueList, change, minCoins, coinsUsed):
    r = change
    set_of_coins = coinValueList #[1,2,3]
    # ways = [1] + [0]*target
    # for coin in coins:
    #     for i in range(coin, target+1):
    #         ways[i] += ways[i-coin]
    # print(ways)

    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(r + 1):
        m[0][i] = i
    print(m)

def dpMakeChange2(coinValueList, change, minCoins, coinsUsed):
   print(minCoins)
   for cents in range(change + 1):
      coinCount = cents # from 0 to n + 1
      newCoin = 1
      coinList = [c for c in coinValueList if c <= cents]
      print('*  cents:' + str(cents))
      print(coinList)
      for j in coinList:    #[c for c in coinValueList if c <= cents]:
          #print(minCoins)
          print('minCoins[cents - j]:' + str(minCoins[cents - j]) +  ' and j:' +  str(j) + ' and coinCount:' + str(coinCount))
          #print(minCoins[cents - j] + 1, cents - j + 1)
          if minCoins[cents - j] <= coinCount:   # minCoins[cents - j] + 1 < coinCount
            coinCount = minCoins[cents - j] + 1
            newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
      #masterList.append(newCoin)
   #print(coinsUsed)
   #print(minCoins)
   return minCoins[change]
   
Original from Bryce Boe
def solve_coin_change(coins, value):
    """A dynamic solution to the coin change problem"""

    table = [None for x in range(value + 1)]
    table[0] = []
    for i in range(1, value + 1):
        for coin in coins:
            if coin > i:
                continue
            elif not table[i] or len(table[i - coin]) + 1 < len(table[i]):
                if table[i - coin] != None:
                    table[i] = table[i - coin][:]
                    table[i].append(coin)

    if table[-1] != None:
        print('%d coins: %s' % (len(table[-1]), table[-1]))
    else:
        print('No solution possible')


coins = [1, 2, 4]
value = 11

solve_coin_change(coins, value)
'''