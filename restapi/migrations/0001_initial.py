# Generated by Django 2.2.4 on 2020-03-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title of message', max_length=100)),
                ('message', models.TextField(help_text='whats on your mind...')),
            ],
        ),
    ]
