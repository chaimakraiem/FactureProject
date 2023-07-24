from django.urls import path
from . import views

urlpatterns = [
    path('SignupPage/',views.SignupPageView,name='Signup'),
    path('',views.HomePageView,name='home'), 
    path('logout/',views.LogoutView,name='logout'),
    path('facture/',views.FactureView.as_view(),name='FactureView'), 
    path('add-customer/',views.AddCustomerView.as_view(),name='add-customer'),
    path('add-invoice/', views.AddInvoiceView.as_view(), name='add-invoice'),
    path('view-invoice/<int:pk>', views.InvoiceVisualizationView.as_view(), name='view-invoice'),
    path('invoice-pdf2/<int:pk>', views.get_invoice_pdf, name="invoice-pdf2"),
    path('LoginPage/',views.LoginPageView,name='login'), 

]
