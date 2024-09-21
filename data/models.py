from django.db import models

class Hosteler(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    enrollment_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} - {self.enrollment_number}"  # Updated __str__

class Attendance(models.Model):
    hosteler = models.ForeignKey(Hosteler, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=True)

    def get_hosteler_name(self):
        return self.hosteler.name

    def get_enrollment_number(self):
        return self.hosteler.enrollment_number


    def __str__(self):
        return f'{self.hosteler.name} - {self.date}'
