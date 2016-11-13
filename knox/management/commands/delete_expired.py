from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from knox.models import AuthToken

class Command(BaseCommand):
  help = 'Delete expired knox tokens'


  def handle(self, *args, **options):
    self.stdout.write(self.style.SUCCESS('Total: %d tokens' % (AuthToken.objects.count())))

    delete_count = 0
    for auth_token in AuthToken.objects.all():
      if auth_token.expires is not None:
        if auth_token.expires < timezone.now():
          delete_count += 1
          auth_token.delete()

    self.stdout.write(self.style.SUCCESS('Deleted: %d tokens' % (delete_count)))
