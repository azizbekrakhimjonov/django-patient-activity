from django.db import models
from datetime import datetime

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile_number = models.CharField(max_length=15)

    class Meta:
        unique_together = ('name', 'age', 'mobile_number')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class PatientActivity(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def duration(self):
        if self.start_time and self.end_time:
            start_dt = datetime.combine(self.date, self.start_time)
            end_dt = datetime.combine(self.date, self.end_time)
            duration = end_dt - start_dt
            total_seconds = duration.total_seconds()
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
        return None

    class Meta:
        ordering = ['date', 'patient']
