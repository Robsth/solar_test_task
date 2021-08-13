# Generated by Django 3.2.6 on 2021-08-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=150)),
                ('url', models.URLField()),
                ('last_ping_date', models.DateTimeField(auto_now=True)),
                ('availability_status', models.BooleanField(default=False)),
            ],
        ),
    ]