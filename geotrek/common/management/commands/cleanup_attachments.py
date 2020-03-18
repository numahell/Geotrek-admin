from pathlib import Path

from django.core.management.base import BaseCommand
from django.conf import settings

from geotrek.common.models import Attachment
from easy_thumbnails.models import Thumbnail


class Command(BaseCommand):
    help = "Remove files for deleted attachments"

    def handle(self, *args, **options):
        paperclip_dir = Path(settings.MEDIA_ROOT) / 'paperclip'
        attachments = set(Attachment.objects.values_list('attachment_file', flat=True))
        thumbnails = set(Thumbnail.objects.values_list('name', flat=True))
        if options['verbosity'] >= 1:
            self.stdout.write(u"Attachments: {} / Thumbnails: {}".format(len(attachments), len(thumbnails)))
        total = 0
        deleted = 0
        for path in paperclip_dir.glob('**/*'):
            if not path.is_file():
                continue
            total += 1
            relative = str(path.relative_to(settings.MEDIA_ROOT)).decode('utf8')
            if relative in attachments or relative in thumbnails:
                if options['verbosity'] >= 2:
                    self.stdout.write(u"Keep {}".format(relative))
                continue
            deleted += 1
            path.unlink()
            if options['verbosity'] >= 1:
                self.stdout.write(self.style.NOTICE(u"Delete {}".format(relative)))
        if options['verbosity'] >= 1:
            self.stdout.write(self.style.SUCCESS(u"Files: {} / Deleted: {}".format(total, deleted)))
