from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    class Status(models.IntegerChoices):
        DOWN = 0, '下架'  # 值只能從選項中選出
        UP = 1, '上架'  # 預設是上架狀態

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    status = models.SmallIntegerField(
        choices=Status.choices,
        default=Status.UP,
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.PROTECT,
        related_name='products',
    )
    tags = models.ManyToManyField(
        to=Tag,
        related_name='products',
    )

    def __str__(self) -> str:
        return self.name
