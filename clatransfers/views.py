from django.shortcuts import *
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from transfers.forms import * 
from transfers.models import *
import random, string
from django.core.exceptions import ValidationError
from django.db.models import Q 



def calculcios(montant):
    tarifs = Tarif.objects.all()
    cios = 0
    for t in tarifs:
        if t.limit_inferior < montant and montant<= t.limit_superior :
            cios = t.montant
    return cios

def mtcngenerate():
    rand_str = lambda n: "".join([random.choice(string.uppercase) for i in xrange(n)])
    r = rand_str(10)
    s = str(timezone.now()).replace(":","").replace("-","").replace(".","").replace(" ","").replace("+","") 
    value = r + s
    print value
    value_digits=""
    for x in value:
        ord_value = ord(x)
        if 48 <= ord_value <= 57: #0-9
           value_digits +=x
        elif 65 <= ord_value <= 90: # A-Z
           value_digits += str(ord_value-55)
        else:
           print "Invalid MTCN"
           raise ValidationError(_('%s is not a valid character for MTCN.').format(x))
    val=int(value_digits)
    cd=str(int(98-(val % 97)))
    if cd<10:
        cd = "0"+cd
    mtcn=value_digits[:9]+str(cd)
    return str(mtcn)

class ListTransferEnvoye(ListView):
    model=Transfert
    form_class=TransferForm
    template_name='clatransfers/index.html'
    context_object_name = "transfer"
    
    def get_queryset(self):
       return Transfert.objects.filter(Q(statut="ENVOYE")).order_by('-datedepot')

    def get_success_url(self):
        return reverse('clatransfers:index?format=pdf')

    def get_context_data(self, **kwargs):
        context = super(ListTransferEnvoye, self).get_context_data(**kwargs)
        context['action'] = reverse('clatransfers:index')
        return context

class ListTransferRecu(ListView):
    model=Transfert
    template_name='clatransfers/indexrecu.html'
    context_object_name = "transfer"
    
    def get_queryset(self):
       return Transfert.objects.filter(statut="RECU").order_by('-datereceiver')

    def get_success_url(self):
        return reverse('clatransfers:indexrecu')

    def get_context_data(self, **kwargs):
        context = super(ListTransferRecu, self).get_context_data(**kwargs)
        context['action'] = reverse('clatransfers:index')
        return context



class TransferDetail(DetailView):
    model=Transfert
    template_name='clatransfers/detailcreatetransfer.html'
    context_object_name = "transfert"



class TransferDetailRecu(DetailView):
    model=Transfert
    template_name='clatransfers/detailtransfer.html'
    context_object_name = "transfert"

    def get_success_url(self):
        return reverse('clatransfers:detailcreatetransfer')


class CreateTransfer(CreateView):
    model=Transfert
    #form_class=TransferForm
    fields = ('first_namesender', 'last_namesender', 'villesender', 'montant','first_namereceiver', 'last_namereceiver')
    template_name='clatransfers/createtransfer.html'
    context_object_name = "transfert"
    
    def form_valid (self, form):
        print "&&&&&&&&&&&&&&&&&&&&"
        instance = form.save(commit=False)
        instance.MTCN = mtcngenerate()
        instance.user_sender=self.request.user
        instance.guichet_sender=self.request.user.guichet
        instance.commission=calculcios(instance.montant)
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self):
 
       return super(CreateTransfer, self).get_object()

    
 
    def get_success_url(self):
        return reverse('clatransfers:index')

    def get_context_data(self, **kwargs):
        context = super(CreateTransfer, self).get_context_data(**kwargs)
        context['action'] = reverse('clatransfers:index')
        return context



class CreatePayTransfer(UpdateView):
    model=Transfert
    form_class=PayTransferForm
    template_name='clatransfers/createpaytransfer.html'
    context_object_name = "transfer"


    def form_valid (self, form):
        print "&&&&&&&&&&&&&&&&&&&&"
        instance = form.save(commit=False)
        instance.statut = "RECU"
        instance.user_receiver = self.request.user
        instance.guichet_receiver = self.request.user.guichet
        instance.datereceiver = timezone.now()
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self):
 
       return super(CreatePayTransfer, self).get_object()

    def get_success_url(self):
        return reverse('clatransfers:indexrecu')

    def get_context_data(self, **kwargs):
        context = super(CreatePayTransfer, self).get_context_data(**kwargs)
        context['action'] = reverse('clatransfers:index')
        return context


class TransfertCreate(CreateView):
      model= Transfert
      fields = ('first_namesender', 'last_namesender', 'villesender', 'montant','first_namereceiver', 'last_namereceiver')
      template_name='clatransfers/createtransfert.html'

class TransfertUpdate(UpdateView):
      model= Transfert
      fields = ('first_namesender', 'last_namesender', 'villesender', 'montant','first_namereceiver', 'last_namereceiver', 'datereceiver', 'cin', 'addressereceiver','villereceiver', 'phonereceiver')
      template_name='clatransfers/updatetransfert.html'

class TransfertDelete(DeleteView):
      model= Transfert
      success_url = reverse_lazy('clatransfer:index')

def paytransfer(request):
    if request.method=='POST':
       mtcnc=request.POST['MTCN']
       #print mtcnc
       transfer=Transfert.objects.get(MTCN=mtcnc)
 
       if transfer:  
          return render(request, 'clatransfers/paytransfer.html', {'transfer':transfer})
    
    else:
        form=MTCNForm()
    return render(request, 'clatransfers/paytransfer.html', {'form':form}) 

