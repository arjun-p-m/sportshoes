from django.db import models

# Create your models here.
class register_tb(models.Model):
	fname=models.CharField(max_length=255)
	lname=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	epassword=models.TextField()
	status=models.CharField(max_length=255)

class user_tb(models.Model):
	fname=models.CharField(max_length=255)
	lname=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	epassword=models.TextField()

class contact_tb(models.Model):
	name=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	message=models.CharField(max_length=255)

class signin_tb(models.Model):
	uname=models.CharField(max_length=255)
	password=models.CharField(max_length=255)

class product_tb(models.Model):
	name=models.CharField(max_length=255)
	price=models.CharField(max_length=255)
	image=models.FileField(upload_to="product",default="")
	owner=models.ForeignKey(register_tb, on_delete=models.CASCADE)
	status=models.CharField(max_length=255)
		
class cart_tb(models.Model):
	pid=models.ForeignKey(product_tb, on_delete=models.CASCADE)
	price=models.CharField(max_length=255)
	totalprice=models.CharField(max_length=255)
	owner=models.ForeignKey(register_tb, on_delete=models.CASCADE)
	user=models.ForeignKey(user_tb, on_delete=models.CASCADE)
	status=models.CharField(max_length=255)
	quantity=models.CharField(max_length=255)
	date=models.CharField(max_length=255)

class payment_tb(models.Model):
	nameoncard=models.CharField(max_length=255)
	username=models.ForeignKey(user_tb, on_delete=models.CASCADE)
	date=models.CharField(max_length=255)
	grandtotal=models.CharField(max_length=255)
	status=models.CharField(max_length=255)
	cartid=models.ForeignKey(cart_tb, on_delete=models.CASCADE)

class feedback_tb(models.Model):
	uid=models.ForeignKey(user_tb, on_delete=models.CASCADE)
	proid=models.ForeignKey(product_tb, on_delete=models.CASCADE)
	owner=models.ForeignKey(register_tb,on_delete=models.CASCADE)
	feedback=models.CharField(max_length=255)

# class newproduct_tb(models.Model):
# 	name=models.CharField(max_length=255)
# 	price=models.CharField(max_length=255)
# 	image=models.FileField(upload_to="product",default="")
# 	addedby=models.CharField(max_length=255)
# 	status=models.CharField(max_length=255)