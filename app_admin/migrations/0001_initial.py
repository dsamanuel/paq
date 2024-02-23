# Generated by Django 4.2.10 on 2024-02-22 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.country')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.region')),
            ],
        ),
        migrations.CreateModel(
            name='Woreda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.zone')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.portfolio_type')),
            ],
        ),
        migrations.CreateModel(
            name='FieldOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_admin.region')),
                ('woreda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_admin.woreda')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_admin.zone')),
            ],
        ),
    ]
