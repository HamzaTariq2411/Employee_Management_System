from django.shortcuts import render , HttpResponse
from .models import Employee, Role , Department
from datetime import datetime
from django.db.models import Q
# Create your views here.




def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request,'all_emp.html',context)

def add_emp(request):
    n=''
    if request.method=="POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        picture=request.FILES['pic']
        phone = int(request.POST['phone'])
        salary = int(request.POST['salary'])
        selected_department_id = request.POST['dept']
        selected_department = Department.objects.get(id=selected_department_id)
        selected_role_id= request.POST['role']
        selected_role=Role.objects.get(id=selected_role_id)
        bonus = int(request.POST['bonus'])

        new_emp=Employee(first_name=firstname,last_name=lastname,picture=picture,phone=phone,salary=salary,dept=selected_department,role=selected_role,bonus=bonus,hire_date=datetime.now())

        new_emp.save()
        n="Employee Added Succssfully"
        return render(request,'add_emp.html',{'n':n})
    
    elif request.method=='GET':
         dept = Department.objects.all()
         role = Role.objects.all()
         context={
             'dept':dept,
             'role':role
         }
         return render(request,'add_emp.html',context)
    else:
        return HttpResponse('Employee is not added')

def remove_emp(request, emp_id=0):
    n=''
    if emp_id:
        try:
            emp_to_be_remove = Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            n="Employee removed successfully"
        except:
            return HttpResponse("Please enter valid employee id")
    emps = Employee.objects.all()
    context = {
        'emps':emps,
        'n': n
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=="POST":
        name= request.POST['name']
        dept =request.POST['dept']
        role =request.POST['role']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) |  Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
             emps = emps.filter(role__name=role)

        context={
            'emps' : emps
        }
        return render(request, 'all_emp.html',context)
    elif request.method=="GET":
          return render(request,'filter_emp.html')
    else:
        return HttpResponse("Erorr")
    

def add_dept(request):
    n=''
    if request.method=="POST":
        name = request.POST['name']
        location = request.POST['location']

        new_dept=Department(name=name,location=location)
        new_dept.save()
        n="Department add successfully"
    return render(request,'add_dept.html',{'n':n})


def add_role(request):
    n=''
    if request.method=="POST":
        name = request.POST['name']

        new_role=Role(name=name)
        new_role.save()
        n="Role add successfully"
    return render(request,'add_role.html',{'n':n})

