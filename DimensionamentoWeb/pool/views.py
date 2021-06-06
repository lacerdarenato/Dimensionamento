from django.shortcuts import render
from . import forms


def cadastro(request):
    form = forms.PoolForm()
    data_dict = {'form': form}
    return render(request, 'pool/pool.html', data_dict)
