from django.shortcuts import render,HttpResponseRedirect
from happ.models import *
import os
import hashlib
import random
import string 
from django.conf import settings
from django.core.mail import send_mail
import datetime
# Create your views here.
def INDEX(request):
	prd=product_tb.objects.all()[:4]
	prd1=product_tb.objects.all()
	return render(request,"index.html",{"data":prd,"data1":prd1})

def SEARCH(request):
	if request.method=="POST":
		name=request.POST['search']
		pro=product_tb.objects.filter(name=name)
		if pro:
			return render(request,"single.html",{"data":pro})
		else:
			return HttpResponseRedirect("/product/")
	else:
		return render(request,"index.html")

def OWNERACCOUNT(request):
	if request.session.has_key("myid"):
		us1=request.session["myid"]
		owner=register_tb.objects.filter(id=us1)
		return render(request,"owneraccount.html",{"data":owner})
	else:
		return HttpResponseRedirect("/")

def USERACCOUNT(request):
	if request.session.has_key("userid"):
		us1=request.session["userid"]
		user=user_tb.objects.filter(id=us1)
		return render(request,"useraccount.html",{"data":user})
	else:
		return HttpResponseRedirect("/")

def CONTACT(request):
	if request.method=="POST":
		cname=request.POST['cName']
		cemail=request.POST['cEmail']
		cmessage=request.POST['cMessage']
		check=contact_tb.objects.filter(email=cemail)
		if check:
			return render(request,"contact.html",{"msg":"email already registered"})
		else:
			add=contact_tb(name=cname,email=cemail,message=cmessage)
			add.save()
			return render(request,"contact.html",{"msg":"thk u 4 the feedback"})
	else:
		return render(request,"contact.html")

def PRODUCT(request):
	prd=product_tb.objects.filter(status="1")
	return render(request,"product.html",{"data":prd})

def REGISTER(request):
	if request.method=="POST":
		cfname=request.POST['rFname']
		clname=request.POST['rLname']
		cemail=request.POST['rEmail']
		cpassword=request.POST['rPassword']
		cphone=request.POST['rPhone']
		hashpass=hashlib.md5(cpassword.encode('utf8')).hexdigest()
		check=register_tb.objects.filter(email=cemail)
		if check:
			return render(request,"register.html",{"msg":"email already registered"})
		else:
			add=register_tb(fname=cfname,lname=clname,email=cemail,password=cpassword,epassword=hashpass,phone=cphone,status="0")
			add.save()
			# x = ''.join(random.choices(fname + string.digits, k=8))
			# y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
			# subject = 'welcome to whatsapp'
			# message = f'Hi {fname} {lname}, thank you for registering in whatsapp . your ownername: {fname} and password: {password}. Follow https://Wa.me/+18478527243 or https://www.tinder.com'
			# email_from = settings.EMAIL_HOST_owner
			# recipient_list = [email, ]
			# send_mail( subject, message, email_from, recipient_list )
			return render(request,"register.html",{"msg":"successfully registered"})
	else:
		return render(request,"register.html")

def USER(request):
	if request.method=="POST":
		fname=request.POST['rFname']
		lname=request.POST['rLname']
		email=request.POST['rEmail']
		password=request.POST['rPassword']
		phone=request.POST['rPhone']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		check=user_tb.objects.filter(email=email)
		if check:
			return render(request,"user.html",{"msg":"email already registered"})
		else:
			add=user_tb(fname=fname,lname=lname,email=email,password=password,epassword=hashpass,phone=phone)
			add.save()
			return render(request,"user.html",{"msg":"successfully registered"})
	else:
		return render(request,"user.html")

def SINGLE(request):
	if request.session.has_key("myid"):
		if request.method=='GET':
			id6=request.GET['pid']
			prd=product_tb.objects.filter(id=id6)
			pro=product_tb.objects.filter(status="1")
			pr=product_tb.objects.filter(status="1")[:3]
			if prd:
				return render(request,"single.html",{"data":prd,"data2":pro,"data3":pr})
			else:
				return HttpResponseRedirect("/product/")
		else:
			return HttpResponseRedirect("/product/")
	elif request.session.has_key("userid"):
		if request.method=='GET':
			id6=request.GET['pid']
			prd=product_tb.objects.filter(id=id6)
			pro=product_tb.objects.filter(status="1")
			pr=product_tb.objects.filter(status="1")[:3]
			if prd:
				return render(request,"single.html",{"data":prd,"data2":pro,"data3":pr})
			else:
				return HttpResponseRedirect("/product/")
		else:
			return HttpResponseRedirect("/product/")
	else:
		return HttpResponseRedirect("/login/")

def LOGIN(request):
	if request.method=="POST":
		name=request.POST['rFname']
		password=request.POST['rPassword']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		owner=register_tb.objects.filter(fname=name,password=password,status="1")
		user=user_tb.objects.filter(fname=name,password=password)
		if owner:
			for x in owner:
				if request.session.has_key("userid"):
					del request.session["userid"]
				request.session["myid"]=x.id
				request.session["myname"]=x.fname
				prd=product_tb.objects.all()[:4]
				return render(request,"index.html",{"data":prd})
		elif user:
			for x in user:
				if request.session.has_key("myid"):
					del request.session["myid"]
				request.session["userid"]=x.id
				request.session["username"]=x.fname
				prd=product_tb.objects.all()[:4]
				return render(request,"index.html",{"data":prd})
		else:
			return render(request,"login.html",{"msg":"invalid creditionals or not approved"})
	else:
		return render(request,"login.html")
def logout(request):
	if request.session.has_key("myid"):
		del request.session["myid"]
		del request.session["myname"]
		return HttpResponseRedirect("/")
	elif request.session.has_key("userid"):
		del request.session["userid"]
		del request.session["username"]
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/")

def OWNERTAB(request):
	owner=register_tb.objects.all()
	return render(request,"ownertab.html",{"data":owner})

def OWNEREDIT(request):
	if request.method=='GET':
		id2=request.GET['uid']
		owner=register_tb.objects.filter(id=id2)
		if owner:
			return render(request,"ownerupdate.html",{"data":owner})
		else:
			return HttpResponseRedirect("/ownerview/")
	else:
		return HttpResponseRedirect("/ownerview/")

def OWNERUPDATE(request):
	if request.method=="POST":
		id1=request.GET['uid']
		cfname=request.POST['rFname']
		clname=request.POST['rLname']
		cemail=request.POST['rEmail']
		cphone=request.POST['rPhone']
		cpassword=request.POST['rPassword']
		register_tb.objects.filter(id=id1).update(fname=cfname,lname=clname,email=cemail,phone=phone,password=cpassword)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/ownerview/")

def OWNERDELETE(request):
	id1=request.GET['uid']
	owner=register_tb.objects.filter(id=id1).delete()
	return HttpResponseRedirect("/ownerview/")

def OWNEREDITPASSWORD(request):
	if request.method=='GET':
		id9=request.GET['uid']
		owner=register_tb.objects.filter(id=id9)
		if owner:
			return render(request,"ownerchangepassword.html",{"data":owner})
		else:
			return HttpResponseRedirect("/login/")
	else:
		return HttpResponseRedirect("/login/")

def OWNERCHANGEPASSWORD(request):
	if request.method=="POST":
		id10=request.GET['uid']
		password=request.POST['rPassword']
		register_tb.objects.filter(id=id10).update(password=password)
		return HttpResponseRedirect("/login/")
	else:
		return HttpResponseRedirect("/login/")

def FORGOTPASSWORD(request):
	if request.method=="POST":
		fname=request.POST['rFname']
		owner=register_tb.objects.filter(fname=fname)
		user=user_tb.objects.filter(fname=fname)
		if owner:
			return render(request,"ownerchangepassword.html",{"data":owner})
		elif user:
			return render(request,"userchangepassword.html",{"data":user})
		else:
			return HttpResponseRedirect("/login/")
	else:
		return render(request,"forgotpassword.html")

def USERTAB(request):
	user=user_tb.objects.all()
	return render(request,"usertab.html",{"data":user})

def USEREDIT(request):
	if request.method=='GET':
		id10=request.GET['usid']
		user=user_tb.objects.filter(id=id10)
		if user:
			return render(request,"userupdate.html",{"data":user})
		else:
			return HttpResponseRedirect("/userview/")
	else:
		return HttpResponseRedirect("/userview/")

def USERUPDATE(request):
	if request.method=="POST":
		id11=request.GET['usid']
		fname=request.POST['rFname']
		lname=request.POST['rLname']
		email=request.POST['rEmail']
		phone=request.POST['rPhone']
		password=request.POST['rPassword']
		user_tb.objects.filter(id=id11).update(fname=fname,lname=lname,email=email,phone=phone,password=password)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/userview/")

def USERDELETE(request):
	id12=request.GET['usid']
	user=user_tb.objects.filter(id=id12).delete()
	return HttpResponseRedirect("/userview/")

def USEREDITPASSWORD(request):
	if request.method=='GET':
		id13=request.GET['usid']
		user=user_tb.objects.filter(id=id13)
		if user:
			return render(request,"userchangepassword.html",{"data":user})
		else:
			return HttpResponseRedirect("/login/")
	else:
		return HttpResponseRedirect("/login/")

def USERCHANGEPASSWORD(request):
	if request.method=="POST":
		id14=request.GET['usid']
		password=request.POST['rPassword']
		user_tb.objects.filter(id=id14).update(password=password)
		return HttpResponseRedirect("/login/")
	else:
		return HttpResponseRedirect("/login/")

def ADDPRODUCTS(request):
	if request.session.has_key("myid"):
		if request.method=="POST":
			name=request.POST['pName']
			price=request.POST['pPrice']
			image=request.FILES['pImage']
			ii=request.session["myid"]
			owner=register_tb.objects.get(id=ii)
			add=product_tb(name=name,price=price,image=image,owner=owner,status="0")
			add.save()
			return render(request,"addproducts.html",{"msg":"successfully added"})
		else:
			return render(request,"addproducts.html")
	else:
		return HttpResponseRedirect("/login/")

def PRODUCTTAB(request):
	if request.session.has_key("myid"):
		ii=request.session["myid"]
		owner=register_tb.objects.get(id=ii)
		product=product_tb.objects.filter(status="1",owner=owner)
		if product:
			return render(request,"producttab.html",{"data":product})
		else:
			return render(request,"producttab.html",{"msg":"not approved"})
	else:
		return HttpResponseRedirect("/login/")

	

def EDITPRODUCT(request):
	if request.method=='GET':
		id4=request.GET['pid']
		product=product_tb.objects.filter(id=id4)
		if product:
			return render(request,"updateproduct.html",{"data":product})
		else:
			return HttpResponseRedirect("/producttab/")
	else:
		return HttpResponseRedirect("/producttab/")

def UPDATEPRODUCT(request):
	if request.method=="POST":
		pr=request.GET['pid']
		name=request.POST['pName']
		price=request.POST['pPrice']
		imgup=request.POST['img']
		if imgup=='yes':
			image1=request.FILES['pImage']
			oldrec=product_tb.objects.filter(id=pr)
			updrec=product_tb.objects.get(id=pr)
			for x in oldrec:
				imgurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('successfully deleted')
			updrec.image=image1
			updrec.save()
		product_tb.objects.filter(id=pr).update(name=name,price=price)
		return HttpResponseRedirect("/producttab/")
	else:
		return HttpResponseRedirect("/producttab/")

def DELETEPRODUCT(request):
	id3=request.GET['pid']
	oldrec=product_tb.objects.filter(id=id3)
	updrec=product_tb.objects.get(id=id3)
	for x in oldrec:
		imgurl=x.image.url
		pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
		if os.path.exists(pathtoimage):
			os.remove(pathtoimage)
			print('successfully deleted')
		updrec.delete()
		product_tb.objects.filter(id=id3).delete()
		return HttpResponseRedirect("/producttab/")
	else:
		return HttpResponseRedirect("/producttab/")

def PROFILE(request):
	if request.session.has_key("myid"):
		us=request.session["myid"]
		profile=register_tb.objects.filter(id=us)
		return render(request,"profile.html",{"data":profile})
	elif request.session.has_key("userid"):
		us=request.session["userid"]
		profile=user_tb.objects.filter(id=us)
		return render(request,"profile.html",{"data":profile})
	else:
		return HttpResponseRedirect("/")

def INDEX1(request):
	return render(request,"backend/index.html")

def SIGNIN(request):
	if request.method=="POST":
		uname=request.POST['aName']
		password=request.POST['aPassword']
		check=signin_tb.objects.filter(uname=uname,password=password)
		if check:
			for x in check:
				request.session["admid"]=x.id
				request.session["admname"]=x.uname
				return render(request,"backend/index.html",{"msg":"login successfull"})
		else:
			return render(request,"backend/signin.html",{"msg":"invalid creditionals"})
	else:
		return render(request,"backend/signin.html")
def signout(request):
	if request.session.has_key("admid"):
		del request.session["admid"]
		return HttpResponseRedirect("/1/")
	else:
		return HttpResponseRedirect("/1/")

def ADMPROFILE(request):
	if request.session.has_key("admid"):
		us=request.session["admid"]
		admin=signin_tb.objects.filter(id=us)
		return render(request,"backend/profile.html",{"data":admin})
	else:
		return HttpResponseRedirect("/1/")

def ADOWNERTAB(request):
	if request.session.has_key("admid"):
		owner=register_tb.objects.all()
		return render(request,"backend/adownertab.html",{"data":owner})
	else:
		return HttpResponseRedirect("/signin/")

def ADUSERTAB(request):
	if request.session.has_key("admid"):
		user=user_tb.objects.all()
		return render(request,"backend/adusertab.html",{"data":user})
	else:
		return HttpResponseRedirect("/signin/")

def APPROVED(request):
	id5=request.GET['uid']
	owner=register_tb.objects.filter(id=id5).update(status="1")
	return HttpResponseRedirect('/adownertab/')

def REJECTED(request):
	id6=request.GET['uid']
	owner=register_tb.objects.filter(id=id6).update(status="2")
	return HttpResponseRedirect('/adownertab/')

def ADCARTTAB(request):
	if request.session.has_key("admid"):
		cart=cart_tb.objects.all()
		return render(request,"backend/adcarttab.html",{"data":cart})
	else:
		return HttpResponseRedirect("/signin/")

# def ADMINADDPRODUCTS(request):
# 	if request.method=="POST":
# 		name=request.POST['pName']
# 		price=request.POST['pPrice']
# 		image=request.FILES['pImage']
# 		add=product_tb(name=name,price=price,image=image,status="0")
# 		add.save()
# 		return HttpResponseRedirect("/product/")
# 	else:
# 		return render(request,"backend/adminaddproducts.html")

def ADMINPROTAB(request):
	if request.session.has_key("admid"):
		product=product_tb.objects.all()
		return render(request,"backend/adminaddprotab.html",{"data":product})
	else:
		return HttpResponseRedirect("/signin/")

def PROAPPROVED(request):
	id7=request.GET['pid']
	admin=product_tb.objects.filter(id=id7).update(status="1")
	return HttpResponseRedirect('/adminprotab/')

def PROREJECTED(request):
	id8=request.GET['pid']
	admin=product_tb.objects.filter(id=id8).update(status="2")
	return HttpResponseRedirect('/adminprotab/')

def ADDCART(request):
	if request.session.has_key("userid"):
		if request.method=="POST":
			pids=request.GET['id']
			prd=product_tb.objects.filter(id=pids)
			for x in prd:
				unitprice=x.price
			qty=request.POST['qty']
			shipping=int(int(unitprice)*10/100)
			total=int(unitprice)*int(qty)+shipping
			date= datetime.datetime.now()
			ii=request.session["userid"]
			uid=user_tb.objects.get(id=ii)
			pid=product_tb.objects.get(id=pids)
			ii=user_tb.objects.get(id=ii)
			check=cart_tb.objects.filter(user=ii,pid=pids,status="pending")
			if check:
				for x in check:
					cartid=x.id
					print(cartid,"++++++++++++++")
					cart_tb.objects.filter(id=cartid).update(price=unitprice,totalprice=total,date=date,quantity=qty)
					myprd=cart_tb.objects.all().filter(user=ii,status="pending")
					grandtotal=0
					for x in myprd:
						grandtotal=int(x.totalprice)+grandtotal
					return render(request,'cart.html',{'msgkey':'cart updated','gt':grandtotal,"data":myprd})
			else:
				data=product_tb.objects.all().filter(id=pids)
				for x in data:
					owner=x.owner
				tocart=cart_tb(user=ii,pid=pid,owner=owner,price=unitprice,totalprice=total,date=date,quantity=qty,status="pending")
				tocart.save()
				myprd=cart_tb.objects.all().filter(user=ii,status="pending")
				grandtotal=0
				for x in myprd:
					grandtotal=int(x.totalprice)+grandtotal
				return render(request,'cart.html',{'msgkey':'Added to cart','gt':grandtotal,"data":myprd})
		else:
			return render(request,"login.html")
	else:
		return HttpResponseRedirect("/login/")

def CART(request):
	if request.session.has_key("userid"):
		ii=request.session["userid"]
		cart=cart_tb.objects.filter(user=ii,status="pending")
		myprd=cart_tb.objects.all().filter(user=ii,status="pending")
		grandtotal=0
		if myprd:
			for x in myprd:
				grandtotal=int(x.totalprice)+grandtotal
			return render(request,'cart.html',{'gt':grandtotal,"data":myprd})
		else:
			# mypr=cart_tb.objects.all().filter(user=ii,status="payed")
			# grandtotal=0
			# for x in mypr:
			# 	grandtotal=float(x.totalprice)+grandtotal
			return render(request,'cart.html',{'gt':grandtotal,"data":myprd})
	else:
		return HttpResponseRedirect("/login/")

def REMOVE(request):
	cid=request.GET['id']
	cart_tb.objects.filter(id=cid).delete()
	return HttpResponseRedirect("/cart/")

def CHECKOUT(request):
	if request.session.has_key("userid"):
		cid=request.GET['id']
		ii=request.session["userid"]
		cart=product_tb.objects.filter(id=cid,status="1")
		myprd=product_tb.objects.all().filter(id=cid,status="1")
		grandtotal=0
		for x in myprd:
			grandtotal=float(x.price)
		return render(request,'checkout.html',{'gt':grandtotal,"data1":myprd})
	else:
		return HttpResponseRedirect("/login/")

def REMOVEALL(request):
	if request.session.has_key("userid"):
		ii=request.session["userid"]
		cart_tb.objects.filter(user=ii,status="pending").delete()
		return HttpResponseRedirect("/cart/")
	else:
		return HttpResponseRedirect("/cart/")

def INDEX2(request):
	return render(request,"payment/index.html")

def PAYMENT(request):
	if request.session.has_key("userid"):
		if request.method=="POST":
			nameoncard=request.POST['pcName']
			uid=request.session['userid']
			uname=user_tb.objects.get(id=uid)
			date=datetime.datetime.now()
			mypr=cart_tb.objects.all().filter(user=uid,status="pending")
			for x in mypr:
				cartid=x.id
				cid=cart_tb.objects.get(id=cartid)
				grandtotal=request.POST['total']
				payment=payment_tb(nameoncard=nameoncard,username=uname,date=date,cartid=cid,grandtotal=grandtotal,status="payed")
				payment.save()
				cart_tb.objects.all().filter(user=uid,status="pending").update(status="payed")
			return HttpResponseRedirect("/bookingtab/")
		else:
			grandtotal=request.GET['gt']
			return render(request,"payment/index.html",{'gt':grandtotal})
	else:
		return HttpResponseRedirect("/login/")

def PROPAYMENT(request):
	if request.session.has_key("userid"):
		if request.method=="POST":
			nameoncard=request.POST['pcName']
			uid=request.session['userid']
			uname=user_tb.objects.get(id=uid)
			date=datetime.datetime.now()
			mypr=cart_tb.objects.all().filter(user=uid,status="pending")
			for x in mypr:
				cartid=x.id
				pid=x.pid
				cid=cart_tb.objects.get(id=cartid)
			grandtotal=request.POST['total']
			payment=payment_tb(nameoncard=nameoncard,username=uname,date=date,cartid=cid,grandtotal=grandtotal,status="payed")
			payment.save()
			cart_tb.objects.all().filter(pid=x.pid,user=uid,status="pending").update(status="payed")
			return HttpResponseRedirect("/cart/")
		else:
			grandtotal=request.GET['gd']
			return render(request,"payment/propayment.html",{'gd':grandtotal})
	else:
		return HttpResponseRedirect("/login/")


def BOOKEDORDERS(request):
	if request.session.has_key("myid"):
		ii=request.session["myid"]
		myprd=cart_tb.objects.all().filter(owner=ii,status="payed")
		if myprd:
			for x in myprd:
				owner=x.owner
				user=x.user
				return render(request,'bookedorder.html',{"data":myprd})
		else:
			return render(request,"bookedorder.html")
	else:
		return HttpResponseRedirect("/login/")

def BOOKING(request):
	if request.session.has_key("userid"):
		ii=request.session["userid"]
		# cart=cart_tb.objects.filter(name=ii,status="pending")
		myprd=cart_tb.objects.all().filter(user=ii,status="payed")
		grandtotal=0
		if myprd:
			for x in myprd:
				grandtotal=float(x.totalprice)+grandtotal
			return render(request,'bookingtab.html',{'gt':grandtotal,"data":myprd})
		else:
			return render(request,'bookingtab.html',{'gt':grandtotal,"data":myprd})
	else:
		return HttpResponseRedirect("/login/")

def FEEDBACK(request):
	if request.session.has_key("userid"):
		id21=request.GET['pid']
		print(id21,"************")
		pro=product_tb.objects.get(id=id21)
		print(pro,"************")
		prod=product_tb.objects.all().filter(id=id21)
		for x in prod:
			ownerid=x.owner
		if request.method=="POST":
			ii=request.session["userid"]
			uid=user_tb.objects.get(id=ii)
			feedback=request.POST["rFeedback"]
			feed=feedback_tb(uid=uid,proid=pro,owner=ownerid,feedback=feedback)
			feed.save()
			return render(request,"feedback.html")
		else:
			return render(request,"feedback.html",{"pid":id21})
	else:
		return HttpResponseRedirect("/login/")

def FEEDBACKED(request):
	if request.session.has_key("myid"):
		ii=request.session["myid"]
		feedb=feedback_tb.objects.all().filter(owner=ii)
		return render(request,"feedbacktab.html",{"data":feedb})
	else:
		return HttpResponseRedirect("/login/")