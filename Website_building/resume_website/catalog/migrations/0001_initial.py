# Generated by Django 4.2.3 on 2023-07-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_cards',
            fields=[
                ('card_ID', models.IntegerField(help_text='card_ID', primary_key=True, serialize=False)),
                ('card_name', models.CharField(help_text='card_name', max_length=255)),
                ('card_type', models.CharField(help_text='card_type', max_length=255)),
            ],
            options={
                'ordering': ['card_ID'],
            },
        ),
    ]