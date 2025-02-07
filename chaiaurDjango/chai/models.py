from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


# Create your models here.


class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE=[
        ("ML","MASALA"),
        ("GR","GINGER"),
        ("KL","KIWI"),
        ("PL","PLAIN"),
        ("EL","ELAICHI"),
    ]

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='chais/')
    date_added= models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name  # this will show the name of the chai variety in the admin panel
    


class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews') #this is one to many relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'


#many to many 

class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='store') #this is many to many relationship    dusre table me which name will be there is kinda called related name 

    def __str__(self):
        return self.name
    
#one to one

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=200)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'certificate for {self.chai.name}'