from django import forms

class PoolForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PoolForm, self).__init__(*args, **kwargs)
        self.fields['comprimento'].error_menssages = {'required' : 'Campo Obrigatório'}
        self.fields['largura'].error_menssages = {'required' : 'Campo Obrigatório'}
        self.fields['profundidade'].error_menssages = {'required' : 'Campo Obrigatório'}

    comprimento = forms.FloatField(label='Comprimento', required=True)
    largura = forms.FloatField(label='Largura', required=True)
    profundidade = forms.FloatField(label='Profundidade', required=True)
