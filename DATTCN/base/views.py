from django.shortcuts import render
from .form import DistrictForm
import pickle
import numpy as np

load = pickle.load(open('model_Random_Forest.sav','rb'))
# from .models import *

# Create your views here.

def Home(request):
    predict = 0
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        
        if form.is_valid():
            selected_district_code_quanhuyen = form.cleaned_data['district_quanhuyen']
            selected_district_quanhuyen = dict(form.fields['district_quanhuyen'].choices)[int(selected_district_code_quanhuyen)]
            selected_district_code_xaphuong = form.cleaned_data['district_xaphuong']
            selected_district_xaphuong = dict(form.fields['district_xaphuong'].choices)[int(selected_district_code_xaphuong)]
            selected_district_code_duongpho = form.cleaned_data['district_duongpho']
            selected_district_duongpho = dict(form.fields['district_duongpho'].choices)[int(selected_district_code_duongpho)]
            selected_district_code_duan = form.cleaned_data['district_duan']
            selected_district_duan = dict(form.fields['district_duan'].choices)[int(selected_district_code_duan)]
            selected_district_code_dientich = request.POST.get('district_dientich')
            selected_district_code_phongngu = request.POST.get('district_phongngu')
            selected_district_code_toilet = request.POST.get('district_toilet')
            data = np.array([selected_district_code_duan,selected_district_code_duongpho,
                             selected_district_code_xaphuong,selected_district_code_quanhuyen,
                             selected_district_code_dientich,selected_district_code_phongngu,
                             selected_district_code_toilet]).reshape(1,-1)
            predict = load.predict(data)
            
    else:
        form = DistrictForm()
    context = {'form': form, 'predict':predict}
    return render(request,'index.html',context)