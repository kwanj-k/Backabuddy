""" Common fields """

from django.db import models


class CustomManager(models.Manager):
    """
    Custom manager so as not to return deleted objects
    """

    def get_queryset(self):
        return super(CustomManager, self).get_queryset().filter(deleted=False)


class AbstractBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted = models.BooleanField(
        default=False,
        help_text="This is to make sure deletes are not actual deletes")
    # everything will be used to query deleted objects e.g Model.everything.all()
    everything = models.Manager()
    objects = CustomManager()
    
    def delete(self, *args, **kwargs):
        """Override delete"""
        self.deleted = True
        self.save()

    
    class Meta:
        abstract = True
        ordering = ('-created_at', '-updated_at')
        app_label = 'apiv1'