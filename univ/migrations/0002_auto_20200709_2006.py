# Generated by Django 3.0.8 on 2020-07-09 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['start_date'], 'verbose_name': '학과별 일정', 'verbose_name_plural': '학과별 일정'},
        ),
        migrations.AlterModelOptions(
            name='sj',
            options={'ordering': ['sj'], 'verbose_name': '수시/정시', 'verbose_name_plural': '수시/정시'},
        ),
    ]
