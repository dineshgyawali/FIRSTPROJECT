# Generated by Django 3.1.5 on 2021-01-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0002_customer_eid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('eID', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=20)),
                ('Address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
