# Generated by Django 5.0.1 on 2024-02-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Display these tags.')),
                ('title', models.CharField(max_length=200, verbose_name='Title tag')),
                ('description', models.TextField(verbose_name='Meta description')),
                ('robots_tag', models.CharField(default='index, follow', max_length=200, verbose_name='Robots tag (index, follow)')),
                ('site_name', models.CharField(max_length=200, verbose_name='og:site_name')),
                ('og_title', models.CharField(max_length=200, verbose_name='og:title')),
                ('og_description', models.TextField(verbose_name='og:description')),
                ('og_image_url', models.URLField(verbose_name='URL for the og:image')),
                ('headtags', models.TextField(blank=True, null=True, verbose_name='HTML Head tags (Google Analytics, Tag managers, others.)')),
            ],
        ),
    ]
