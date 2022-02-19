# Generated by Django 3.2.12 on 2022-02-18 05:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_orderitem_expire_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='token',
            new_name='link_download',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='expire_token',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 5, 26, 40, 614138, tzinfo=utc)),
        ),
    ]
