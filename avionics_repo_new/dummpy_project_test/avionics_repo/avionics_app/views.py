from django.shortcuts import render,redirect
from django.http import HttpResponse
from subprocess import run
import sys
import os
# from .models import process_file_repo
from .functions.functions import handle_uploaded_file,convert_to_24_h,clear_old_files


#####################
# Create your views here.
def index(request):
    return render(request, 'index.html')


def new_process(request):

    projects=''
    context = {"projects":  projects}
    return render(request, 'index.html', context)


def process_execution(request):
    context = {"process_execution": "active"}
    return render(request, 'process-execution.html')


def project_management(request):
    context = {"project_management": "active"}
    return render(request, 'project-management.html')


def update_task(request):
    return render(request, 'update-task.html')


def role_management(request):
    context = {"role_management": "active"}
    return render(request, 'role-management.html')


def user_management(request):
    context = {"user_management": "active"}
    return render(request, 'user-management.html')


def job_dashboard(request):
    context = {"job_dashboard": "active"}
    return render(request, 'job-dashboard.html')


def template_details(request):
    context = {"template_details": "active"}
    return render(request, 'template-details.html')


def template_configuration(request):
    context = {"template_configuration": "active"}
    return render(request, 'template-configuration.html')


def notification_config(request):
    context = {"notification_config": "active"}
    return render(request, 'notification-config.html')


def base(request):
    context = {}
    return render(request, 'base.html')



def login(request):
    context = {}
    return render(request, 'login.html')


def schedule_project(request,pk):


    project_file_li=[]
    pk=''
    context={'process':project_file_li,'pk':pk}
    return render(request,'schedule_project.html',context)


def delete_process(request,pk):

    process=''
    return render(request,'delete_page.html',{'obj':process})


# def update_task(request,pk):
#
#     process=''
#     context={'obj': process}
#     return render(request,'update_task.html',context)

