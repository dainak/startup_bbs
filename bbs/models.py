from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(verbose_name="カテゴリ名", max_length=20)

    def __str__(self):
        return self.name

class Topic(models.Model):
    category = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="コメント", max_length=2000)

    def __str__(self):
        return self.comment

class Reply(models.Model):
    target = models.ForeignKey(Topic, verbose_name="リプライ対象のトピック", on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="コメント", max_length=2000)

    def __str__(self):
        return self.comment