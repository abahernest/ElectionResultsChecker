from django.urls import path,include
from .views import *

urlpatterns= [
    path('unit/',UnitViews,name='unit'),
    path('unitresults/',UnitSolutionViews,name="unit_solution"),
    path('sumunit/',SumUnitViews,name='sumunit'),
    path('sumunit_solution/',SumUnitSolutionViews,name="sumunit_solution"),
    path('newunit/',NewUnitViews,name='newunit'),
]