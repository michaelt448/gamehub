# Generated by Django 2.2.2 on 2019-06-29 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('defaultgame', '0007_auto_20190624_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='game_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playerss', to='defaultgame.Games'),
        ),
        migrations.AlterField(
            model_name='players',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rounds',
            name='game_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roundss', to='defaultgame.Games'),
        ),
        migrations.AlterField(
            model_name='turns',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playerss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turns',
            name='round_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turnss', to='defaultgame.Rounds'),
        ),
    ]