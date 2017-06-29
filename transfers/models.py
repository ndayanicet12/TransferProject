from __future__ import unicode_literals
from django.db import models
from profiles.models import *
from django.core.urlresolvers import reverse, reverse_lazy

# Create your models here.
class Transfert(models.Model):	

    STATUT_CHOICES = (
        ('ENVOYE', 'ENVOYE'),
        ('RECU', 'RECU'),
    )

    last_namesender=models.CharField(max_length=50, verbose_name=(u"Nom de l' expediteur"))
    first_namesender=models.CharField(max_length=30, verbose_name=(u"Prenom de l' expediteur"))
    villesender=models.CharField(max_length=30, default="BUJUMBURA", verbose_name=(u"Ville de l' expediteur"))
    montant=models.IntegerField()
    datedepot=models.DateTimeField(verbose_name=(u'Date du  depot'), auto_now_add=True)
    MTCN=models.CharField(max_length=12, null=True, blank=True, unique=True)
    commission=models.IntegerField(verbose_name=(u'Commission a payer'), null=True, blank=True,)
    last_namereceiver=models.CharField(max_length=50, verbose_name=(u'Nom du  destinateur'))
    first_namereceiver=models.CharField(max_length=30,verbose_name=(u'Prenom du destinataire'))
    cin=models.CharField(max_length=50, null=True, blank=True, verbose_name=(u"Carte nationale d'identite"))
    datereceiver=models.DateTimeField(blank=True, null=True, verbose_name=(u'Date de reception'))
    villereceiver=models.CharField(blank=True, null=True,max_length=50, verbose_name=(u'Ville   du  destinataire'))
    addressereceiver=models.CharField(blank=True, null=True, max_length=30,verbose_name=(u'Adresse du destinataire'))
    phonereceiver=models.CharField(max_length=12, blank=True, null=True, verbose_name=(u'Telephone du destinataire'))
    guichet_sender=models.ForeignKey(Guichet, blank=True, null=True)
    user_sender=models.ForeignKey(User, blank=True, null=True)
    guichet_receiver=models.ForeignKey(Guichet, blank=True, null=True, related_name='guichet_receiver')
    user_receiver=models.ForeignKey(User, blank=True, null=True, related_name='user_receiver')
    statut=models.CharField(max_length=12, default="ENVOYE", choices=STATUT_CHOICES)
	

    def __str__(self):
        return  self.last_namesender 

    def get_absolute_url(self):
        return reverse('transferdetail', kwargs={'pk': self.pk})
                                                                   


class Tarif(models.Model):
	limit_inferior=models.IntegerField(verbose_name=(u'Limite inferieure'))
	limit_superior=models.IntegerField(verbose_name=(u'Limite superieure'))
	montant=models.IntegerField()

	def __str__(self):
	    return  self.montant 






