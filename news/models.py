from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True) #blank=True - обозначает поле необязательное к заполнению
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True - обозначает, что дата и время будут создаваться автоматически и при редактировании не изменяться (не обновляться)
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True при редактировании (обновлении) новости будет указано время ее редактирования
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/') # сохранение по дате при загрузке %Y/%m/%d/
    is_puplished = models.BooleanField(default=True)  # default=True - новость по умолчанию публикуется

    def __str__(self):
        return self.title
