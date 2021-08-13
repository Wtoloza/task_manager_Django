from django.db import models

# Create your models here.

class Project(models.Model):
    id_project = models.SmallIntegerField(primary_key=True)
    name_project = models.CharField(max_length=50)

    def __str__(self):
        return self.name_project

class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    project_task = models.ForeignKey(Project, null=False, blank=False, on_delete=models.CASCADE)
    title_task = models.CharField(max_length=50)
    description_task = models.CharField(max_length=200)
    imporant_task_choice = [
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'Urgent')
    ]
    imporant_task = models.CharField(max_length=1, choices=imporant_task_choice, default='0')
    status_task = models.BooleanField(default=False)

    def __str__(self):
        task = '{0} / {1} >> {2}'
        if self.status_task:
            status = 'Terminada'
        else:
            status = 'Pendiente'
        return task.format(self.title_task, self.project_task, status)

