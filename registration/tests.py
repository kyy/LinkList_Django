from django.test import TestCase
import hashlib


password = 'volosatiy'
result = hashlib.sha256(password.encode())
print(result.hexdigest())




# if result.hexdigest() != User.objects.filter(password=password):
#     raise forms.ValidationError("Password is incorrect.")
# print(User.objects.filter(password=password), result.hexdigest(), password)
