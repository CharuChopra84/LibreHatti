# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suspense', '0001_initial'),
        ('catalog', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuspenseOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_order', models.ForeignKey(to='catalog.PurchaseOrder', to_field='id')),
                ('distance', models.IntegerField(default=0)),
                ('is_cleared', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
