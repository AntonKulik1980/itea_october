degree = 31
sun = True

if degree > 30 and sun == True:
    print('Hot and Sunny')
elif degree > 20:
    print('Comfort')
elif  degree > 10:
    print('Not cold')
elif  degree > 0:
    print('Cold')
else:
    print('Very Cold')