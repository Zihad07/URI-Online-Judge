

days = int(input())

year = days//365

remain_days = days % 365
month = remain_days // 30

remain_days = remain_days % 30

print("%d ano(s)" %year)
print("%d mes(es)" %month) 
print("%d dia(s)" %remain_days)