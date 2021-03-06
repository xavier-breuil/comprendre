# Generated by Django 3.1.3 on 2020-11-09 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('stop_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteering',
            fields=[
                ('meeting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='meetings.meeting')),
                ('title', models.CharField(max_length=100)),
                ('helper_group', models.ManyToManyField(related_name='volunteering_as_helper', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteering_as_host', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('meetings.meeting',),
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('meeting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='meetings.meeting')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(blank=True, max_length=400, null=True)),
                ('attender_group', models.ManyToManyField(related_name='conf_as_attender', to=settings.AUTH_USER_MODEL)),
                ('speaker_group', models.ManyToManyField(related_name='conf_as_speaker', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('meetings.meeting',),
        ),
    ]
