from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=200)
    duration = models.TimeField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # sort_order = models.IntegerField(default=0)

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
