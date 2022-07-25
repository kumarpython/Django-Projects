from django.contrib import admin, messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import model_ngettext
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerCreationForm, CustomerChangeForm
from .models import Customer, CustomerAddress
from .conf import settings


class CustomerAdmin(UserAdmin) :
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    model = Customer
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = ((None, {'fields' : ('email', 'password')}),
                 ('Permissions', {'fields' : ('is_staff', 'is_active')}),)
    add_fieldsets = ((None, {'classes' : ('wide',),
                             'fields' : ('email', 'password1', 'password2', 'is_staff', 'is_active')}),)
    search_fields = ('email',)
    ordering = ('email',)
    actions = ('activate_users', 'send_activation_email',)

    def activate_users(self, request, queryset) :
        """
        Activates the selected users, if they are not already
        activated.
        """
        n = 0
        for user in queryset :
            if not user.is_active :
                user.activate()
                n += 1
        self.message_user(request,_('Successfully activated %(count)d %(items)s.') %{'count' : n, 'items' : model_ngettext(self.opts, n)}, messages.SUCCESS)
    activate_users.short_description = _('Activate selected %(verbose_name_plural)s')

    def send_activation_email(self, request, queryset) :
        """
        Send activation emails for the selected users, if they are not already
        activated.
        """
        n = 0
        for user in queryset :
            if not user.is_active and settings.USERS_VERIFY_EMAIL :
                self.send_activation_email(user=user, request=request)
                n += 1

        self.message_user(
            request, _('Activation emails sent to %(count)d %(items)s.') %
                     {'count' : n, 'items' : model_ngettext(self.opts, n)}, messages.SUCCESS)

    send_activation_email.short_description = \
        _('Send activation emails to selected %(verbose_name_plural)s')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerAddress)
