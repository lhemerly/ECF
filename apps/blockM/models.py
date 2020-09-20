from django.db import models

# Create your models here.


class Lalur(models.Model):
    LalurCode = models.IntegerField(primary_key=True)  # TODO: ENUMERATE OPTIONS FROM ECF DEFAULT TABLE
    LalurName = models.CharField(max_length=500)  # TODO: FROM LALUR CODE


class BAccounts(models.Model):
    BAccountCode = models.CharField(max_length=500,
                                    primary_key=True)
    BAccountDesc = models.CharField(max_length=500)


class BlockM001(models.Model):
    BlockName = models.CharField(max_length=4,
                                 default="M001",
                                 editable=False)
    Informed = models.BooleanField()


class BlockM010(models.Model):
    BlockName = models.CharField(max_length=4,
                                 default="M010",
                                 editable=False)
    BAccountCode = models.ForeignKey('BAccounts',
                                     on_delete=models.CASCADE,
                                     blank=False)
    AccountCreatedDate = models.DateField(max_length=8)  # TODO: VALIDATOR-> LOWER THAN FINAL DATE
    DefaultTableCode = models.CharField(max_length=6)  # TODO: VALIDATOR CODE OF THE DEFAULT TABLE SEE ECF MANUAL
    LimitDate = models.DateField(max_length=8,
                                 blank=True)
    TaxCode = models.CharField(max_length=1,
                               choices=[('I', 'IR'),
                                        ('C', 'CSLL')])
    InitialBalance = models.DecimalField(max_length=19,
                                         max_digits=12,
                                         decimal_places=2)
    InitialBalanceInd = models.CharField(max_length=1,
                                         choices=[('D', 'Débito'),
                                                  ('C', 'Crédito')])
    CNPJEspSituation = models.CharField(max_length=14)  # TODO: CNPJ VALIDATOR


class BlockM030(models.Model):
    BlockName = models.CharField(max_length=4,
                                 default="M030",
                                 editable=False)
    InitialDate = models.DateField(max_length=8)
    FinalDate = models.DateField(max_length=8)


class BlockM300(models.Model):
    BlockName = models.CharField(max_length=4,
                                 default="M300",
                                 editable=False)
    LalurCode = models.ForeignKey('Lalur',
                                  on_delete=models.CASCADE,
                                  blank=False)
    AdjustmentType = models.CharField(max_length=1,
                                      choices=[('A', 'Adição'),
                                               ('E', 'Exclusão'),
                                               ('P', 'Compensação de Prejuízo'),
                                               ('L', 'Lucro')])
    RelationType = models.CharField(max_length=1,
                                    choices=[('1', 'Com conta da parte B'),
                                             ('2', 'Com conta contábil'),
                                             ('3', 'Com conta da parte B e conta contábil'),
                                             ('4', 'Sem relacionamento')])
    Value = models.DecimalField(max_digits=12,
                                decimal_places=2)
    Comments = models.CharField(max_length=500)


class BlockM305(models.Model):
    BlockName = models.CharField(max_length=4,
                                 default="M305",
                                 editable=False)
    BAccountCode = models.ForeignKey('BAccounts',
                                     on_delete=models.CASCADE,
                                     blank=False)
    Value = models.DecimalField(max_digits=12,
                                decimal_places=2)
    ValueInd = models.CharField(max_length=1,
                                choices=[('D', 'Débito'),
                                        ('C', 'Crédito')])
    LalurCode = models.ForeignKey('Lalur',
                                  on_delete=models.CASCADE,
                                  blank=False)
    LalurName = models.CharField(max_length=500)  # TODO: FROM LALUR CODE
    AccountCode = models.ForeignKey('accounting.Accounts',
                                    on_delete=models.CASCADE)
    CostCenterCode = models.ForeignKey('accounting.CostCenters',
                                       on_delete=models.CASCADE)


class BlockM310(models.Model):
    BlockName = models.CharField(max_length=4,
                                 default="M310",
                                 editable=False)
    AccountCode = models.ForeignKey('accounting.Accounts',
                                    on_delete=models.CASCADE)
    CostCenterCode = models.ForeignKey('accounting.CostCenters',
                                       on_delete=models.CASCADE)
    Value = models.DecimalField(max_digits=12,
                                decimal_places=2)
    ValueInd = models.CharField(max_length=1,
                                choices=[('D', 'Débito'),
                                        ('C', 'Crédito')])

