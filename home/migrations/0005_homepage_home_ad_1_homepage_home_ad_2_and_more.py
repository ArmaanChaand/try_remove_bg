# Generated by Django 5.0.1 on 2024-02-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_aboutpage_contactpage_privacypolicypage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='home_ad_1',
            field=models.TextField(blank=True, null=True, verbose_name='Home Ad Code'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_ad_2',
            field=models.TextField(blank=True, null=True, verbose_name='Home Ad Code'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_ad_3',
            field=models.TextField(blank=True, null=True, verbose_name='Home Ad Code'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_ad_4',
            field=models.TextField(blank=True, null=True, verbose_name='Home Ad Code'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_ad_5',
            field=models.TextField(blank=True, null=True, verbose_name='Home Ad Code'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_ad_6',
            field=models.TextField(blank=True, null=True, verbose_name='Home Ad Code'),
        ),
    ]