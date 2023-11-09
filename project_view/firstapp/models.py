from django.db import models

# Create your models here.
class UserDetail(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_fname = models.CharField(max_length=20)
    u_lname = models.CharField(max_length=20)
    u_contact = models.CharField(max_length=13)
    u_address = models.CharField(max_length=50)
    u_email = models.EmailField(max_length=100)
    u_password = models.CharField(max_length=50)

    class Meta:
        db_table = "UserDetail"
