# Generated by Django 3.0.3 on 2020-06-22 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gnen', models.TextField(blank=True, db_column='#query_name', null=True)),
                ('annotations', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Annotations',
                'managed': False,
            },
        ),
    ]