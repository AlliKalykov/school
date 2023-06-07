from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    # related name - это имя, которое будет использоваться для обращения к связанным объектам
    # так как в модели Student мы указали group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # то в модели Group мы можем обращаться к связанным объектам через related_name='students'

    def __str__(self):
        return self.name

class Subject(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name[0]}. {self.last_name}'
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name[0]}. {self.last_name}'
    
class Mark(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    mark = models.IntegerField()

    def __str__(self):
        return f'{self.mark}'
    

class Raspisanie(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject} {self.group}'
