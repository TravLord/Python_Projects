from django.db import models

# creating model for database field structure


class DjangoClasses(models.Model):
    Title = models.CharField(max_length=100,default="", null=False)
    CourseNumber = models.IntegerField(default="", blank=True, null=False)
    InstructorName = models.CharField(max_length=70, default="", blank=True, null=False)
    Duration = models.FloatField(max_length=70, default="", blank=True, null=False)

    objects = models.Manager()
    # this adds the Title of the course as the Field title on the admin webpage
    def __str__(self):
        return self.Title
