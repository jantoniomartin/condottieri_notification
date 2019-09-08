# -*- coding: utf-8 -*-


from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(verbose_name='message')),
                ('added', models.DateTimeField(default=datetime.datetime.now, verbose_name='added')),
                ('unseen', models.BooleanField(default=True, verbose_name='unseen')),
                ('archived', models.BooleanField(default=False, verbose_name='archived')),
                ('notice_type', models.ForeignKey(verbose_name='notice type', to='notifications.NoticeType')),
                ('recipient', models.ForeignKey(related_name='received_notices', verbose_name='recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sent_notices', verbose_name='sender', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-added'],
                'verbose_name': 'notice',
                'verbose_name_plural': 'notices',
            },
            bases=(models.Model,),
        ),
    ]
