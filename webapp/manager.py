from django.db.models import Manager

from webapp.querysets import CustomBaseQuerySet


class TaskManager(Manager):

    def get_or_none(self, pk=None):
        try:
            return self.get_queryset().get(pk=pk)
        except self.model.DoesNotExist:
            return None


    def all(self):
        return self.get_queryset().all()
    def get_queryset(self):
        return CustomBaseQuerySet(self.model, using=self._db)