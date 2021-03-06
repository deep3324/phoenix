# Generated by Django 3.1.4 on 2020-12-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogTitle', models.CharField(default='', max_length=80)),
                ('Studentname', models.CharField(default='', max_length=50)),
                ('aboutstudent', models.CharField(default='', max_length=500)),
                ('Date', models.CharField(default='', max_length=20)),
                ('Content', models.TextField()),
                ('image', models.ImageField(default='', upload_to='blogs/blog/images')),
                ('studentimage', models.ImageField(default='', upload_to='blogs/student/images')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('year', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_name', models.CharField(default='', max_length=80)),
                ('Event_id', models.CharField(default='', max_length=80)),
                ('image', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80)),
                ('email', models.CharField(default='', max_length=50)),
                ('session', models.CharField(default='', max_length=150)),
                ('department', models.CharField(default='', max_length=20)),
                ('contact', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PreviousEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtype', models.CharField(default='', max_length=50)),
                ('eventname', models.CharField(default='', max_length=50)),
                ('studentname', models.CharField(default='', max_length=50)),
                ('position', models.CharField(default='', max_length=10)),
                ('year', models.CharField(default='', max_length=10)),
                ('department', models.CharField(default='', max_length=30)),
                ('college', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(default='', upload_to='result/images')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UpComingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('desc', models.TextField()),
                ('image', models.ImageField(default='', upload_to='upcomingevents/images')),
            ],
        ),
    ]
