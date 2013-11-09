from django.db import models

# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=200)
    device_desc = models.CharField(max_length=1000)
    last_sent_command = models.CharField(max_length=1000)
    create_date = models.DateTimeField('date added')
    rs232_settings = models.CharField(max_length=200)

    def __unicode__(self):
        return self.device_name
