

time_second = int(input())

hour,minute,seond = 0,0,0

second = time_second % 60
minute = time_second // 60
hour = minute // 60
minute = (minute % 60)


print("%d:%d:%d" %(hour,minute,second))

