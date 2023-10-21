from django.contrib import admin
from .models import *

models_list = [
    PersonData,
    SocialData,
]

for model in models_list:
    admin.site.register(model)

