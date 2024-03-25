from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from storages.backends.s3boto3 import S3Boto3Storage
from django.utils import timezone

# to import into any module: from shared.models import Report, File

class Report(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW'
        PENDING = 'PENDING'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    incident_date = models.DateField(default = timezone.now) # include default for existing models in db
    incident_location = models.CharField(max_length=255, default = 'Unknown')
    students_involved = models.TextField(default = 'Unknown')
    report_text = models.TextField(default = "")
    report_summary = models.TextField(default = 'summary to be provided')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)

    class Meta:
        ordering = ['-submission_date']
        indexes = [
            models.Index(fields=['submission_date', 'status', 'incident_date', 'incident_location']),
        ]
    def __str__(self):
        user_display = self.user.username if self.user else 'Anonymous'
        return f'{self.id}: {user_display} - {self.report_text}'
    
class File(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    file = models.FileField(storage=S3Boto3Storage(), upload_to='uploads/')
    class Meta:
        indexes = [
            models.Index(fields=['report', 'file']),
        ]
    def get_file_url(self):
        return self.file.url
    def __str__(self):
        return f'{self.report.id}: {self.file}'
    
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username}: {self.is_admin}'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    