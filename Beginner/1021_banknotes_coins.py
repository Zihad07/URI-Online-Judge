
money = input() #"576.73"
moneylist = money.split('.') #[576,73]
# print(moneylist)
input_money, input_coin = int(moneylist[0]), int(moneylist[1])

money_of_notes = [100,50,20,10,5,2,1]  # list of note of taka

coins = ['50','25','10','05','01']
print("NOTAS:")
for note in money_of_notes:
    number_of_note = input_money//note
    input_money = input_money - (note*number_of_note)
    if note == 1:
        print("MOEDAS:")
        print(str(number_of_note) + " moeda(s) de R$ " + str(note)+".00")
    else:
        print(str(number_of_note) + " nota(s) de R$ " + str(note)+".00")



for coin in coins:
    number_of_coin = input_coin // int(coin)
    # print(input_coin) for debugginh
    input_coin = input_coin - (int(coin)*number_of_coin)
    print(str(number_of_coin) + " moeda(s) de R$ " +"0." +coin)