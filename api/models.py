from django.db import models




class Sohalar(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Sohalar"

# Create your models here.
class TestModel(models.Model):
    asnwers = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
        ('d', 'd')
    )
    test_name = models.CharField(max_length=140)
    test = models.CharField(max_length=100)
    a = models.CharField(max_length=50, null=True, blank=True)
    b = models.CharField(max_length=50, null=True, blank=True)
    c = models.CharField(max_length=50, null=True, blank=True)
    d = models.CharField(max_length=50, null=True, blank=True)

    soha = models.ForeignKey(Sohalar, on_delete=models.CASCADE, null=True, blank=True)
    correct_answer = models.CharField(max_length=15, choices=asnwers)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.test_name



    class Meta:
        ordering = ('-created_at', )
        verbose_name_plural = 'Testlar'

