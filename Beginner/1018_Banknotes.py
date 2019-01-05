

"""
input
-----
576

output
------
	
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

"""
# input_money = 11257

input_money = int(input())
money_of_notes = [100,50,20,10,5,2,1]  # list of note of taka

print(input_money)
for note in money_of_notes:
    number_of_note = int(input_money/note)
    input_money = input_money - (note*number_of_note)

    print(str(number_of_note) + " nota(s) de R$ " + str(note)+",00")

