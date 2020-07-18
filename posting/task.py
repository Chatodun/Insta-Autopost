from celery import task
from django.apps import apps
from django.conf import settings
from instabot import Bot


def _model(model_name):
    return apps.get_model('posting', model_name)


@task
def post_created(post_id):
    post = _model('Post').objects.get(pk=post_id)
    bot = Bot()

    bot.login(username=settings.INSTA_USERNAME,
              password=settings.INSTA_PASSWORD)
    path = settings.MEDIA_ROOT + str(post.image)
    return bot.upload_photo(path,
                            caption=post.text)
