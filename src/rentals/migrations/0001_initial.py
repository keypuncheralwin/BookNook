# Generated by Django 4.2.6 on 2023-10-21 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('#0', 'rented'), ('#1', 'returned'), ('#2', 'lost'), ('#3', 'delayed')], max_length=2)),
                ('rent_start_date', models.DateField(help_text='When the book was rented')),
                ('rent_end_date', models.DateField(blank=True, help_text='deadline')),
                ('return_date', models.DateField(blank=True, help_text='actual return date', null=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]
