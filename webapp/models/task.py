from django.db import models



class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Description', max_length=500)
    status = models.ForeignKey(to='webapp.Status', related_name='task', on_delete=models.RESTRICT, verbose_name='Status')
    type = models.ManyToManyField(to='webapp.Type', related_name='task', verbose_name='Type' )
    created_at = models.CharField(max_length= 200, verbose_name='Created at')
    ended_at = models.CharField(max_length=200, verbose_name='Ended at')
    project = models.ForeignKey(to='webapp.Project', related_name='task', on_delete=models.RESTRICT, verbose_name='Project')
    def __str__(self) -> str:
        return self.title