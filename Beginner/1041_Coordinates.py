
rersult = {
    '++' : "Q1",
    '-+' : "Q2",
    '--' : "Q3",
    '+-' : "Q4",
    '00' : "Origem",
    'x0' : "Eixo X",
    '0y' : "Eixo Y"
}


answer = ''

x,y = map(float,input().split())

if x==0 and y == 0:
    answer = '00'
elif x == 0 and (y<0 or y>0):
    answer = '0y'
elif y == 0 and (x<0 or x>0):
    answer = 'x0'
elif x > 0 and y > 0:
    answer = '++'
elif x > 0 and y < 0:
    answer = '+-'
elif x < 0 and y > 0:
    answer = '-+'
else:
    answer = '--'


print(rersult[answer])