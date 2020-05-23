from django.shortcuts import render
from .models import *

def HomeViews (request):
    return render(request,'index.html')


def UnitSolutionViews (request):
    Apu=AnnouncedPuResults.objects.all()
    Pu=PollingUnit.objects.all()
    if 'unit_unique_id' in request.GET:
        Announced_unit_objects=Apu.filter(polling_unit_uniqueid=request.GET['unit_unique_id']).values()
        polling_unit_Id=Pu.filter(uniqueid=request.GET['unit_unique_id'])[0].polling_unit_id
        lga_Id=Pu.filter(uniqueid=request.GET['unit_unique_id'])[0].lga_id
        ward_Id=Pu.filter(uniqueid=request.GET['unit_unique_id'])[0].ward_id
        state_Id=Lga.objects.values().get(lga_id=lga_Id)['state_id']
        context={'unitobjects':Announced_unit_objects,'lga_id':lga_Id,'ward_id':ward_Id,'state_id':state_Id,'polling_unit_id':polling_unit_Id}
        print(request.GET['unit_unique_id'])
        return render(request,'unit_solution.html',context)
    else:
        return render (request,'unit_solution.html')






def SumUnitSolutionViews(request):
    Apu=AnnouncedPuResults.objects.all()
    Pu=PollingUnit.objects.all()
    lga=Lga.objects.all()
    if 'lga_id' in request.GET:
        uniqueid=Pu.filter(lga_id=request.GET['lga_id'])
        id_list=[]
        context=Pol_parties={}
        for i in uniqueid:
            id_list.append(i.uniqueid) ##creates list of units unique id
        for j in id_list:
            party_obj=list(Apu.filter(polling_unit_uniqueid=j).values()) ##List of parties dictionaries and votes in 
            for k in party_obj:
                if k['party_abbreviation'] in Pol_parties.keys():
                    Pol_parties[k['party_abbreviation']] += k['party_score']

                else:
                    Pol_parties[k['party_abbreviation']] = k['party_score']
        context={'pol_parties':Pol_parties,'number_pu':len(id_list)}
        return render(request,'sumunit_solution.html',context)
    else:
        return render(request,'sumunit_solution.html')

def NewUnitViews (request):
    return render(request,'newunit.html')


