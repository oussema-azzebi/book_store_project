# Generated by Django 3.0.5 on 2020-05-22 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.IntegerField(null=True, verbose_name='reference')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('status', models.IntegerField(choices=[(1, 'Available to borrow'), (2, 'Borrowed by someone'), (3, 'Archived - not available anymore')], default=1, verbose_name='status')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('category', models.CharField(choices=[('OTHER', 'Other'), ('ASTRONOMY', 'Astronomy'), ('BIOLOGY', 'Biology'), ('CHEMISTRY', 'Chemistry'), ('HISTORY', 'History'), ('MEDECINE', 'Medecine'), ('MATHEMATICS', 'Mathematics'), ('PSYCHOLOGY', 'Psychology'), ('COMPUTER SCIENCE', 'Computer science'), ('PHILOSOPHY', 'Philosophy')], default='OTHER', max_length=200, verbose_name='category')),
                ('picture', models.TextField(verbose_name='picture URL')),
                ('price', models.IntegerField(null=True, verbose_name='price')),
                ('release_date', models.IntegerField(null=True, verbose_name='release date')),
                ('language', models.CharField(max_length=200, verbose_name='language')),
                ('authors', models.ManyToManyField(blank=True, related_name='books', to='store.Author')),
            ],
            options={
                'verbose_name': 'book',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_site', models.URLField(blank=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('signature', models.TextField(blank=True)),
                ('subscribed_newsletter', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('processed', models.BooleanField(default=False, verbose_name='is processed ?')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'booking',
            },
        ),
    ]
