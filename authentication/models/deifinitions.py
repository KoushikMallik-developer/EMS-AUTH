from django.db import models


class AccountType(models.TextChoices):
    EMPLOYEE = "employee", "Employee"
    MANAGER = "manager", "Manager"
    HR = "hr", "HR"
    ADMIN = "admin", "Admin"
    STAFF = "staff", "Staff"
