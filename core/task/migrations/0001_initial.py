# Generated by Django 4.1 on 2022-09-03 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('errorMessage', models.CharField(max_length=100)),
                ('labelButton', models.CharField(max_length=50)),
            ],
        ),
    ]