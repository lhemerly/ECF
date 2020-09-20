# Generated by Django 3.1.1 on 2020-09-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountCode', models.CharField(max_length=500)),
                ('AccountName', models.CharField(max_length=500)),
                ('CostCenterCode', models.CharField(max_length=500)),
                ('CostCenterName', models.CharField(max_length=500)),
                ('AccountLevel1', models.CharField(max_length=500)),
                ('AccountLevel2', models.CharField(max_length=500)),
                ('AccountLevel3', models.CharField(max_length=500)),
                ('AccountLevel4', models.CharField(max_length=500)),
                ('AccountLevel5', models.CharField(max_length=500)),
                ('AccountLevel6', models.CharField(max_length=500)),
                ('AccountLevel7', models.CharField(max_length=500)),
                ('ECDAccountCode', models.CharField(max_length=500)),
                ('ECDAccountName', models.CharField(max_length=500)),
                ('ECDAccountGroup', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='BalanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyCode', models.CharField(max_length=3)),
                ('CompanyName', models.CharField(max_length=500)),
                ('Date', models.DateField()),
                ('AccountCode', models.CharField(max_length=500)),
                ('AccountName', models.CharField(max_length=500)),
                ('CostCenterCode', models.CharField(max_length=500)),
                ('CostCenterName', models.CharField(max_length=500)),
                ('AccountBalance', models.DecimalField(decimal_places=2, max_digits=12, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyCode', models.CharField(max_length=3)),
                ('CompanyName', models.CharField(max_length=500)),
                ('CNPJ', models.CharField(max_length=14)),
            ],
        ),
    ]
