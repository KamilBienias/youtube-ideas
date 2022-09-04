from django.db import models

IDEA_STATUS = (
    ('pending', 'Waiting for review'),
    ('accepted', 'Accepted'),
    ('done', 'Done'),
    ('rejected', 'Rejected')
)


class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # youtube_url może być pusty
    youtube_url = models.URLField(null=True, blank=True)
    status = models.CharField(choices=IDEA_STATUS, max_length=30, default='pending')

    # po to żeby nie wyświetlało np Idea object (1)
    # Ta metoda wywołana gdy ktoś z obiektu próbuje zrobić string
    def __str__(self):
        return self.title


class Vote(models.Model):
    # klucz obcy to Idea. W momencie jak ktoś usuwa pomysł to głosy też się usuwają (CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    # reason to dlaczego głosuję na ten pomysł
    reason = models.TextField()

    def __str__(self):
        return f'ID {self.id}'
