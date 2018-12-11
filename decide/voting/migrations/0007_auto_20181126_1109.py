# Generated by Django 2.0 on 2018-11-26 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_auto_20181126_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voting',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='voting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='voting.Voting'),
            preserve_default=False,
        ),
    ]
