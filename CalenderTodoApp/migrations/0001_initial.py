# Generated by Django 3.2 on 2022-05-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createuser', models.TextField()),
                ('createdate', models.CharField(max_length=50)),
                ('todo', models.TextField()),
            ],
        ),
    ]
