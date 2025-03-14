# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Actions(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    enterprises = models.ForeignKey('Enterprises', models.DO_NOTHING, db_column='enterprises', blank=True, null=True)
    type_of_actions = models.ForeignKey('TypeOfActions', models.DO_NOTHING, db_column='type_of_actions', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cf_services = models.ForeignKey('CfServices', models.DO_NOTHING, db_column='cf_services', blank=True, null=True)
    date_actions = models.DateField(blank=True, null=True,help_text='gg/mm/aaaa')
    date_expire_actions = models.DateField(blank=True, null=True,help_text='gg/mm/aaaa')
    whoami = models.ForeignKey('EnterprisesPeople', models.DO_NOTHING, db_column='whoami', blank=True, null=True)
    org_chart_item = models.ForeignKey('OrgChartsItems', models.DO_NOTHING, db_column='org_chart_item', blank=True, null=True)
    prot = models.IntegerField(blank=True, null=True)
    approved_from = models.ForeignKey('EnterprisesPeople', models.DO_NOTHING, db_column='approved_from', related_name='actions_approved_from_set', blank=True, null=True)
    writed_from = models.ForeignKey('EnterprisesPeople', models.DO_NOTHING, db_column='writed_from', related_name='actions_writed_from_set', blank=True, null=True)
    verified_from = models.ForeignKey('EnterprisesPeople', models.DO_NOTHING, db_column='verified_from', related_name='actions_verified_from_set', blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    date_event = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'actions'
    def __str__(self):
        return f"{self.type_of_actions}: {self.name} del: {self.date_actions}"


class ActionsActions(models.Model):
    id = models.UUIDField(primary_key=True)
    actions_from = models.UUIDField(blank=True, null=True)
    actions_to = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions_actions'


class ActionsAssets(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    assets = models.ForeignKey('Assets', models.DO_NOTHING, db_column='assets', blank=True, null=True)
    actions = models.ForeignKey(Actions, models.DO_NOTHING, db_column='actions', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions_assets'
    def __str__(self):
        return self.name

class ActionsItemsStandards(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    actions = models.ForeignKey(Actions, models.DO_NOTHING, db_column='actions', blank=True, null=True)
    items_standards = models.ForeignKey('ItemsStandards', models.DO_NOTHING, db_column='items_standards', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions_items_standards'
    def __str__(self):
        return self.name

class Assets(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    enterprises = models.ForeignKey('Enterprises', models.DO_NOTHING, db_column='enterprises', blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets'
    def __str__(self):
        return f"{self.type}-> {self.name}"

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
    def __str__(self):
        return self.username

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserTenants(models.Model):
    id = models.UUIDField(primary_key=True)
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user', blank=True, null=True)
    tenants = models.ForeignKey('Tenants', models.DO_NOTHING, db_column='tenants', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user_tenants'


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AxesAccessattempt(models.Model):
    user_agent = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=1025)
    path_info = models.CharField(max_length=255)
    attempt_time = models.DateTimeField()
    get_data = models.TextField()
    post_data = models.TextField()
    failures_since_start = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axes_accessattempt'
        unique_together = (('username', 'ip_address', 'user_agent'),)


class AxesAccessfailurelog(models.Model):
    user_agent = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=1025)
    path_info = models.CharField(max_length=255)
    attempt_time = models.DateTimeField()
    locked_out = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'axes_accessfailurelog'


class AxesAccesslog(models.Model):
    user_agent = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=1025)
    path_info = models.CharField(max_length=255)
    attempt_time = models.DateTimeField()
    logout_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axes_accesslog'


class CfFiles(models.Model):
    filename = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    content = models.BinaryField(blank=True, null=True)
    enterprises = models.UUIDField(blank=True, null=True)
    father = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cf_files'


class CfPeople(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cf_people'


class CfServices(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cf_services'


class Companies(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    enterprises = models.ForeignKey('Enterprises', models.DO_NOTHING, db_column='enterprises', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EnterpriseStandards(models.Model):
    id = models.UUIDField(primary_key=True)
    enterprises = models.ForeignKey('Enterprises', models.DO_NOTHING, db_column='enterprises', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    standards = models.ForeignKey('Standards', models.DO_NOTHING, db_column='standards', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'enterprise_standards'


class Enterprises(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True)
    tenants = models.ForeignKey('Tenants', models.DO_NOTHING, db_column='tenants', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprises'
    def __str__(self):
        return self.name

class EnterprisesEnterprises(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    enterprises = models.ForeignKey(Enterprises, models.DO_NOTHING, db_column='enterprises', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprises_enterprises'
    def __str__(self):
        return self.name

class EnterprisesLocations(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    enterprises = models.ForeignKey(Enterprises, models.DO_NOTHING, db_column='enterprises', blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprises_locations'
    def __str__(self):
        return self.name

class EnterprisesPeople(models.Model):
    id = models.UUIDField( primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    enterprises = models.ForeignKey(Enterprises, models.DO_NOTHING, db_column='enterprises', blank=True, null=True)
    rolespeople = models.UUIDField(blank=True, null=True)
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'enterprises_people'
    def __str__(self):
        return f"{self.name} {self.surname} ({self.enterprises})"

class Roles(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    org_charts_items = models.ForeignKey('OrgChartsItems', models.DO_NOTHING, db_column='org_charts_items', blank=True, null=True)
    enterprises_people = models.ForeignKey(EnterprisesPeople, models.DO_NOTHING, db_column='enterprises_people', blank=True, null=True)
    roles_type_fk = models.ForeignKey('RolesType', models.DO_NOTHING, db_column='roles_type_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'
    def __str__(self):
        return self.name


class RolesType(models.Model):
    id = models.UUIDField(primary_key=True)
    tenants = models.ForeignKey('Tenants', models.DO_NOTHING, db_column='tenants', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_type'
    def __str__(self):
        return self.name

class EnterprisesStandardsItems(models.Model):
    id = models.UUIDField(primary_key=True)
    enterprises = models.ForeignKey(Enterprises, models.DO_NOTHING, db_column='enterprises', blank=True, null=True)
    standards_items = models.ForeignKey('ItemsStandards', models.DO_NOTHING, db_column='standards_items', blank=True, null=True)
    is_applicable = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    accoutability = models.CharField(db_column='Accoutability', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'enterprises_standards_items'
    def __str__(self):
        return self.name


class Files(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    content = models.BinaryField(blank=True, null=True)
    enterprises = models.UUIDField(blank=True, null=True)
    date_time_create = models.DateTimeField(blank=True, null=True)
    father = models.ForeignKey('self', models.DO_NOTHING, db_column='father', blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    ext_file_link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'
    def __str__(self):
        return self.name




class ItemsStandards(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    standards = models.ForeignKey('Standards', models.DO_NOTHING, db_column='standards', blank=True, null=True)
    group1 = models.CharField(max_length=100, blank=True, null=True)
    group2 = models.CharField(max_length=100, blank=True, null=True)
    group3 = models.CharField(max_length=100, blank=True, null=True)
    group4 = models.CharField(max_length=100, blank=True, null=True)
    name_extended = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    text_item = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'items_standards'
    def __str__(self):
        return self.name

class OrgCharts(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    enterprises = models.ForeignKey(Enterprises, models.DO_NOTHING, db_column='enterprises', blank=True, null=True)
    owner = models.ForeignKey(EnterprisesPeople, models.DO_NOTHING, db_column='owner', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'org_charts'
    def __str__(self):
        return self.name

class OrgChartsItems(models.Model):
      id = models.UUIDField(primary_key=True)
      name = models.CharField(max_length=100, blank=True, null=True)
      description = models.TextField(blank=True, null=True)
      orgcharts = models.ForeignKey(OrgCharts, models.DO_NOTHING, db_column='orgcharts', blank=True, null=True)
      orgcharts_items_fk = models.ForeignKey('self', models.DO_NOTHING, db_column='orgcharts_items_fk', blank=True, null=True)
      owner = models.ForeignKey(EnterprisesPeople, models.DO_NOTHING, db_column='owner', blank=True, null=True)

      class Meta:
          managed = False
          db_table = 'org_charts_items'
      def __str__(self):
          return f"{self.orgcharts.name} -> {self.name} "


class RequestCategory(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_category'
    def __str__(self):
        return self.name

class Requests(models.Model):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    WAITING = 'WAITING'
    STATUS = [
        (OPEN, ('Aperto')),
        (CLOSED, ('Chiuso')),
        (WAITING, ('Attesa')),
    ]
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    eml = models.BinaryField(blank=True, null=True)
    whoami = models.ForeignKey(EnterprisesPeople, models.DO_NOTHING, db_column='whoami', blank=True, null=True)
    actions = models.ForeignKey(Actions, models.DO_NOTHING, db_column='actions', blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True, choices=STATUS,default=OPEN)
    date_time_open = models.DateTimeField(blank=True, null=True)
    in_charge = models.ForeignKey(EnterprisesPeople, models.DO_NOTHING, db_column='in_charge', related_name='requests_in_charge_set', blank=True, null=True)
    request_category = models.ForeignKey(RequestCategory, models.DO_NOTHING, db_column='request_category', blank=True, null=True)
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING, db_column='tenant', blank=True, null=True)
    enterprise = models.ForeignKey(Enterprises, models.DO_NOTHING, db_column='enterprise', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'requests'
    def __str__(self):
        return self.name




class PeopleGroup(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    enterprises = models.UUIDField(blank=True, null=True)
    colour = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people_group'


class Standards(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    text_standard = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'standards'
    def __str__(self):
        return self.name

class SystemLog(models.Model):
    date_time_utc = models.DateTimeField(db_column='date-time-utc', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    event = models.TextField(blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_log'


class Tenants(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    state = models.BigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    ref_enterprise_customer = models.UUIDField(blank=True, null=True)
    ref_person_customer = models.UUIDField(blank=True, null=True)
    ref_person_cf = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenants'
    def __str__(self):
        return self.name

class Todos(models.Model):
    ###            ###
    ### Properties ###
    ###            ###

    MONTH = 'MONTHLY'
    DAY = 'DAILY'
    YEAR = 'YEARLY'

    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    SATISFY = 'SATISFY'
    STATUS_REQ= [
    (OPEN, ('Aperto')),
    (SATISFY, ('Soddisfatto')),
    ]
    STATUS = [
        (OPEN, ('Aperto')),
        (CLOSED, ('Chiuso')),
    ]
    YES = 'YES'
    NO = 'NO'
    YESNO= [
        (YES, ('SI')),
        (NO, ('NO')),
    ]
    RECURRENCY = [
        (DAY, ('Giorni')),
        (MONTH, ('Mesi')),
        (YEAR, ('Anni')),
    ]

    ###         ###
    ### Columns ###
    ###         ###

    id =                      models.UUIDField(primary_key=True)
    name =                    models.CharField(max_length=100, blank=True, null=True)
    description =             models.TextField(blank=True, null=True)
    note =                    models.TextField(blank=True, null=True)
    enterprises =             models.ForeignKey(Enterprises, models.DO_NOTHING, db_column='enterprises', blank=True, null=True)
    type =                    models.CharField(max_length=100, blank=True, null=True)
    state_requirement =       models.CharField(max_length=100, blank=True, null=True, choices=STATUS_REQ,default=OPEN)
    state =                   models.CharField(max_length=100, blank=True, null=True, choices=STATUS,default=OPEN)
    date_time_open =          models.DateTimeField(blank=True, null=True)
    expire =                  models.DateField(blank=True, null=True,help_text='gg/mm/aaaa')
    enterprises_people =      models.ForeignKey(EnterprisesPeople, models.DO_NOTHING, db_column='enterprises_people', blank=True, null=True)
    items_standards =         models.ForeignKey(ItemsStandards, models.DO_NOTHING, db_column='items_standards', blank=True, null=True)
    standards =               models.ForeignKey(Standards, models.DO_NOTHING, db_column='standards', blank=True, null=True)
    group1 =                  models.CharField(max_length=100, blank=True, null=True)
    group2 =                  models.CharField(max_length=100, blank=True, null=True)
    group3 =                  models.CharField(max_length=100, blank=True, null=True)
    group4 =                  models.CharField(max_length=100, blank=True, null=True)
    enterprisepeopleobj =     models.ForeignKey(EnterprisesPeople, models.DO_NOTHING, db_column='enterprisepeopleobj', related_name='todos_enterprisepeopleobj_set', blank=True, null=True)
    todo_template =           models.ForeignKey('TodosTemplate', models.DO_NOTHING, db_column='todo_template', blank=True, null=True)
    assets =                  models.ForeignKey(Assets, models.DO_NOTHING, db_column='assets', blank=True, null=True)
    date_time_open =          models.DateTimeField(blank=True, null=True)
    recurrency_start =        models.DateField(blank=True, null=True)
    recurrency_end =          models.DateField(blank=True, null=True)
    recurrency_every =        models.CharField(max_length=100, blank=True, null=True,choices=RECURRENCY, default=DAY)
    recurrency_periodo =      models.IntegerField(blank=True, null=True)
    recurrency_enable =       models.CharField(max_length=100, blank=True, null=True, choices=YESNO, default=NO)
    recurrency_id_scheduler = models.IntegerField(blank=True, null=True)

    @property
    def expire_month(self):
        if self.expire:
            return self.expire.month
        return None

    @property
    def expire_year(self):
        if self.expire:
            return self.expire.year
        return None

    class Meta:
        managed = False
        db_table = 'todos'

    def __str__(self):
        return self.name

class TypeOfActions(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    export_file = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'type_of_actions'
    def __str__(self):
        return self.name


class TodosTemplate(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type_of_todos = models.ForeignKey('TypeOfTodo', models.DO_NOTHING, db_column='type_of_todos', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'todos_template'
    def __str__(self):
       return self.name


class TypeOfTodo(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_of_todo'
    def __str__(self):
       return self.name

class TOfAEnterprisesItemsStandards(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type_of_actions = models.ForeignKey('TypeOfActions', models.DO_NOTHING, db_column='type_of_actions', blank=True, null=True)
    enterprises_items_standards = models.ForeignKey(EnterprisesStandardsItems, models.DO_NOTHING, db_column='enterprises_items_standards', blank=True, null=True)
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING, db_column='tenant', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_of_a_enterprises_items_standards'
    def __str__(self):
       return self.name