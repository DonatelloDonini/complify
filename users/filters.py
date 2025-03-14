from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
import django_filters
from .models import Todos

class TodosFilter(django_filters.FilterSet):
    state = django_filters.ChoiceFilter(choices=Todos.STATUS)
    date_time_open = django_filters.DateFilter()
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    group1 = django_filters.CharFilter(lookup_expr='icontains')
    group2 = django_filters.CharFilter(lookup_expr='icontains')
    group3 = django_filters.CharFilter(lookup_expr='icontains')
    group4 = django_filters.CharFilter(lookup_expr='icontains')
    
    def __init__(self, *args, **kwargs):
        super(TodosFilter, self).__init__(*args, **kwargs)
        
        # Configura il layout del filtro
        self.helper = FormHelper()
        self.helper.form_method = 'get'
       

# =============================================================================
#     class Meta:
#         model = Todos
#         fields = ['state', 'date_time_open', 'name', 'description']
# =============================================================================


class StandardsItemFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    
    def __init__(self, *args, **kwargs):
        super(StandardsItemFilter, self).__init__(*args, **kwargs)
        
        # Configura il layout del filtro
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        
      
   
class RequestsFilter(django_filters.FilterSet):
    from django_filters import ChoiceFilter
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    state = ChoiceFilter(choices=[('OPEN', 'Aperto'), ('CLOSE', 'Chiuso'), ('WAITING', 'Attesa')])

    
    def __init__(self, *args, **kwargs):
        super(RequestsFilter, self).__init__(*args, **kwargs)
        
        # Configura il layout del filtro
        self.helper = FormHelper()
        self.helper.form_method = 'get'     