# Generated by Django 2.2.3 on 2019-07-12 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exammode', '0001_initial'),
        ('userprofile', '0003_auto_20160728_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='active_exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exammode.ExamAttempt'),
        ),
    ]