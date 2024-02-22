from django.db import models

# to import into any module: from shared.models import Report, File

class Report(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    report_text = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    class Meta:
        ordering = ['-submission_date']
        indexes = [
            models.Index(fields=['submission_date', 'status']),
        ]
    def __str__(self):
        return f'{self.id}: {self.report_text}'
    
class File(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    class Meta:
        indexes = [
            models.Index(fields=['report', 'file']),
        ]
    def __str__(self):
        return f'{self.report.id}: {self.file}'
    
    
    