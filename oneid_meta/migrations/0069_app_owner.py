# Generated by Django 2.0.13 on 2019-12-24 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0068_auto_20191224_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oneid_meta.Org'),
        ),
    ]