from django.db import models

# Create your models here.
class BalanceSheet(models.Model):
    CompanyCode = models.CharField(max_length=3)
    CompanyName = models.CharField(max_length=500)
    Date = models.DateField()
    AccountCode = models.CharField(max_length=500)
    AccountName = models.CharField(max_length=500)
    CostCenterCode = models.CharField(max_length=500)
    CostCenterName= models.CharField(max_length=500)
    AccountBalance = models.DecimalField(max_length=500,max_digits=12,decimal_places=2)
    AccountIndicator = models.CharField(max_length=1,
                                        default= 'D',
                                        choices=[('D', 'Débito'),
                                                ('C', 'Crédito')])

class AccountingChart(models.Model):
    AccountCode = models.CharField(max_length=500)
    AccountName = models.CharField(max_length=500)
    CostCenterCode = models.CharField(max_length=500)
    CostCenterName = models.CharField(max_length=500)
    AccountLevel1 = models.CharField(max_length=500) #Assets, Liabilities, Equity or Income Statement
    AccountLevel2 = models.CharField(max_length=500) #Short-Term, Long-Term, Equity, Income Statement
    AccountLevel3 = models.CharField(max_length=500)
    AccountLevel4 = models.CharField(max_length=500)
    AccountLevel5 = models.CharField(max_length=500)
    AccountLevel6 = models.CharField(max_length=500)
    AccountLevel7 = models.CharField(max_length=500)
    ECDAccountCode = models.CharField(max_length=500)
    ECDAccountName = models.CharField(max_length=500)
    ECDAccountGroup = models.CharField(max_length=500)

class Company(models.Model):
    CompanyCode = models.CharField(max_length=3)
    CompanyName = models.CharField(max_length=500)
    CNPJ = models.CharField(max_length=14)  #TODO: CNPJ VALIDATOR