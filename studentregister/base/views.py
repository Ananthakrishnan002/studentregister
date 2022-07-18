from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

# Create your views here.



def listStudent(request):
    if 'q' in request.GET:
        q = request.GET['q']
        students = Student.objects.filter(name__icontains=q)

    else:
        students = Student.objects.all()

    if 'sort' in request.GET:
        students = Student.objects.all().order_by('name')
    context = {'students':students}
    return render(request,'index.html',context)


def studentRegister(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        Student.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            adress = request.POST.get('adress'),
            phonenumber = request.POST.get('phonenumber'),
            branch = request.POST.get('branch'),
        )
        return redirect('list')

    context = {'form':form}
    return render(request, 'register.html',context)

def studentView(request,pk):
    student = Student.objects.get(id=pk)
    context = {'student':student}
    return render(request,'view_student.html', context)

def editStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        student.name = request.POST.get("name")
        student.email = request.POST.get('email')
        student.adress = request.POST.get('adress')
        student.phonenumber = request.POST.get('phonenumber')
        student.branch = request.POST.get('branch')
        student.save()
        return redirect('list')
    context = {'form': form, 'student': student}
    return render(request, 'register.html',context)



def deleteStudent(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    context = {'student':student}
    return render(request, 'delete.html', context)




    

