>>> from customer.models import Customer
>>> my_new_customer = Customer()
>>> my_new_customer.name = "ABC Corp. - Stone Pollock"
>>> my_new_customer.email = "abccorpsp@email.com"
>>> my_new_customer.save()
>>> xyz_corp = Customer()
>>> xyz_corp.name = "XYZ Corporation"
>>> xyz_corp.email = "xyzcorporationsp@email.com"
>>> xyz_corp.save()
>>> quit(0
... )
>>> from customer.models import Customer
>>> Customer.objects.get(pk=1)
<Customer: Customer object (1)>
>>> customer_one = Customer.objects.get(pk=1)
>>> customer_one.name
'ABC Corp. - Stone Pollock'
>>> customer_one.name = "Some new Name - Stone Pollock"
>>> customer_one.save()
>>> xyz_corp.name = "XYZ Corporation - Stone Pollock"
Traceback (most recent call last):       
  File "<console>", line 1, in <module>  
NameError: name 'xyz_corp' is not defined
>>> Customer.objects.get(pk=2) 
<Customer: Customer object (2)>
>>> customer_two = Customer.objects.get(pk=2) 
>>> customer_two.name = "XYZ Corporation - Stone Pollock"
>>> customer_two.save()
>>> customer_one.delete()
(1, {'customer.Customer': 1})
>>> Customer.objects.create(name="Plumbing Solutions - Stone Pollock",email="plumbingsolutionssp@email.com")  
<Customer: Customer object (3)>
>>> Customer.objects.create(name="Electronics Experts - Stone Pollock",email="electronicsexpertssp@email.com")  
<Customer: Customer object (4)>
>>>
KeyboardInterrupt
>>> Customer.objects.create(name="Structural Consultants - Stone Pollock",email="structuralconsultantssp@email.com") 

<Customer: Customer object (5)>
>>> customer = Customer.objects.get(name='Electronics Experts - Stone Pollock')
>>> customer.name
'Electronics Experts - Stone Pollock'
>>> results = Customer.objects.filter(name__startswith=("Plumb"))
>>> results.count()
1
>>> results[0].name
'Plumbing Solutions - Stone Pollock'
>>> customer = Customer.objects.all()
>>> customer.count()
4
>>> results = Customer.objects.exclude(name__startswith=("Plumb"))
>>> results.count()
3
>>> results[0].name
'XYZ Corporation - Stone Pollock'
>>> results[1].name 
'Electronics Experts - Stone Pollock'
>>> results[2].name 
'Structural Consultants - Stone Pollock'
>>> customers = Customer.objects.all()
>>> customers
<QuerySet [<Customer: Customer object (2)>, <Customer: Customer object (3)>, <Customer: Customer object (4)>, <Customer: Customer object (5)>]>
>>> customers[0]
<Customer: Customer object (2)>
>>> customers[0].name
'XYZ Corporation - Stone Pollock'
>>> customers[1].name
'Plumbing Solutions - Stone Pollock'
>>> from customer.models import Order   
>>> the_customer = Customer.objects.get(pk=4)
>>> order1 = Order(customer=the_customer,total_price=34.99,total_items=3)
>>> order1.save()
>>> order2 = Order(customer=the_customer,total_price=16.99,total_items=6) 
>>> order2.save() 
>>> a_customer = Customer.objects.get(pk=2) 
>>> order3 = Order(customer=a_customer,total_price=81.99,total_items=4)    
>>> order3.save()
>>> some_customer = Customer.objects.get(pk=3)  
>>> order4 = Order(customer=some_customer,total_price=41.99,total_items=5)     
>>> order4.save()