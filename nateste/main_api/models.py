from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_cooker = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # TODO add avatar
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Order(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=2000)
    deadline = models.IntegerField()  # TODO change to Datafield
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    weight = models.FloatField()
    price = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='customer_order')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                               related_name='worker_order')

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=2000)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='customer_review')
    worker = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='worker_review')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.title



#TODO make order , find order {query string},

#graphql

