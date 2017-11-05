from django.db import models
from django.db.models import signals
from django.dispatch import receiver


# Create your models here.

class InsydoGuide(models.Model):
    EAT = 'ET'
    DRINK = 'DR'
    PARTY = 'PT'
    ADVENTURE = 'AD'
    EXPLORE = 'EX'
    WORKOUT = 'WK'
    LOOK_GOOD = 'LG'
    KIDS = 'KD'
    WATCH = 'WT'
    TRAVEL = 'TR'
    NEWS = 'NW'

    INSYDO_CATEGORY_CHOICES = (
        (EAT, 'Eat'),
        (DRINK, 'Drink'),
        (PARTY, 'Party'),
        (ADVENTURE, 'Adventure'),
        (EXPLORE, 'Explore'),
        (WORKOUT, 'Work Out'),
        (LOOK_GOOD, 'Look Good'),
        (KIDS, 'Kids'),
        (WATCH, 'Watch'),
        (TRAVEL, 'Travel'),
        (NEWS, 'News'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=2,
                                choices=INSYDO_CATEGORY_CHOICES,
                                default=EAT)
    published_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


@receiver(signals.pre_init, sender=InsydoGuide)
def initialize_guide(sender, **kwargs):
    print("Guide initialized", kwargs)
