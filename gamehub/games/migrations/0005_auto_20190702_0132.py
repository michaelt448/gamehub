# Generated by Django 2.2.3 on 2019-07-02 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20190702_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineplayers',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='onlineuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
