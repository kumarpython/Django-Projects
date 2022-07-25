from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from .conf import settings


class Customer(AbstractBaseUser,PermissionsMixin):
    """
        Abstract User with the same behaviour as Django's default User.
        Customer does not have username field. Uses email as the
        USERNAME_FIELD for authentication.
        Use this if you need to extend EmailUser.
        Inherits from both the AbstractBaseUser and PermissionMixin.
        The following attributes are inherited from the superclasses:
            * password
            * last_login
            * is_superuser
        """

    USERS_AUTO_ACTIVATE = not settings.USERS_VERIFY_EMAIL

    username = None
    email = models.EmailField(_("email address"), max_length=255, unique=True, db_index=True)
    email_verified=models.BooleanField(default=False)
    is_staff = models.BooleanField(_("staff status"),default=False)
    is_active = models.BooleanField(_("active"),default=USERS_AUTO_ACTIVATE)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    fname=models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    pic=models.ImageField(default='', upload_to='customer_profile_pics')
    mobile= models.IntegerField()
    mobile_verified=models.BooleanField(default=False,null=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self) :
        return self.fname

    @property
    def verify_email(self):
        pass

    @property
    def verify_mobile(self) :
        pass


class CustomerAddress(models.Model):
    user=models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    nickname=models.CharField(max_length=50)
    address= models.TextField(max_length=200)
    city= models.CharField(max_length=50)
    zipcode=models.IntegerField()
    contact=models.IntegerField()
