from django.contrib import admin

# Register your models here.
# =============================================================================
# from .models import Actions
# from .models import ActionsItemsStandards
# from .models import AuthGroup
# from .models import AuthGroupPermissions
# from .models import AuthPermission
# from .models import AuthUser
# from .models import AuthUserGroups
# from .models import AuthUserUserPermissions
# from .models import CfFiles
# from .models import CfPeople
# from .models import CfServices
# from .models import DjangoContentType
# from .models import DjangoMigrations
# from .models import DjangoSession
# from .models import EnterprisesPeople
# from .models import Files
# from .models import HeaderActions
# from .models import LocationsEnterprises
# from .models import Todos
# from .models import TypeOfActions
#from .models import DjangoAdminLog
# =============================================================================



from .models import Standards
from .models import SystemLog
from .models import Tenants
from .models import ItemsStandards
from .models import Enterprises
from .models import AuthUserTenants

# =============================================================================
# admin.site.register(Actions)
# admin.site.register(ActionsItemsStandards)
# admin.site.register(AuthGroup)
# admin.site.register(AuthGroupPermissions)
# admin.site.register(AuthPermission)
# admin.site.register(AuthUser)
# admin.site.register(AuthUserGroups)
# admin.site.register(AuthUserUserPermissions)
# admin.site.register(CfFiles)
# admin.site.register(CfPeople)
# admin.site.register(CfServices)
# admin.site.register(DjangoContentType)
# admin.site.register(DjangoMigrations)
# admin.site.register(DjangoSession)
# admin.site.register(Enterprises)
# admin.site.register(EnterprisesPeople)
# admin.site.register(Files)
# admin.site.register(HeaderActions)
# admin.site.register(LocationsEnterprises)
# admin.site.register(Todos)
# admin.site.register(TypeOfActions)
# =============================================================================

class StandardsAdmin(admin.ModelAdmin):
    list_display = ('name','state')
admin.site.register(Standards, StandardsAdmin)

class ItemsStandardsAdmin(admin.ModelAdmin):
    list_display = ('name','standards','group1')
admin.site.register(ItemsStandards, ItemsStandardsAdmin)

class TenantsAdmin(admin.ModelAdmin):
    list_display = ('name','state')
admin.site.register(Tenants, TenantsAdmin)

class SystemLogAdmin(admin.ModelAdmin):
    list_display = ('event','user')
admin.site.register(SystemLog, SystemLogAdmin)

class EnterprisesAdmin(admin.ModelAdmin):
    list_display = ('name','tenants')
admin.site.register(Enterprises, EnterprisesAdmin)

class AuthUserTenantsAdmin(admin.ModelAdmin):
    list_display = ('id','auth_user','tenants')
admin.site.register(AuthUserTenants, AuthUserTenantsAdmin)





