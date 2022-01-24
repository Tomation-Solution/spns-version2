from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages




def indexPage(request):
    services = models.ServiceModel.objects.all()
    return render(request,'home-agency.html',
    {
        "all_service":services,
        "5_service":services[0:5],
        "all_researchInfor3":models.ResearchInsightInfo.objects.all()[0:3],
        "all_researchInfor":models.ResearchInsightInfo.objects.all()

    }
    )




def about(request):
    return render(request,'about.html',{
       "all_service" :models.ServiceModel.objects.all(),

 
        "all_researchInfor3":models.ResearchInsightInfo.objects.all()[0:3],
        "all_researchInfor":models.ResearchInsightInfo.objects.all()

    })



def team(request):
    return render(request,"our-team.html",
    {
       "all_service" :models.ServiceModel.objects.all(),
          "all_researchInfor3":models.ResearchInsightInfo.objects.all()[0:3],
        "all_researchInfor":models.ResearchInsightInfo.objects.all()

    })


def insightList(request):
    return render(request,'insight-list.html',
    {
       "all_service" :models.ServiceModel.objects.all(),
        "all_researchInfor":models.ResearchInsightInfo.objects.all(),

    })


def insightDetail(request,pk=None):


    reseacrhInsight = models.ResearchInsightInfo.objects.get(id=pk)
    name = ''
    email = ''
    Location = ''
    company = ''
    jobTitle = ''
    message = ''
    phoneNumber=''

    if request.method == 'POST':


        try:
            # data = dict(request.POST)  
            # print(data)  
            name = request.POST['name']
            email = request.POST['email']
            Location = request.POST['Location']
            company = request.POST['company']
            jobTitle = request.POST['job-title']
            phoneNumber=request.POST['phone-number']
            message= request.POST['message'] if request.POST['message'] else ""
            # print(name,email,message)
            data = models.PeopleDataForPdf.objects.create(
                name=name,email=email,
                location=Location,
                company=company,jobTitle=jobTitle,message=message,
                phone_number=phoneNumber,
                # location=location
            )
            data.save()
            messages.success(request, 'Thank you!!!..')
            # application/pdf

        # with open(reseacrhInsight.pdf_file.url) as fh:

            response = HttpResponse(reseacrhInsight.pdf_file.url,content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{reseacrhInsight.heading}.csv"'
            return response

        except:
            messages.error(request, 'Please Provide required fields.')
            return HttpResponse("Some Error Occurred")
    return render(request,'insightDetail.html',{
                'object':reseacrhInsight,
        "object_para":models.ResearchInsightInfo.objects.get(id=pk).researchinsight_paragraph_set.all(),
       "all_service" :models.ServiceModel.objects.all(),

   "all_researchInfor3":models.ResearchInsightInfo.objects.all()[0:3],
        "all_researchInfor":models.ResearchInsightInfo.objects.all()

    })

def solutionDetail(request,pk=None):
    return render(request,'solutionDetail.html',
    {
       "all_service" :models.ServiceModel.objects.all(),
       "object":models.ServiceModel.objects.get(id=pk),
          "all_researchInfor3":models.ResearchInsightInfo.objects.all()[0:3],
        "all_researchInfor":models.ResearchInsightInfo.objects.all()

    })

def solutionList(request):
    return render(request,'solutionList.html',
    {
       "all_service" :models.ServiceModel.objects.all(),
          "all_researchInfor3":models.ResearchInsightInfo.objects.all()[0:3],
        "all_researchInfor":models.ResearchInsightInfo.objects.all()


    })


def contact(request,pk=None):

    name = ''
    email = ''
    message = ''
    messageType = ''
    phone =''
    location=''

    if request.method == 'POST':

        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        messageType = request.POST['messageType']  
       
        location       = request.POST['location'] 
        phone =request.POST['phone']         
 
        # print(
        #     name,"name\n",
        #     email,"email\n",
        #     message,"message\n",
        # )
        contact= models.Contact.objects.create(
        name=name,email=email,message=message,message_type=messageType,phone=phone,
        location=location
        )

        contact.save()
        messages.success(request, 'Thank you for reach out.. our team will get back to you')





    return render(request,'contact.html',
    {
       "all_service" :models.ServiceModel.objects.all(),
          "all_researchInfor3":models.ResearchInsightInfo.objects.all()[0:3],
        "all_researchInfor":models.ResearchInsightInfo.objects.all()

    })

