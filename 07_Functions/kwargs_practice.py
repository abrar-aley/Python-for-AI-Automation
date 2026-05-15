# kwargs practice

def displayInfo(**kwargs):
    for key,value in kwargs.items():
        print(key,' : ',value)

displayInfo(name='Ali',age=22)

displayInfo(city='Islamabad',country='Pakistan', language='Urdu')