from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        abstract = True


# наследуем от Person
class Employee(Person):
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


# наследуем от Person
class Customer(Person):
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)


# связыыываем работника и покупателя
class EmployeeCustomer(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
