from django import forms
from profiles.models import User
from transfers.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import *
from crispy_forms.bootstrap import TabHolder, Tab


class TransferForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super(TransferForm, self).__init__(*args, **kargs)
        self.helper = FormHelper()
        
        self.helper.form_class = 'form-vertical'
        self.helper.form_id = 'transfer-form'
      
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        self.helper.form_method = 'post'
        #self.helper.form_action = reverse('transfers:addtransfer')
        self.helper.add_input(Submit('submit', 'Transferer'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
           Fieldset('Details of the sender',
                    Field('first_namesender', 'last_namesender', 'villesender', 'montant', css_class="some-class"),
                    ),
                    #Div( ),),
           Fieldset('Details of the receiver', 
                   Field('first_namereceiver', 'last_namereceiver', style="color: blue;"),
 		)
                )       

    class Meta:
        model = Transfert
        #fields=('first_namesender','last_namesender')
        exclude = ('datedepot','MTCN','datereceiver','guichet','user', 'cin')

class MTCNForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super(MTCNForm, self).__init__(*args, **kargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        #self.helper.form_action = reverse('transfers:addtransfer')
        self.helper.add_input(Submit('submit', 'Rechercher'))
         
    class Meta:
        model = Transfert
        fields=('MTCN',)
        #exclude = ('datedepot','MTCN','datereceiver','guichet','user', 'cin')


class PayTransferForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super(PayTransferForm, self).__init__(*args, **kargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
           self.fields['first_namesender'].widget.attrs['readonly'] = True
           self.fields['last_namesender'].widget.attrs['readonly'] = True
           self.fields['montant'].widget.attrs['readonly'] = True
           self.fields['first_namereceiver'].widget.attrs['readonly'] = True
           self.fields['last_namereceiver'].widget.attrs['readonly'] = True
           self.fields['villesender'].widget.attrs['readonly'] = True
        self.helper = FormHelper()
        
        self.helper.form_class = 'form-vertical'
        self.helper.form_id = 'transfer-form'
      
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        self.helper.form_method = 'post'
        #self.helper.form_action = reverse('transfers:addtransfer')
        self.helper.add_input(Submit('submit', 'Payer Transfert'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
           Fieldset('Details of the sender',
                    Field('first_namesender', 'last_namesender','villesender', 'montant',
                          css_class="some-class"),
                    ),
                    #Div( ),),
           Fieldset('Details of the receiver', 
                   Field('first_namereceiver', 'last_namereceiver', 'cin','villereceiver', 'addressereceiver', 'phonereceiver', style="color: blue;"),
 		)
                )       

    class Meta:
        model = Transfert
        #fields=('first_namesender','last_namesender')
        exclude = ('datedepot','MTCN','guichet_sender','user_sender','guichet_receiver', 'user_receiver','commission', 'datereceiver','statut')




