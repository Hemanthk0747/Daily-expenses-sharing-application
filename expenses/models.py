from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Expense(models.Model):
    SPLIT_CHOICES = [
        ('equal', 'Equal Split'),
        ('exact', 'Exact Amount'),
        ('percentage', 'Percentage Split')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_paid')
    participants = models.ManyToManyField(User, related_name='expenses_participated')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    split_type = models.CharField(max_length=10, choices=SPLIT_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}'s Expense"
    

class ExactSplit(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class PercentageSplit(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

