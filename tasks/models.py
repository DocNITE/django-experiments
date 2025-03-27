from django.db import models

# Not many, right?
class Task(models.Model):
    text = models.CharField(max_length=200, verbose_name='Содержание')
    done = models.BooleanField(default=False, verbose_name='Готовность')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Задания'
        verbose_name = 'Задание'
        ordering = ['-created']