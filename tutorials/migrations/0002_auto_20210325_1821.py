# Generated by Django 3.0.3 on 2021-03-25 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='song',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name_of_song', models.CharField(default='', max_length=70)),
                ('duration', models.IntegerField(default='', max_length=200)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
