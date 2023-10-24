from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField


class PersonData(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    organization = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    emails = ArrayField(models.CharField(max_length=256), null=True, blank=True)

    def __str__(self):
        return f"Data of person: {self.name}"


class SocialData(models.Model):
    person = models.ForeignKey(PersonData, related_name='social_data', on_delete=models.CASCADE)

    instagram = models.CharField(max_length=256, null=True, blank=True)
    facebook = models.CharField(max_length=256, null=True, blank=True)
    tiktok = models.CharField(max_length=256, null=True, blank=True)
    paypal = models.CharField(null=True, blank=True)
    twitter = models.URLField(max_length=256, null=True, blank=True)
    snapchat = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"Social data of person: {self.person.name}"

