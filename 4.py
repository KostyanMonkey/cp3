years = int(input("Введите колличество лет: "))
days = (years // 4) * 366 + (years - years // 4) * 365
inday = 8 * 60 // 5 
print ("Столько картин можно посмотреть", inday * days)
arts = int(input("Введите колличество картин: "))
time = 5 * arts 
timeHours = time // 60
timeDays = timeHours // 8
timeYears = timeDays // 365
vesYears = timeYears // 4
print("Вам понадобится", timeYears, "лет,", timeDays - (timeYears - vesYears ) * 365 - vesYears*366, "дней,", timeHours - timeDays * 8, "часов,", time - timeHours * 60 , "минут")

