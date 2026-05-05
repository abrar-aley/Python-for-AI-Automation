#tas 10 paired lists

countries=['Iran','Pakistan','India','Afghanistan','Russia']
capitals=['Tehran','Islamabad','Delhi','Kabul','Moscow']

for country,capital in zip(countries,capitals):
    if country=='Pakistan' and capital=='Islamabad':
        print('The capital of ',country,' is ',capital)

