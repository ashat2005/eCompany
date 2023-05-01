from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название продукта"
    )
    description = models.CharField(
        max_length=300,
        verbose_name= "Описание продукта"
    )
    product_image = models.ImageField(
        upload_to= 'product_images/',
        verbose_name="Фотография продукта"
    )
    price = models.PositiveBigIntegerField(
        verbose_name="Цена"
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"