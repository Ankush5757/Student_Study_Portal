# Generated by Django 5.1.3 on 2024-11-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_homework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
    ]
