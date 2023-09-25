# Generated by Django 4.0.6 on 2023-09-15 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.AlterModelOptions(
            name='accountitem',
            options={'verbose_name': 'Ingreso - Egreso', 'verbose_name_plural': 'Ingresos - Egresos'},
        ),
        migrations.AlterField(
            model_name='account',
            name='expense',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Egreso Total'),
        ),
        migrations.AlterField(
            model_name='account',
            name='income',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Ingreso Total'),
        ),
        migrations.AlterField(
            model_name='account',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Caja Total'),
        ),
        migrations.AlterField(
            model_name='account',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Ultima actualización'),
        ),
        migrations.AlterField(
            model_name='accountitem',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Monto'),
        ),
        migrations.AlterField(
            model_name='accountitem',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Ultima actualización'),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('comments', models.ManyToManyField(related_name='video_comments', to='accounts.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('comments', models.ManyToManyField(related_name='image_comments', to='accounts.comment')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('score', models.PositiveIntegerField(default=0)),
                ('comments', models.ManyToManyField(related_name='blog_comments', to='accounts.comment')),
            ],
        ),
    ]
