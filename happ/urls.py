from django.urls import path
from happ import views
urlpatterns = [
   path('',views.INDEX),
   path('owneraccount/',views.OWNERACCOUNT),
   path('useraccount/',views.USERACCOUNT),
   path('contact/',views.CONTACT),
   path('product/',views.PRODUCT),
   path('register/',views.REGISTER),
   path('user/',views.USER),
   path('single/',views.SINGLE),
   path('login/',views.LOGIN),
   path('logout/',views.logout),
   path('ownerview/',views.OWNERTAB),
   path('editowner/',views.OWNEREDIT),
   path('ownerupdate/',views.OWNERUPDATE),
   path('deleteowner/',views.OWNERDELETE),
   path('userview/',views.USERTAB),
   path('edituser/',views.USEREDIT),
   path('userupdate/',views.USERUPDATE),
   path('deleteuser/',views.USERDELETE),
   path('profile/',views.PROFILE),
   path('search/',views.SEARCH),
   path('addcart/',views.ADDCART),
   path('cart/',views.CART),
   path('remove/',views.REMOVE),
   path('removeall/',views.REMOVEALL),
   path('ownereditpassword/',views.OWNEREDITPASSWORD),
   path('ownerchangepassword/',views.OWNERCHANGEPASSWORD),
   path('usereditpassword/',views.USEREDITPASSWORD),
   path('userchangepassword/',views.USERCHANGEPASSWORD),
   path('forgotpassword/',views.FORGOTPASSWORD),
   path('addproducts/',views.ADDPRODUCTS),
   path('producttab/',views.PRODUCTTAB),
   path('editproduct/',views.EDITPRODUCT),
   path('updateproduct/',views.UPDATEPRODUCT),
   path('deleteproduct/',views.DELETEPRODUCT),
   path('1/',views.INDEX1),
   path('signin/',views.SIGNIN),
   path('signout/',views.signout),
   path('admprofile/',views.ADMPROFILE),
   path('adownertab/',views.ADOWNERTAB),
   path('adusertab/',views.ADUSERTAB),
   path('approved/',views.APPROVED),
   path('rejected/',views.REJECTED),
   path('adcarttab/',views.ADCARTTAB),
   # path('adminaddproducts/',views.ADMINADDPRODUCTS),
   path('adminprotab/',views.ADMINPROTAB),
   path('proapproved/',views.PROAPPROVED),
   path('prorejected/',views.PROREJECTED),
   path('2/',views.INDEX2),
   path('payment/',views.PAYMENT),
   path('propayment/',views.PROPAYMENT),
   path('bookingtab/',views.BOOKING),
   path('bookedorders/',views.BOOKEDORDERS),
   # path('bookingorders/',views.BOOKINGORDERS),
   path('checkout/',views.CHECKOUT),
   path('feedback/',views.FEEDBACK),
   path('feedbacked/',views.FEEDBACKED),



]