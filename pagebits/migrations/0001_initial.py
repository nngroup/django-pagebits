# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField()),
                ('description', models.TextField(help_text='Description show in the admin', blank=True)),
                ('instructions', models.TextField(help_text='Detailed instructions presented at top of the admin form.', blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Bit Group',
                'verbose_name_plural': 'Bit Groups',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('url', models.CharField(help_text="Define the URL for this page, for example 'about/'. NOTE: You should not include the initial slash.", max_length=200, verbose_name='URL', db_index=True)),
                ('bit_groups', models.ManyToManyField(related_name='pages', to='pagebits.BitGroup')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.CreateModel(
            name='PageBit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=0, verbose_name='Bit Type', choices=[(0, b'Plain Text'), (1, b'HTML'), (2, b'Image')])),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('context_name', models.CharField(help_text='This will be the name in the template context.', max_length=100)),
                ('order', models.IntegerField(default=1, verbose_name='Admin form display order')),
                ('text_widget', models.CharField(default=b'charfield', help_text='Which type of input widget to use in admin form for Plain Text fields.', max_length=10, choices=[(b'charfield', 'Text Input Field'), (b'textarea', 'Textarea Input Field')])),
                ('required', models.BooleanField(default=False, help_text='Is this field required?', verbose_name='Required')),
                ('help_text', models.TextField(verbose_name='Optional admin help text', blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('group', models.ForeignKey(related_name='bits', to='pagebits.BitGroup')),
            ],
            options={
                'ordering': ('order', 'created'),
            },
        ),
        migrations.CreateModel(
            name='PageData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.TextField(blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'pagebits/data/images/', blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('bit', models.OneToOneField(related_name='data', to='pagebits.PageBit')),
            ],
            options={
                'verbose_name': 'Page Data',
                'verbose_name_plural': 'Page Data',
            },
        ),
        migrations.CreateModel(
            name='PageTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name shown to user', max_length=100, verbose_name='Name')),
                ('path', models.CharField(help_text="Path to template in TEMPLATE_DIRS, for example 'pages/homepage.html'", max_length=200, verbose_name='Path')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Page Template',
                'verbose_name_plural': 'Page Template',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.ForeignKey(related_name='pages', to='pagebits.PageTemplate'),
        ),
        migrations.CreateModel(
            name='PageEdit',
            fields=[
            ],
            options={
                'ordering': ('name', 'modified', 'created'),
                'verbose_name': 'Edit Page Data',
                'proxy': True,
                'verbose_name_plural': 'Edit Page Data',
            },
            bases=('pagebits.bitgroup',),
        ),
    ]
