# Generated by Django 2.0.7 on 2018-07-31 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Заказчик'), (2, 'Исполнитель')], default=1),
        ),
    ]