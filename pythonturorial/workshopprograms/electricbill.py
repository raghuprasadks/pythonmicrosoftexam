unit=(int(input('Enter the unit =')))
if(unit<=100):
      unit=unit*1
      print('Amount payeable is =',unit)
elif(unit>100 and unit<=200):
    unit=unit*2-100
    print('Amount payeable is =',unit)
elif(unit>200 and unit<=300):
    unit=unit*3-200
    print('Amount payeable is =',unit)
elif(unit>300):
    unit=unit*4-500
    print('Amount payeable is =',unit)
else:
    print('invalid input')
