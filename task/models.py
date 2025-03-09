from django.db import models


class ProjectTask(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        DONE = 'DONE', 'Done'

    date = models.DateField()
    project = models.CharField(max_length=200)
    project_code = models.CharField(max_length=50)
    activity = models.TextField()
    estimated_hours = models.IntegerField(
        help_text="Number of hours allocated for this task"
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.IN_PROGRESS
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', 'project']
        verbose_name = 'Project Task'
        verbose_name_plural = 'Project Tasks'

    def __str__(self):
        return f"{self.project_code} - {self.activity[:50]}"