from django.db import migrations, models
import django.db.models.deletion


def move_product_categories(apps, schema_editor):
    Product = apps.get_model("shop", "Product")
    Category = apps.get_model("shop", "Category")
    SubCategory = apps.get_model("shop", "SubCategory")

    first_category = Category.objects.first()

    # Give each product the category that came from its old sub category.
    for product in Product.objects.all():
        if product.sub_category.category:
            product.category = product.sub_category.category
        else:
            product.category = first_category
        product.save()

    sub_categories = {}

    # Keep one sub category with each name, for example only one Spinning.
    for sub_category in SubCategory.objects.all().order_by("id"):
        if sub_category.name in sub_categories:
            first_sub_category = sub_categories[sub_category.name]
            Product.objects.filter(sub_category=sub_category).update(sub_category=first_sub_category)
            sub_category.delete()
        else:
            sub_categories[sub_category.name] = sub_category


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.category",
            ),
        ),
        migrations.RunPython(move_product_categories, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="subcategory",
            name="category",
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.category",
            ),
        ),
    ]
