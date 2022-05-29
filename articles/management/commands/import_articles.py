import json

from django.core.management.base import BaseCommand
from articles.models import Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('articles.json', 'r', encoding='utf-8') as file:
            articles = json.load(file)

        for article in articles:
            Article.objects.get_or_create(
                id= article['pk'],
                title= article['fields']['title'],
                text= article['fields']['text'],
                published_at= article['fields']['published_at'],
                image= article['fields']['image']
            )
