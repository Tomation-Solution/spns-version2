from django.db import models

# Create your models here.

class ServiceModel(models.Model):
    title = models.CharField(max_length=300)
    main_content = models.TextField()
    intro_content=models.TextField(max_length=300)
    icon_class = models.CharField(max_length=200,default="..")


    def __str__(self):return f'{self.title}'


class PeopleDataForPdf(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    location = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    jobTitle = models.CharField(max_length=300)
    message = models.TextField()
    phone_number = models.CharField(max_length=100,default="")
    # location = models.CharField(max_length=600,default="")
    

    def __str__(self):return f'{self.name}'



class ResearchInsightInfo(models.Model):
    cover_image = models.ImageField(upload_to='spns_cover_image/')
    heading= models.CharField(max_length=350)
    intro_content = models.TextField(default='..')
    pdf_file = models.FileField(upload_to='researcch_and_insight',blank=True)

    def __str__(self):return f'{self.heading}'


class researchinsight_ParaGraph(models.Model):
    researchinsightinfo = models.ForeignKey(ResearchInsightInfo,on_delete=models.CASCADE)
    paragraph = models.TextField()

    # defs



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message_type = models.CharField(max_length=50)
    message = models.TextField()
    phone = models.CharField(max_length=100,default="")

    def __str__(self):
        return f'{self.name} sent a message'