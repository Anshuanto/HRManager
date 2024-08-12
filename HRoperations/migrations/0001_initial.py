# Generated by Django 5.0.7 on 2024-07-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('passport_expiry_date', models.DateField()),
                ('brp_expiry_date', models.DateField()),
                ('passport_document', models.FileField(upload_to='documents/passport/')),
                ('brp_document', models.FileField(upload_to='documents/brp/')),
            ],
        ),
    ]
