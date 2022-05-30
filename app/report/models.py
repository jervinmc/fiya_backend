from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Report(models.Model):
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    message=models.CharField(_('message'),max_length=255,blank=True,null=True)
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    report_id=models.CharField(_('report_id'),max_length=255,blank=True,null=True)
    is_respo=models.CharField(_('is_respo'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]