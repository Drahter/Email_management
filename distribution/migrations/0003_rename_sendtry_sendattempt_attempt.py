# Generated by Django 5.1.1 on 2024-09-30 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0002_alter_client_options_delivery_email_client_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SendTry',
            new_name='SendAttempt',
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_last_attempt', models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')),
                ('status_attempt', models.BooleanField(default=False, verbose_name='Статус')),
                ('server_answer', models.TextField(blank=True, max_length=100, null=True)),
                ('delivery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='distribution.delivery', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'попытка',
                'verbose_name_plural': 'попытки',
            },
        ),
    ]
