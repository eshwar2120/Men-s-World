# Generated by Django 3.2.8 on 2021-12-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0007_auto_20211216_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_products',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]