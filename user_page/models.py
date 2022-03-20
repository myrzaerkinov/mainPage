from django.db import models



from django.db import models
from business_accounts.models import Staff, SalonService
from user.models import User



STATUS_TYPE = [
    ("На прием", "На прием"),
    ("Подтвержден", "Подтвержден")
]
class Records(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    data = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()
    promo_code = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(choices=STATUS_TYPE, max_length=100, default="На прием")

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    service = models.ForeignKey(SalonService, on_delete=models.CASCADE)

