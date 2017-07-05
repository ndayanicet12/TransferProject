from django.shortcuts import *
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.views.generic import *
from transfers.forms import * 
from transfers.models import *
import random, string
from django.core.exceptions import ValidationError
from django.db.models import Q

###*********** ******************************##########
###******  Function based views *************##########
###*********** ******************************##########
 
def index(request):
    trans =  Transfert.objects.filter(statut='ENVOYE') 
    return render(request, 'transfers/index.html',{'trans':trans})

def listeTransfersPayes(request):
    transfer =  Transfert.objects.filter(statut='RECU') 
    return render(request, 'transfers/listeTransfersPayes.html',{'transfer':transfer})

def calculcios(montant):
    tarifs = Tarif.objects.all()
    cios = 0
    for t in tarifs:
        if t.limit_inferior < montant and montant<= t.limit_superior :
            cios = t.montant
    return cios

def  addtransfer(request):
	 
    if request.method=='POST':
        montant = int(request.POST['montant'])
        print montant
        user = request.user
        guichet = request.user.guichet
        trs = Transfert.objects.create(MTCN=mtcngenerate(), first_namesender=request.POST['first_namesender'], villesender=request.POST['villesender'],last_namesender=request.POST['last_namesender'], montant=montant, commission=calculcios(montant), first_namereceiver=request.POST['first_namereceiver'], last_namereceiver=request.POST['last_namereceiver'], user_sender=user, guichet_sender=guichet)
        trs.save()
	return render(request, 'transfers/addtransfer.html', {'trs':trs})
                  
    else:
        form=TransferForm()
        return render(request, 'transfers/addtransfer.html', {'form':form})


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

def paytransfer(request):
    if request.method=='POST':
       mtcnc=request.POST['MTCN']
       #print mtcnc
       transfer=Transfert.objects.get(MTCN=mtcnc)
 
       if transfer:  
          return render(request, 'transfers/paytransfer.html', {'transfer':transfer})
      #else :
           #return render(request, 'transfers/paytransfererror.html') 
                  
    else:
        form=MTCNForm()
        return render(request, 'transfers/paytransfer.html', {'form':form}) 

def validtransfer(request):
    if request.method=='POST':
       user = request.user  #update_object
       guichet = request.user.guichet
       transfer= Transfert.objects.update(datereceiver=timezone.now(), user_receiver=user, guichet_receiver=guichet,cin = request.POST['cin'])
       return render(request, 'transfers/validtransfer.html', {'transfer':transfer})
                  
    else:
        
        return render(request, 'transfers/paytransfer.html', {})
    

def transferdetail(request, pk):
    #pkid=int(pkid)
    trans = Transfert.objects.get(pk=pk)
    return render(request, 'transfers/transferdetail.html', {'trans': trans})

def transferdetailrecu(request, pk):
    #pkid=int(pkid)
    transfer = Transfert.objects.get(pk=pk)
    return render(request, 'transfers/transferdetailrecu.html', {'transfer': transfer})


def updatetransfer(request, pk):
    transfer=Transfert.objects.get(pk=pk)
    print transfer.montant
    form = PayTransferForm(request.POST or None, instance=transfer)
    #return render(request,'transfers/validtransfer.html', {'form':form})

    user = request.user  #update_object
    guichet = request.user.guichet
    if request.method=='POST':
        trs = Transfert.objects.get(pk=pk)
        trs.cin = request.POST['cin']
        trs.datereceiver=timezone.now()
        trs.villereceiver = request.POST['villereceiver']
        trs.addressereceiver = request.POST['addressereceiver']
        trs.phonereceiver = request.POST['phonereceiver']
        trs.statut="RECU"
        trs.user_receiver=user
        trs.guichet_receiver=guichet
        trs.save()
        print trs.montant, trs.cin
        return render(request,'transfers/validtransfer.html', {'trs':trs})

    else : 
        return render(request, 'transfers/validtransfer.html', {'form':form})

 

###*********** ******************************##########
###******  Class based views ****************##########
###*********** ******************************##########


class CreateTransfer(CreateView):
    form_class=TransferForm
    template_name='transfers/createtransfer.html'
    context_object_name = "transfert"

    def form_valid (self, form):
        instance = form.save(commit=False)
        instance.MTCN = mtcngenerate()
        instance.user_sender=self.request.user
        instance.guichet_sender=self.request.user.guichet
        instance.commission=calculcios(instance.montant)
        instance.save()
 
    def get_success_url(self):
        return reverse('transfers:detailcreatetransfer')



class CreatePayTransfer(CreateView):
    form_class=MTCNForm
    template_name='transfers/createpaytransfer.html'
    context_object_name = "transfer"


    def form_valid (self, form):
        mtcn = self.request.POST 
        transfert = Transfert.objects.get(Q(MTCN=mtcnc) & Q(statut="ENVOYE"))

    def get_success_url(self):
        return reverse('transfers:createpaytransfer')


 
