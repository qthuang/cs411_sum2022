# Generated by Django 2.2.5 on 2022-06-24 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, null=True, unique=True, verbose_name='email_address')),
                ('password', models.CharField(max_length=30, null=True, unique=True, verbose_name='password')),
            ],
            options={
                'db_table': 'tb_ProjectUser',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='password'),
        ),
    ]