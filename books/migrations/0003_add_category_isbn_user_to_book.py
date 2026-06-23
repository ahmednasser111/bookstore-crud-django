from django.conf import settings
from django.db import migrations, models
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_author_remove_book_price_book_desc_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # 1. Create Category
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    max_length=100,
                    validators=[django.core.validators.MinLengthValidator(2)],
                )),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),

        # 2. Narrow title to max 50 chars
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(
                max_length=50,
                validators=[django.core.validators.MinLengthValidator(10)],
            ),
        ),

        # 3. Add user FK with one-off default=1 (first superuser)
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='books',
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),

        # 4. Add M2M categories
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='books', to='books.category'),
        ),

        # 5. Create ISBN with OneToOne to Book
        migrations.CreateModel(
            name='ISBN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_title', models.CharField(blank=True, max_length=200)),
                ('book_title', models.CharField(max_length=50)),
                ('isbn_number', models.CharField(blank=True, max_length=13, unique=True)),
                ('book', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='isbn',
                    to='books.book',
                )),
            ],
            options={
                'verbose_name': 'ISBN',
                'verbose_name_plural': 'ISBNs',
            },
        ),
    ]
