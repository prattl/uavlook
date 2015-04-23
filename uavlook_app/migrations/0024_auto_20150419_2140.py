# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0023_auto_20150419_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='InquiryType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(verbose_name='Type', max_length=240)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contactform',
            name='recipients',
            field=models.CharField(verbose_name='Recipients', max_length=2040, default='lenny+uavlook@prattdev.net', help_text='Recipients for this contact form. Separate multiple email addresses with a comma.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactformsubmission',
            name='contact_form',
            field=models.ForeignKey(to='uavlook_app.ContactForm', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactformsubmission',
            name='inquiry_type',
            field=models.ManyToManyField(to='uavlook_app.InquiryType', db_constraint='Inquiry Type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactformsubmission',
            name='phone',
            field=models.CharField(verbose_name='Phone Number', max_length=240, default=''),
            preserve_default=True,
        ),
    ]
