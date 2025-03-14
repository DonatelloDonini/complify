# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import uuid
from datetime import datetime

from .models import OrgChartsItems, Requests, Enterprises,Actions,EnterprisesPeople,OrgCharts,Files,EnterprisesLocations,EnterprisesEnterprises,Assets,ActionsItemsStandards,EnterprisesStandardsItems,Todos,EnterpriseStandards
from django import forms


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Row, Submit, Button, Column, HTML

# from ckeditor.widgets import CKEditorWidget


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Enterprises_crud(forms.ModelForm):
    class Meta:
        model = Enterprises
        fields = ['id','name', 'description','context', 'tenants']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()
        self.fields['tenants'].widget = forms.HiddenInput()
        # self.fields['description'].widget = CKEditorWidget()
        # self.fields['context'].widget = CKEditorWidget()
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('id'),
                Div('tenants'),
                css_class='row'
            ),
            Div(
                Div('name'),

                css_class='row'
            ),
             Div(
                Div('description'),
                css_class='row'
            ),
             Div(
                Div('context'),
                css_class='row'
            ),


            Div(


                Submit('azione', 'Save', css_class='btn btn-primary  d-grid gap-2 d-md-flex justify-content-md-end'),
                Submit('azione', 'Delete',  css_class='btn btn-danger d-grid gap-2 d-md-flex justify-content-md-end',onclick="return confirm('Sei sicuro di voler cancellare?');"),
                css_class='d-grid gap-2 d-md-flex justify-content-md-end' )
        )



class Actions_crud(forms.ModelForm):
    class Meta:
        model = Actions
        fields = ['approved_from', 'state','date_event','writed_from','verified_from','prot', 'name','date_actions','date_expire_actions', 'id', 'type_of_actions', 'enterprises', 'description',  'whoami', 'org_chart_item','cf_services']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()

# =============================================================================
        self.fields['enterprises'].widget = forms.HiddenInput()
        self.fields['prot'].widget = forms.HiddenInput()
        self.fields['type_of_actions'].widget = forms.HiddenInput()
        self.fields['cf_services'].widget = forms.HiddenInput()
        #self.fields['enterprises'].queryset = Enterprises.objects.filter(tenants=ten)
# =============================================================================
        self.fields['id'].required = False  # Imposta il campo ID come non obbligatorio
        # self.fields['description'].widget = CKEditorWidget()
        self.fields['whoami'].widget.attrs['class'] = 'form-select form-select-sm'
        self.fields['org_chart_item'].widget.attrs['class'] = 'form-select form-select-sm'

        self.fields['approved_from'].widget.attrs['class'] = 'form-select form-select-sm'
        self.fields['writed_from'].widget.attrs['class'] = 'form-select form-select-sm'
        self.fields['verified_from'].widget.attrs['class'] = 'form-select form-select-sm'

        self.fields['whoami'].label = 'Firmatario'
        self.fields['org_chart_item'].label = 'Area coinvolta'

        self.fields['approved_from'].label = 'Approvato da'
        self.fields['state'].label = 'Stato'
        self.fields['date_event'].label = 'Data evento'
        self.fields['writed_from'].label = 'Scritto da'
        self.fields['verified_from'].label = 'Verificato da'

        self.fields['description'].label = 'Descrizione'
        self.fields['date_actions'].label = 'Data del documento'

        self.fields['date_expire_actions'].label = 'Scadenza'

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(

                Submit('azione', 'Export Word', css_class='btn btn-warning  d-grid gap-2 d-md-flex justify-content-md-end'),
                css_class='d-grid gap-2 d-md-flex justify-content-md-end' ),
            Div(
                Div('id'),
                Div('prot'),
                Div('enterprises'),
                Div('type_of_actions'),
                Div('cf_services'),
                css_class='row'
            ),
            Div(
                Div('name'),

                css_class='row'
            ),
            Div(
                Div('date_actions', css_class='col-md-6'),
                Div('date_expire_actions', css_class='col-md-6'),

                css_class='row'
            ),
            Div(
                Div('date_event', css_class='col-md-6'),


                css_class='row'
            ),
            Div(
                Div('org_chart_item', css_class='col-md-6'),
                Div('whoami', css_class='col-md-6 '),
                css_class='row'
            ),

            Div(
                Div('writed_from', css_class='col-md-6'),
                Div('verified_from', css_class='col-md-6 '),
                css_class='row'
            ),
            Div(
                Div('approved_from', css_class='col-md-6'),
                Div('state', css_class='col-md-6 '),
                css_class='row'
            ),
            Div(
                Div('description'),
                css_class='row'
            ),


            Div(


                Submit('azione', 'Save', css_class='btn btn-primary  d-grid gap-2 d-md-flex justify-content-md-end'),
                Submit('azione', 'Delete',  css_class='btn btn-danger d-grid gap-2 d-md-flex justify-content-md-end',onclick="return confirm('Sei sicuro di voler cancellare?');"),
                css_class='d-grid gap-2 d-md-flex justify-content-md-end' )
        )





class Enterprises_people_crud(forms.ModelForm):
    class Meta:
        model = EnterprisesPeople
        fields = [ 'id', 'name', 'surname','enterprises','auth_user']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()


class Orgchart_crud(forms.ModelForm):
    class Meta:
        model = OrgCharts
        fields = ['id','name', 'enterprises']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()


class Files_crud(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['id','date_time_create','name', 'enterprises', 'father','type']
    content = forms.FileField(label='Seleziona un file')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()
        self.fields['date_time_create'].widget = forms.HiddenInput()
        self.fields['father'].widget = forms.HiddenInput()
        self.fields['enterprises'].widget = forms.HiddenInput()
        self.fields['type'].widget = forms.HiddenInput()
        self.fields['content'].required = False  # Imposta il campo ID come non obbligatorio
        self.fields['id'].required = False  # Imposta il campo ID come non obbligatorio
        if not self.instance.id:
            # Se l'istanza non ha un ID, crea un campo nascosto con un nuovo UUID casuale
            #self.fields['date_time_create'].initial = datetime.now()
            self.fields['id'] = forms.CharField(initial=str(uuid.uuid4()), widget=forms.HiddenInput())


class FilesDir_crud(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['id','date_time_create','name','father', 'type','enterprises']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()
        self.fields['date_time_create'].widget = forms.HiddenInput()
        self.fields['type'].widget = forms.HiddenInput()
        self.fields['father'].widget = forms.HiddenInput()
        self.fields['enterprises'].widget = forms.HiddenInput()
        self.fields['id'].required = False  # Imposta il campo ID come non obbligatorio
        if not self.instance.id:
            # Se l'istanza non ha un ID, crea un campo nascosto con un nuovo UUID casuale
            #self.fields['date_time_create'].initial = datetime.now()
            self.fields['id'] = forms.CharField(initial=str(uuid.uuid4()), widget=forms.HiddenInput())


class EnterprisesEnterprises_crud(forms.ModelForm):
    class Meta:
        model = EnterprisesEnterprises
        fields = ['id','name', 'enterprises']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()

class Assets_crud(forms.ModelForm):
    class Meta:
        model = Assets
        fields = ['id','name', 'enterprises','type']
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['id'].widget = forms.HiddenInput()

class EnterprisesLocations_crud(forms.ModelForm):
    class Meta:
        model = EnterprisesLocations
        fields = ['id','name', 'enterprises']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()


class ActionsItemsStandards_crud(forms.ModelForm):
    class Meta:
        model = ActionsItemsStandards
        fields = ['id','name', 'actions', 'items_standards']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()




class Todos_crud(forms.ModelForm):
          class Meta:
               model = Todos
               fields = ['id','name','description','note','enterprises', 'todo_template','state','state_requirement','expire', 'enterprises_people', 'type','date_time_open' , 'recurrency_start', 'recurrency_end' ,   'recurrency_every' ,  'recurrency_periodo',  'recurrency_enable' ,'recurrency_id_scheduler']
# =============================================================================
          t = forms.CharField(widget=forms.HiddenInput(), required=False)
          ido = forms.CharField(widget=forms.HiddenInput(), required=False)
          tod = forms.CharField(widget=forms.HiddenInput(), required=False)
# =============================================================================
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                self.fields['id'].widget = forms.HiddenInput()
                self.fields['enterprises'].widget = forms.HiddenInput()
                self.fields['type'].widget = forms.HiddenInput()
                self.fields['recurrency_id_scheduler'].widget = forms.HiddenInput()
                self.fields['todo_template'].widget = forms.HiddenInput()
                # self.fields['description'].widget = CKEditorWidget()
                # self.fields['note'].widget = CKEditorWidget()
                self.fields['state'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['type'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['state_requirement'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['enterprises_people'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['recurrency_every'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['recurrency_enable'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['todo_template'].widget.attrs['class'] = 'form-select form-select-sm'

                self.fields['name'].label = 'Titolo'
                self.fields['description'].label = 'Descrizione'
                self.fields['state_requirement'].label = 'Stato del requisito'
                self.fields['state'].label = 'Stato'
                self.fields['date_time_open'].label = 'Data e ora di creazione'
                self.fields['expire'].label = 'Scadenza'
                self.fields['enterprises_people'].label = 'Assegnato a'
                self.fields['note'].label = 'Note'


                self.fields['recurrency_enable'].label = 'Abilita ricorrenze'
                self.fields['recurrency_start'].label = 'Data inizio'
                self.fields['recurrency_end'].label = 'Data fine'
                self.fields['recurrency_every'].label = 'Unità di misura'
                self.fields['recurrency_periodo'].label = 'Numero di unità'



                self.helper = FormHelper()
                self.helper.layout = Layout(
                    Div(
                        Div('id'),
                        Div('t'),
                        Div('ido'),
                        Div('tod'),
                        Div('enterprises'),
                        Div('todo_template'),
                        Div('type'),
                        Div('recurrency_id_scheduler'),
                        css_class='row'
                    ),
                    Div(
                        Div('name'),

                        css_class='row'
                    ),
                    Div(
                        Div('description'),

                        css_class='row'
                    ),
                    Div(
                        Div('note'),

                        css_class='row'
                    ),

                    Div(
                        Div('state_requirement', css_class='col-md-3'),
                        Div('state', css_class='col-md-3'),
                        Div('date_time_open',css_class='col-md-3'),
                        Div('expire', css_class='col-md-3'),
                        css_class='row'
                    ),
                    Div(

                        Div('enterprises_people',css_class='col-md-3'),
                        css_class='row'
                    ),
               Div(
                   Div('', css_class='row', style='height:20px;'),
                    HTML('<br><h3>Ricorrenze<br</h3><hr class="my-4">'),  # Aggiunta di una riga orizzontale
                    css_class='row'
                ),

               Div(
                   Div('', css_class='row', style='height:20px;'),
                   Div('recurrency_enable',css_class='col-md-3'),
                   Div('', css_class='row', style='height:20px;'),
                   css_class='row'
               ),


                    Div(
                        Div('', css_class='row', style='height:20px;'),
                        Div('recurrency_start',css_class='col-md-3'),
                        Div('recurrency_end',css_class='col-md-3'),
                        Div('recurrency_every',css_class='col-md-3'),
                        Div('recurrency_periodo',css_class='col-md-3'),
                        Div('', css_class='row', style='height:20px;'),
                        css_class='row'
                    ),


                    Div(


                        Submit('action', 'Save', css_class='btn btn-primary  d-grid gap-2 d-md-flex justify-content-md-end'),
                        Submit('action', 'Delete',  css_class='btn btn-danger d-grid gap-2 d-md-flex justify-content-md-end',onclick="return confirm('Sei sicuro di voler cancellare?');"),
                        css_class='d-grid gap-2 d-md-flex justify-content-md-end' )
                )


class EnterprisesStandardsItems_crud(forms.ModelForm):
      class Meta:
           model = EnterprisesStandardsItems
           fields = ['id','name','description']
      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['id'].widget = forms.HiddenInput()
            self.fields['name'].widget = forms.HiddenInput()
            # self.fields['description'].widget = CKEditorWidget()
            self.helper = FormHelper()
            self.helper.layout = Layout(
                    Div(
                        Div('id'),
                        Div('name'),
                        css_class='row'
                    ),
                    Div(
                        Div('description'),

                        css_class='row'
                    ),

                    Div(


                        Submit('azione', 'Save', css_class='btn btn-primary  d-grid gap-2 d-md-flex justify-content-md-end'),
                        Submit('azione', 'Delete',  css_class='btn btn-danger d-grid gap-2 d-md-flex justify-content-md-end',onclick="return confirm('Sei sicuro di voler cancellare?');"),
                        css_class='d-grid gap-2 d-md-flex justify-content-md-end' )
                )







class EnterpriseStandards_crud(forms.ModelForm):
      class Meta:
           model = EnterpriseStandards
           fields = ['id','name','description']
      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['id'].widget = forms.HiddenInput()
            self.fields['name'].widget = forms.HiddenInput()
            # self.fields['description'].widget = CKEditorWidget()
            self.helper = FormHelper()
            self.helper.layout = Layout(
                    Div(
                        Div('id'),
                        Div('name'),
                        css_class='row'
                    ),
                    Div(
                        Div('description'),

                        css_class='row'
                    ),

                    Div(


                        Submit('azione', 'Save', css_class='btn btn-primary  d-grid gap-2 d-md-flex justify-content-md-end'),
                        Submit('azione', 'Delete',  css_class='btn btn-danger d-grid gap-2 d-md-flex justify-content-md-end',onclick="return confirm('Sei sicuro di voler cancellare?');"),
                        css_class='d-grid gap-2 d-md-flex justify-content-md-end' )
                )



class Requests_crud(forms.ModelForm):
          class Meta:
               model = Requests
               fields = ['id','name','enterprise','description', 'whoami', 'actions', 'state', 'date_time_open', 'in_charge','request_category', 'tenant' ]
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['id'].widget = forms.HiddenInput()
                self.fields['tenant'].widget = forms.HiddenInput()
                if not self.instance.id:
                    # Se l'istanza non ha un ID, crea un campo nascosto con un nuovo UUID casuale
                    self.fields['date_time_open'].initial = datetime.now()
                    self.fields['id'] = forms.CharField(initial=str(uuid.uuid4()), widget=forms.HiddenInput())
                # self.fields['description'].widget = CKEditorWidget()
                self.fields['state'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['enterprise'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['actions'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['whoami'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['in_charge'].widget.attrs['class'] = 'form-select form-select-sm'
                self.fields['request_category'].widget.attrs['class'] = 'form-select form-select-sm'

                self.fields['description'].label = 'Descrizione'
                self.fields['state'].label = 'Stato'
                self.fields['whoami'].label = 'Firmatario'
                self.fields['in_charge'].label = 'Assegnato a'
                self.fields['actions'].label = 'Azione intrapresa'
                self.fields['date_time_open'].label = 'Data e ora dell evento'
                self.fields['name'].label = 'Titolo'
                self.fields['request_category'].label = 'Categoria'
                self.fields['enterprise'].label = 'Azienda'



                self.helper = FormHelper()
                self.helper.layout = Layout(
                    Div(
                        Div('id'),
                        Div('tenant'),
                        css_class='row'
                    ),
                    Div(
                        Div('name'),

                        css_class='row'
                    ),

                    Div(
                        Div('date_time_open', css_class='col-md-6'),
                        Div('state', css_class='col-md-6'),

                        css_class='row'
                    ),
                    Div(
                        Div('enterprise',css_class='col-md-6'),
                        Div('request_category',css_class='col-md-6'),

                        css_class='row'
                    ),
                    Div(
                        Div('whoami', css_class='col-md-6'),
                        Div('in_charge', css_class='col-md-6 '),
                        css_class='row'
                    ),
                    Div(
                        Div('description'),
                        css_class='row'
                    ),
                    Div(
                        Div('actions'),

                        Div('', css_class='row', style='height:20px;'),
                        css_class='row'
                    ),


                    Div(


                        Submit('action', 'Save', css_class='btn btn-primary  d-grid gap-2 d-md-flex justify-content-md-end'),
                        Submit('action', 'Delete',  css_class='btn btn-danger d-grid gap-2 d-md-flex justify-content-md-end',onclick="return confirm('Sei sicuro di voler cancellare?');"),
                        css_class='d-grid gap-2 d-md-flex justify-content-md-end' )
                )


class OrgChartsItems_crud(forms.ModelForm):
          class Meta:
               model = OrgChartsItems
               fields = ['id','name' ,'description','orgcharts','orgcharts_items_fk','owner']
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['id'].widget = forms.HiddenInput()
                # self.fields['description'].widget = CKEditorWidget()
                if not self.instance.id:
                    # Se l'istanza non ha un ID, crea un campo nascosto con un nuovo UUID casuale
                    self.fields['id'] = forms.CharField(initial=str(uuid.uuid4()), widget=forms.HiddenInput())



