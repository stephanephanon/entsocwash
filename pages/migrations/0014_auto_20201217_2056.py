# Generated by Django 3.0.8 on 2020-12-17 20:56

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('pages', '0013_auto_20201217_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='location',
            field=models.CharField(default='', help_text='Enter the location of the meeting', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('subtitle', wagtail.core.blocks.CharBlock(classname='full title', help_text='Enter a subtitle for the page')), ('section', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='Enter a heading for a section of text on the page')), ('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateTimeField(help_text='Enter the date and time of the meeting'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='image',
            field=models.ImageField(blank=True, help_text='Optional; select an image to go with this meeting', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='title',
            field=models.CharField(default='', help_text='Add a title for this specific meeting', max_length=100),
        ),
        migrations.DeleteModel(
            name='EventPage',
        ),
    ]
