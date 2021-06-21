from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect , HttpResponse
from PhoenixApp.models import ArtCraft, Review,Contact,PreviousEvent,UpComingEvent,Result, Blog, Gallery, quizomania
# from PhoenixApp.models import Review,Contact,PreviousEvent,UpComingEvent,Result, Blog, Member, Gallery, ArtCraft
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    context = {"home_page": "active"}
    return render(request,'home.html', context)

def clubs(request):
    context = {"clubs_page": "active"}
    return render(request,'club.html', context)

def events(request):
    prevevents = PreviousEvent.objects.all()
    upevn= UpComingEvent.objects.all()
    context = {
        "events_page": "active",
        'product': prevevents,
        'upcomingevents': upevn,
        }
    return render(request,'events.html', context)

def result(request, slug):
    results= Result.objects.filter(slug=slug)
    return render(request, 'result.html', {"results" : results})

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs_page": "active",
        "blog":blogs,
    }
    return render(request,'blogs.html', context)
def blog(request, myid):
    blog= Blog.objects.filter(id=myid)
    contents = Blog.objects.all()
    return render(request,"blog.html",{'blog':blog, "contents": contents})

def gallery(request):
    gallery = Gallery.objects.all()
    context = {"gallery_page": "active", "contents": gallery}
    return render(request,"gallery.html", context)

def webteam(request):
    context = {"webteam_page": "active"}
    return render(request,'webteam.html', context)

def contact(request):
    context = {"contact_page": "active"}
    if request.method=='POST':
        name=request.POST.get('name')
        year=request.POST.get('year')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        subject= name + ' of ' + year+ ' wants to know about '+ desc + '\n \n His/Her Email ID is ' + email +'.'
        contact = Contact(name=name,year=year,email=email,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your Contact Request has been Submitted. We'll Contact you soon.")
        send_mail('Contact Request',subject,settings.EMAIL_HOST_USER,['info@phoenixnsec.in'])
    return render(request,'contact.html', context)

def avenir(request):
    context = {"events_page": "active"}
    return render(request,'avenir.html', context)

def brainstormer(request):
    context = {"events_page": "active"}
    return render(request,'brainstormer.html', context)

def aavahan(request):
    context = {"events_page": "active"}
    return render(request,'aavahan.html', context)

def cybernix(request):
    context = {"clubs_page": "active"}
    return render(request,'cybernix.html', context)

def eloquense(request):
    context = {"clubs_page": "active"}
    return render(request,'eloquense.html', context)

def robonix(request):
    context = {"clubs_page": "active"}
    return render(request,'robonix.html', context)

def lensified(request):
    context = {"clubs_page": "active"}
    return render(request,'lensified.html', context)

def nirmaan(request):
    context = {"clubs_page": "active"}
    return render(request,'nirmaan.html', context)

def review(request):
    if request.method=='POST':
        review=request.POST.get('review')
        subject= 'We got the following review about Phoenix : \n'+ review
        review = Review(review=review, date=datetime.today())
        review.save()
        messages.success(request, "Your Review has been submitted, We'll soon start work on your review")
        send_mail('Review form',subject,settings.EMAIL_HOST_USER,['core@phoenixnsec.in'])
    return redirect('/home')

# def membership(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         contact=request.POST.get('contact')
#         session=request.POST.get('session')
#         department=request.POST.get('department')
#         subject= name + ' of ' + department+ ' department of ' + session+ ', wants to be a member of Phoenix. '+ '\n \n His/Her Contact Number is '+ contact +' and  Email ID is ' + email +'.'
#         subject1= 'Hey ' +name + ', \n Thank you for becoming Permanent Member of Phoenix - The Offical Tech Club of NSEC.'
#         member = Member(name=name,session=session,email=email,department=department, contact=contact, date=datetime.today())
#         member.save()
#         messages.success(request, "Your One-time Membership Request has been Submitted. We'll Contact you soon.")
#         send_mail('Membership Request',subject,settings.EMAIL_HOST_USER,['info@phoenixnsec.in'])
#         send_mail('Membership | PHOENIX',subject1,settings.EMAIL_HOST_USER,[email])
#     return render(request,'membership.html')


# def Creativarty(request):
#     return render(request,'artcraft.html')

def Quizomania(request):
    return render(request,'quizomania.html')

# def Confirmation(request):
#     if request.method=='POST' and request.FILES['image']:
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         contact=request.POST.get('contact')
#         college=request.POST.get('college')
#         department=request.POST.get('department')
#         year=request.POST.get('year')
#         image=request.FILES['image']
#         subject= name + ' of ' + department+ ' department, ' + year + ' year of ' + college+ ', Participated in Creativarty. '+ '\n \n His/Her Contact Number is '+ contact +' and  Email ID is ' + email +'.'
#         subject1= 'Hey ' +name + ', \n Thank you for Participating in Creativarty. \n\nBe alert for Results on 2nd June 2021.\n\n\n Thanking you \n Phoenix\n The Official Tech Club of NSEC\n Kolkata, West Bengal\ne-mail: info@phoenixnsec.in\nWebsite: www.phoenixnsec.in'
#         artcraft = ArtCraft(name=name,college=college,email=email,department=department, year=year, contact=contact,image=image , date=datetime.today())
#         artcraft.save()
#         messages.success(request, "Your Form Has Been Submitted. Be alert for Results on 2nd June 2021.")
#         send_mail('Creativarty Participation',subject,settings.EMAIL_HOST_USER,['info@phoenixnsec.in'])
#         send_mail('Creativarty | PHOENIX',subject1,settings.EMAIL_HOST_USER,[email])
#     return redirect('/home')
def confirmation(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        department=request.POST.get('department')
        subject= name + ' of ' + department+ ' department, of 1st Year has been Participated in Quizomania. '+ '\n \n His/Her Contact Number is '+ contact +' and  Email ID is ' + email +'.'
        subject1= "Hey " + name + ", \n Thank you for Participating in Quizomania. \n\nBe Ready for Quiz on 20th June 2021 (Sunday) at 4 PM. Don't miss this amazing Opportunity.\nAll the Best!!!\n\n\n Thanking you \n\n Phoenix\n The Official Tech Club of NSEC\n Kolkata, West Bengal\ne-mail: info@phoenixnsec.in\nWebsite: www.phoenixnsec.in"

        abc = quizomania(name = name, email=email, contact=contact, department=department, date=datetime.today())
        abcd = quizomania.objects.all()
        for i in abcd:
            if abc.email== i.email:
                messages.warning(request, "Your Form Has Been Already Submitted.")
                return redirect('/events/Quizomania')
        else:
            abc.save()
        messages.success(request, "Your Form Has Been Submitted. Be Ready for Quiz on 20th June 2021 (Sunday) at 4 PM. Don't miss this amazing Opportunity.")
        send_mail('Quizomania Participation',subject,settings.EMAIL_HOST_USER,['info@phoenixnsec.in'])
        send_mail('Quizomania | PHOENIX',subject1,settings.EMAIL_HOST_USER,[email])
    return render(request,'confirmation.html')

