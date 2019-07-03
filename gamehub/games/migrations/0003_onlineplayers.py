# Generated by Django 2.2.3 on 2019-07-02 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0002_games_extras'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlinePlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=500)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='onlineuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]