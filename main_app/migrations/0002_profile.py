# Generated by Django 3.0.5 on 2020-06-22 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=2)),
                ('pet_preference', models.CharField(choices=[('dog', 'Dogs'), ('cat', 'Cats'), ('rabbit', 'Rabbits'), ('small-furry', 'Small, furry animals'), ('horse', 'Horses'), ('bird', 'Birds'), ('scales-fins-other', 'Fish and reptiles'), ('barnyard', 'Barnyard animals')], default='dog', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]