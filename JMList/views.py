from django.shortcuts import render, redirect
from django.http import HttpResponse
from JMList.models import Item, Employee

def homepage(request):
	return render(request, 'homepage.html')

def View_List(request, eID):
	empId = Employee.objects.get(id=eId)
	return render(request, 'idlist.html', {'EmpId':empId})

def New_List(request):
	newEmp = Employee.objects.create(eName=request.POST['newEmployee'],eAddress=request.POST['newAddress'])
	return redirect(f'/JMList/{newEmp.id}/')

def Add_Item(request, eID):
	empID = Employee.objects.get(id=eID)
	Item.objects.create(EmpId=empId, ValID=request.POST['validEntry'],ValNum=request.POST['validNumber'],ValDate=request.POST['validDate'])
	return redirect(f'/JMList/{empId.id}/')

def dataManipulation(request):
	#Creating
	employee = Employee(Name="", Address ="", PhoneNumber="", EmailAddress="")
	employee.save()

	#Read all in employee
	objects = Employee.objects.all()
	result ='Printing all of the entries under Employee model : <br>'
	for x in objects:
		result += x.Name+"<br>"

	#Read specific entry in employee
	ename = Employee.objects.get(id="")
	result += 'Printing only one entry <br>'
	result += ename.PhoneNumber

	#Delete
	result += 'Deleting an entry <br>'
	ename.delete()

	#Update
	employee = Employee.objects.get(name ='')
	employee.PhoneNumber = ""
	employee.save = ""
	res = ""

	#Filtering
	jm = ValidID.objects.filtered(Name = "")
	result += "Found : %s results <br>" % len (jm)

	#Ordering
	jm = Employee.objects.ordered_by("Address")
	for x in jm:
		result += x.Name + x.Address + '<br>'



'''
def homepage(request):
	items = Item.objects.all()
	return render(request, 'homepage.html',{'items' : items})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'idlist.html', {'list':list_})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['newFirst'],last=request.POST['newLast'],list=list_)
	return redirect(f'/JMList/{list_.id}/')

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(valID=request.POST['validEntry'],valNum=request.POST['validNumber'],date=request.POST['validDate'],list=list_)
	return redirect(f'/JMList/{list_.id}/')'''


'''	
	if request.method == 'POST':
		Item.objects.create(text=request.POST['validEntry'])
		return redirect('/')
	items = Item.objects.all()
	return render(request,'homepage.html',{'items':items})'''


#def homepage(request):
	#return render(request,'homepage.html',{'validEntry':request.POST.get('validEntry',''),'validNumber':request.POST.get('validNumber',''),'validDate':request.POST.get('validDate',''),})

'''def homepage(request):
	item1 = Item()
	item1.text=request.POST.get('validEntry','')
	item1.save()
	return render(request,'homepage.html',{'newEntry': item1.text,})

#def homepage(request):
	if request.method == 'POST':
		newItem = request.POST['validEntry']
		Item.objects.create(text=newItem)
	else:
		newItem=''
	return render(request,'homepage.html',{'newEntry':newItem,})'''


#from django.shortcuts import render
#from django.http import HttpResponse
																																																																																																																																																																																																				
#def home_page(request):																																																													
#	return HttpResponse('<html><title>Student List</title></html>')																																		
# Create your views here