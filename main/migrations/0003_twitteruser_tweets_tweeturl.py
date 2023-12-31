# Generated by Django 4.2.2 on 2023-06-17 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_tweets_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='twitterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitterUser', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Nuetral', 'Nuetral'), ('Offensive Language', 'Offensive Language'), ('Hateful Message', 'Hateful Message')], default='Not yet analysed', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='tweets',
            name='tweetURL',
            field=models.CharField(default='twitter.com/placeholder', max_length=255),
            preserve_default=False,
        ),
    ]
