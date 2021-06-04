from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
        
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

class table(models.Model):
    def __str__(self):
        return self.user_name
    user_name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200,default=0)
    phn=models.CharField(max_length=200,default=0)

class farmer(models.Model):
    def __str__(self):
        return self.user_name
    user_name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200,default=0)
    phn=models.CharField(max_length=200,default=0)



#after creating a table register it in admin.py 
class seller(models.Model):
    def __str__(self):
        return self.user_name
    user_name=models.CharField(max_length=200)
    crop_name=models.CharField(max_length=200)
    price_per_kg=models.IntegerField(default=0)
    max_kg=models.IntegerField(default=0)
    photo=models.ImageField(upload_to='images/',default=0)
    #https://blearningclub.com/django-tutorial/how-to-upload-image-in-django-by-user/
    # see the above link for uploading
    

#now neec to add buyyer class

class verif(models.Model):
    def __str__(self):
        return self.user_name
    user_name=models.CharField(max_length=200)
    user_id=models.CharField(max_length=200)
    
class corporate(models.Model):
    def __str__(self):
        return self.company
    good_name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    priceperkg=models.CharField(max_length=200)
    email=models.CharField(max_length=200,default=0)
    photo=models.ImageField(upload_to='images/',default=0)

class cart(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    seller_name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)

class feedback(models.Model):
    def __str__(self):
        return self.crop_name
    crop_name=models.CharField(max_length=200)
    rate=models.IntegerField(default=0)
