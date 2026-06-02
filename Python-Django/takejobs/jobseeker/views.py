from django.shortcuts import render
from django.http import HttpResponse
from jobseeker.models import user,jobseeker
# Create your views here.
def login(request):
    return render(request,'jobseeker/login.html')

def register(request):
#     if request.POST:
#         #ye python ka veriable hai 
#         role=request.POST["role"]
#                                 # yehtml ka variable hai
#         # print("-------------->",role) #check kane ke liye
#         if role=="jobseeker":
#             f_name=request.POST['f_name']
#             l_name=request.POST['l_name']
#             Email=request.POST['Email']
#             number=request.POST['number']
#             skills=request.POST['skills']
#             password=request.POST['password']
#             con_pass=request.POST['con_pass']
#             if 'Terms' in request.POST:
#                 uid=user.objects.create(
#                     email=email,
#                     password=password,
#                     role=role
#                 )
#                 jid=jobseeker.objects.create(
#                     user_fk=uid,
#                     f_name=fis_name,
#                     l_name=las_name,
#                     number=number,
#                     skills=skills
#                 )
#             return render(request,'jobseeker/login.html')
    # else:
    return render(request,'jobseeker/registeration.html')