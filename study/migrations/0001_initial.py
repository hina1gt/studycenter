# Generated by Django 4.2.5 on 2023-09-29 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=256, verbose_name='Полное имя')),
                ('about', models.TextField(blank=True, null=True, verbose_name='O ceбе')),
                ('experience', models.IntegerField(blank=True, null=True, verbose_name='Опыт работы')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('study_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.studycenter', verbose_name='Учебный центр')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=256, verbose_name='Полное имя')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('study_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.studycenter', verbose_name='Учебный центр')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.teacher', verbose_name='Учитель(ница)')),
            ],
        ),
    ]
