
time1, time2 = map(int, input().split())

if time1 == time2:
    print("O JOGO DUROU 24 HORA(S)")
elif time1 > time2:
    print("O JOGO DUROU %d HORA(S)" %((24-time1)+time2))
else:
    print("O JOGO DUROU %d HORA(S)" %(time2 - time1))