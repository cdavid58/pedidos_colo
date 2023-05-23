from django.http import HttpResponse
from django.shortcuts import render
from inventory.models import Product, Category
from order.models import Order
import json, socket

def Orders(request):
	return render(request,'index.html',{'cat':Category.objects.all()})

def List_Product(request):
	if request.is_ajax():
		pk = request.GET['id']
		list_product = Product.objects.filter(category = Category.objects.get(pk = pk))
		data = [
			{
				'pk':i.pk,
				'name':i.name
			}
			for i in list_product
		]

		return HttpResponse(json.dumps(data))

def Send_Order(request):
	if request.is_ajax:
		data = json.dumps(request.GET)
		list_data = []
		for i in data:
			_data = json.loads(data)
			for j in _data:
				for x in json.loads(_data[j]):
					Order(
						name_product = x['name'],
						quantity = x['quantity']
					).save()
					list_data.append({
						'name_product' : x['name'],
						'quantity' : x['quantity']
						})
			break
		Activate_Client(request,list_data)
	return HttpResponse(True)

def Activate_Client(request, data):
    host = '25.35.176.44'
    port = 1234
    print(data)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    json_data = json.dumps(data)
    client_socket.send(json_data.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print("Respuesta del servidor:", response)
    client_socket.close()
