from django.db import models

# Create your models here.


class BlockM001(models.Model):
    BlockName = models.CharField(max_length=4, default="M001")  #TODO: FIXED VALUE FIELD
    Informed = models.BooleanField()


class BlockM010(models.Model): #TODO: VALIDATOR -> MANDATORY FIELDS
    BlockName = models.CharField(max_length=4, default="M010")  #TODO: FIXED VALUE FIELD
    BAccountCode = models.CharField()
    BAccountDesc = models.CharField()
    AccountCreatedDate = models.DateField(max_length=8)  #TODO: VALIDATOR-> LOWER THAN FINAL DATE
    DefaultTableCode = models.CharField(max_length=6)  #TODO: VALIDATOR CODE OF THE DEFAULT TABLE SEE ECF MANUAL
    LimitDate = models.DateField(max_length=8)  #NOT MANDATORY
    TaxCode = models.CharField(max_length=1)  #TODO: VALIDATOR(ONLY ACCEPTS [I;C])
    InitialBalance = models.DecimalField(max_length=19, max_digits=2)
    InitialBalanceInd = models.CharField(max_length=1)  #TODO: VALIDATOR(ONLY ACCEPTS [D;C]
    CNPJEspSituation = models.CharField(max_length=14)  #TODO: CNPJ VALIDATOR


class BlockM030(models.Model):
    BlockName = models.CharField(max_length=4, default="M030")  #TODO: FIXED VALUE FIELD
    InitialDate = models.DateField(max_length=8)
    FinalDate = models.DateField(max_length=8)


class BlockM300(models.Model):
    BlockName = models.CharField(max_length=4, default="M300")  #TODO: FIXED VALUE FIELD
    LalurCode = models.IntegerField()  #TODO: ENUMERATE OPTIONS FROM ECF DEFAULT TABLE
    LalurName = models.CharField()  #TODO: FROM LALUR CODE
    AdjustmentType = models.CharField(max_length=1)  #TODO: VALIDATOR ONLY [A;E;P;L]
    RelationType = models.CharField(max_length=1)  #TODO: VALIDATOR ONLY [1;2;3;4]
    Value = models.DecimalField(max_length=19, max_digits=2)
    Comments = models.CharField(max_length=500)


class BlockM305(models.Model):
    BlockName = models.CharField(max_length=4, default="M305")  # TODO: FIXED VALUE FIELD
    BAccountCode = models.CharField()
    Value = models.DecimalField(max_length=19, max_digits=2)
    ValueInd = models.CharField(max_length=1)  # TODO: VALIDATOR(ONLY ACCEPTS [D;C]
    LalurCode = models.IntegerField()  #TODO: ENUMERATE OPTIONS FROM ECF DEFAULT TABLE
    LalurName = models.CharField()  #TODO: FROM LALUR CODE
    AccountCode = models.CharField()  #From Accounting App - Non-mandatory
    CostCenterCode = models.CharField()  #From Accounting App - Non-mandatory


class BlockM310(models.Model):
    BlockName = models.CharField(max_length=4, default="M310")  # TODO: FIXED VALUE FIELD
    AccountCode = models.CharField()  # From Accounting App
    CostCenterCode = models.CharField()  # From Accounting App
    Value = models.DecimalField(max_length=19, max_digits=2)
    ValueInd = models.CharField(max_length=1)  # TODO: VALIDATOR(ONLY ACCEPTS [D;C]

