from django.db import models

class StudentDetails(models.Model):
    name = models.CharField(max_length=100)
    rollnumber = models.CharField(max_length=10, unique=True) #the roll number is unique
    standard = models.CharField(max_length=50)
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Marks(models.Model):
    #forign key linking the studentdetils
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE, related_name='marks')
    subject = models.CharField(max_length=100)
    marks= models.PositiveIntegerField()
    

    def __str__(self):
        return f"{self.student.name} - {self.subject}"


class Score(models.Model):
    #one to one relationship with the  marks
    marks = models.OneToOneField(Marks, on_delete=models.CASCADE, related_name='score')
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.marks.student.name} - {self.grade}"


class PersonalDetails(models.Model):
    #one to one relationship with the  studentdetails
    student = models.OneToOneField(StudentDetails, on_delete=models.CASCADE, related_name='personal_details')
    address = models.TextField()
    parentname=models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.student.name} - Personal Details"
