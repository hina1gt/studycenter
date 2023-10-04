from django.db import models

class StudyCenter(models.Model):
    name = models.CharField('Название', max_length=256)
    def __str__(self):
        return f'{self.name}'

class Teacher(models.Model):
    fullname = models.CharField('Полное имя', max_length=256)
    about = models.TextField('O ceбе', blank=True, null=True)
    experience = models.IntegerField('Опыт работы', blank=True, null=True)
    study_center = models.ForeignKey(
        StudyCenter,
        on_delete=models.CASCADE,
        verbose_name='Учебный центр'
    )
    phone_number = models.CharField('Номер телефона', max_length=13)

    def __str__(self):
        return f'{self.fullname}'
    
class Student(models.Model):
    fullname = models.CharField('Полное имя', max_length=256)
    about = models.TextField('О себе', blank=True, null=True)
    phone_number = models.CharField('Номер телефона', max_length=13)
    study_center = models.ForeignKey(
        StudyCenter,
        on_delete=models.CASCADE,
        verbose_name='Учебный центр'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='Учитель(ница)'
    )
    
    def __str__(self):
        return f'{self.fullname}'
