from django.urls import path,include
from .views import *

urlpatterns= [
    path('unitresults/',UnitSolutionViews,name="unit_solution"),
    path('sumunit_solution/',SumUnitSolutionViews,name="sumunit_solution"),
    path('newunit/',NewUnitViews,name='newunit'),
]