from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
User = get_user_model()


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug':obj.slug})


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name="Имя категории")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract = True
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name="Описание товара", null = True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.title

class LatestProductsManager:

    @staticmethod
    def get_products_for_modules(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model_in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products

class LatestProducts:
    objects = LatestProductsManager


class CartProduct(models.Model):


    user = models.ForeignKey("Customer", verbose_name="Покупатель", on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", verbose_name="Корзина", on_delete=models.CASCADE, related_name='related_cart')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Общая Цена")

    def __str_(self):
        return "Продукт: {}(Для корзины)".format(self.product.title)


class Cart(models.Model):

    owner = models.ForeignKey("customer",verbose_name="Владелец", on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Общая Цена")

    def __str__(self):
        return str(self.id)

class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)

class ShoesProduct(Product):
    size = models.CharField(max_length=255, verbose_name="Размер кроссовок")
    brand_name = models.CharField(max_length=255, verbose_name="Брендовое имя кроссовок")
    sex = models.CharField(max_length=255, verbose_name="Пол")
    season = models.CharField(max_length=255, verbose_name="Кроссовок для Сезона")

    def __str__(self):
        return"{} : {}".format(self.category.name, self.title)
    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class TShirtsProduct(Product):
    size = models.CharField(max_length=255, verbose_name="Размер Футболок")
    brand_name = models.CharField(max_length=255, verbose_name="Брендовое имя Футболок")
    sex = models.CharField(max_length=255, verbose_name="Пол")
    season = models.CharField(max_length=255, verbose_name="Футболки для Сезона")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class HoodieProduct(Product):
    size = models.CharField(max_length=255, verbose_name="Размер Худи")
    brand_name = models.CharField(max_length=255, verbose_name="Брендовое имя Худи")
    sex = models.CharField(max_length=255, verbose_name="Пол")
    season = models.CharField(max_length=255, verbose_name="Худи для Сезона")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')