# Generated by Django 4.2.6 on 2023-10-17 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('question_text', models.TextField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.test')),
            ],
        )

    ]