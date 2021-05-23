from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import CharField, DecimalField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menu'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'

class Product(models.Model):
    # Category가 삭제되면 같이 Delete?? 기존 Category는 삭제되지만 현재의 물품은 그냥 Category변경이라면?
    # 일단 CASCADE 미적용
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()

    # 상품을 날린다고 영양정보가 날라가면 안되니 CASCADE미적용
    # 다른 상품에서 해당 영양정보를 사용가능할것 같기는 하나, 영양정보가 완전 동일한 상품이 있을지는 미지수...
    # 아무튼 일단 미적용
    nutrition = models.ForeignKey(Nutrition, on_delete=models.DO_NOTHING)

    # Many to Many 설정
    allegry = models.ManyToManyField(Allergy, through='Product_Allergy')

    class Meta:
        db_table = 'products'

class Product_Allergy(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=CASCADE)

    class Meta:
        db_table = 'products_allergy'

class Image(models.Model):
    image_url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'