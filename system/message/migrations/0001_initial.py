# Generated by Django 4.1.2 on 2022-11-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message_contains',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=25)),
                ('receiver', models.CharField(max_length=25)),
                ('message', models.TextField()),
                ('subject', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
