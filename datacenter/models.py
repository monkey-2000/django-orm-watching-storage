from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def is_visit_long(self, minutes=15):
        """ The function checks the duration of the visit.

        Return True if visit duration more than value of minutes param.

       """
        return self.get_duration() / 60 >= minutes

    def get_duration(self):
        """Count duration of visit and return duration in seconds."""

        entered_at = localtime(value=self.entered_at)

        if self.leaved_at:
            end_time_duration = localtime(value=self.leaved_at)
        else:
            end_time_duration = localtime()

        delta = end_time_duration - entered_at
        seconds = delta.total_seconds()
        return seconds

    def format_duration(self, with_colons=True):
        """Create visit duration record.

        Create visit duration record in text format: "0:00:00" by default and
        "0ч0мин" if with_colons= False

        """

        duration = self.get_duration()
        if with_colons:
            hours = int(duration // 3600)
            duration %= 3600
            min = int(duration // 60)
            duration %= 60
            seconds = int(duration)
            return '{:0=1}:{:0=2}:{:0=2}'.format(hours, min, seconds)
        else:
            hours = int(duration // 3600)
            duration %= 3600
            min = int(duration // 60)
            return '{}ч {}мин'.format(hours, min)
