# Generated by Django 3.1.2 on 2020-11-06 00:30

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CivicConnect', '0006_auto_20201022_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Cybersecurity'), ('2', 'Police Brutality')], max_length=3)),
                ('template', models.CharField(default='Write Template Here', max_length=5000)),
            ],
        ),
    ]
