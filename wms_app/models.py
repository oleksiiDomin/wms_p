from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Model
from django.utils import timezone


# from rest_framework.utils import timezone


class Seller(Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}, {self.country}, {self.city}'



class Material(Model):
    lot = models.CharField(max_length=50)
    current_balance = models.PositiveIntegerField(validators=[MaxValueValidator(10000000)])
    weight_of_lot = models.PositiveIntegerField(validators=[MaxValueValidator(40000)])
    seller = models.ForeignKey(Seller, related_name='materials', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.lot}: | Balance - {self.current_balance} | Weight of lot - {self.weight_of_lot} | Seller -{self.seller.name}'



class Calcium(Material):

    def save(self, *args, **kwargs):
        self.current_balance = self.weight_of_lot
        super().save(*args, **kwargs)



class CalciumSilicon(Material):

    def save(self, *args, **kwargs):
        self.current_balance = self.weight_of_lot
        super().save(*args, **kwargs)



class Carbon(Material):
    carbon_content = models.FloatField(validators=[MaxValueValidator(100.00)])
    sulfur_content = models.FloatField(validators=[MaxValueValidator(100.0)])

    def __str__(self):
        return f'{self.lot}: | Balance - {self.current_balance} | Weight of lot - {self.weight_of_lot} | Seller -{self.seller.name} | Carbon -{self.carbon_content} | Sulfur -{self.sulfur_content}'

    def save(self, *args, **kwargs):
        self.current_balance = self.weight_of_lot
        super().save(*args, **kwargs)



class MetalStrip(Material):
    thickness = models.FloatField(
        validators = [
            MaxValueValidator(1.0),
            MinValueValidator(0.1)
        ]
    )
    width = models.PositiveIntegerField(
        validators = [
            MaxValueValidator(80),
            MinValueValidator(30)
        ]
    )

    def __str__(self):
        return f'{self.lot}: | Balance - {self.current_balance} | Weight of lot - {self.weight_of_lot} | Seller -{self.seller.name} | Thickness - {self.thickness} | Width - {self.width}'

    def save(self, *args, **kwargs):
        self.current_balance = self.weight_of_lot
        super().save(*args, **kwargs)



class MetalShot(Material):
    diameter = models.FloatField(
        validators=[
            MaxValueValidator(3.0),
            MinValueValidator(0.1)
        ]
    )

    def __str__(self):
        return f'{self.lot}: | Balance - {self.current_balance} | Weight of lot - {self.weight_of_lot} | Seller -{self.seller.name} | Diameter - {self.diameter}'

    def save(self, *args, **kwargs):
        self.current_balance = self.weight_of_lot
        super().save(*args, **kwargs)



class Customer(Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}, {self.country}, {self.city}'



class WireType(models.TextChoices):
    CK30 = "CK-30", "CK-30"
    CK40 = "CK-40", "CK-40"
    CaSi = "Ca Si", "Ca Si"
    CAFE30 = "Ca-Fe 30/70", "Ca-Fe 30/70"
    CAFE40 = "Ca-Fe 40/60", "Ca-Fe 40/60"
    C = "C", "C"
    B = 'B', "B"



class Order(Model):
    lot = models.CharField(max_length=50)
    type = models.CharField(choices=WireType.choices, default=WireType.CK30.value, max_length=12)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quality_certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f'{self.lot}: | {self.type} | {self.customer}'



class Coil(Model):
    number = models.CharField(max_length=50)
    type = models.CharField(choices=WireType.choices, default=WireType.CK30.value, max_length=12)
    length = models.PositiveIntegerField(validators=[MaxValueValidator(7000)])
    filling = models.PositiveIntegerField(validators=[MaxValueValidator(1500)])
    metal_shel = models.PositiveIntegerField(validators=[MaxValueValidator(500)])
    weight = models.PositiveIntegerField(validators=[MaxValueValidator(3000)])
    customer = models.ForeignKey(Customer, related_name='coils', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, related_name='coils', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.number}: {self.type}, {self.weight}, {self.customer.name}'



class IncludedMaterial(Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(20000)])

    def __str__(self):
        return f'Material - {self.order.type}: | Customer - {self.order.customer.name} | Quantity - {self.quantity} | Material LOT - {self.material.lot }'

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.material.current_balance -= self.quantity
            if self.material.current_balance < 0:
                raise ValueError(f"Insufficient balance for {self.material.name}")


            if self.material.current_balance < 41000:
                send_low_stock_email(self.material)


            self.material.save()
        super().save(*args, **kwargs)

    def update(self, instance, validated_data):
        if self.material.current_balance < 0:
            raise ValueError(f"Insufficient balance for {self.material.lot}")
        if self.material.current_balance < 12100:
            print(f'Attention!: Low count of balance. Current balance: {self.material.current_balance}')

        super().update(instance, validated_data)

def send_low_stock_email(material):
    subject = f"Low Stock Alert: {material.lot}"
    message = f"The stock for {material.lot} is low. Only {material.current_balance} units left."
    recipient_list = ['o.domin16@gmail.com', 'daria.tertyshnaya5@gmail.com']
    send_mail(subject, message, 'from@example.com', recipient_list)



class CustomerCoilRelation(Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coil = models.ForeignKey(Coil, on_delete=models.CASCADE)
    like = models.BooleanField()
    feedback = models.CharField(max_length=1000)

    RATE_CHOICES = (
        (1, 'Terrible'),
        (2, 'Bad'),
        (3, 'Norman'),
        (4, 'Good'),
        (5, 'Excellent')
    )