# Generated by Django 2.2.6 on 2021-04-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210427_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
