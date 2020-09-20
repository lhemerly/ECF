from django.db import models

# Create your models here.
class BalanceSheet(models.Model):
    Company = models.CharField()
    Date = models.DateField()
    AccountCode = models.CharField()
    AccountName = models.CharField()
    CostCenterCode = models.CharField()
    CostCenterName= models.CharField()
    AccountBalance = models.DecimalField()

class AccountingChart(models.Model):
    AccountCode = models.CharField()
    AccountName = models.CharField()
    CostCenterCode = models.CharField()
    CostCenterName = models.CharField()
    AccountLevel1 = models.CharField() #Assets, Liabilities, Equity or Income Statement
    AccountLevel2 = models.CharField() #Short-Term, Long-Term, Equity, Income Statement
    AccountLevel3 = models.CharField()
    AccountLevel4 = models.CharField()
    AccountLevel5 = models.CharField()
    AccountLevel6 = models.CharField()
    AccountLevel7 = models.CharField()
    ECDAccountCode = models.CharField()
    ECDAccountName = models.CharField()
    ECDAccountGroup = models.CharField()
