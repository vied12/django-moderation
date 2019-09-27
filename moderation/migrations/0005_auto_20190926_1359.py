# Generated by Django 2.2.5 on 2019-09-26 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moderation', '0004_auto_20180918_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderatedobject',
            name='by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moderated_objects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='moderatedobject',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Rejected'), (1, 'Approved'), (2, 'Pending')], default=2, editable=False),
        ),
    ]
