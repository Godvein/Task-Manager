# Generated by Django 5.1.1 on 2024-10-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('complete', models.BooleanField()),
                ('timecomplete', models.DateTimeField()),
                ('registeredtime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
