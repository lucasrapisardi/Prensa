from cProfile import label
import math
from django import forms
from .tensCis import TensCis
import planesections as ps


class TensCis_Forms(forms.Form):
    cargaExerc = forms.IntegerField(label="Carga exercida sobre a peça [N]: ")
    nRebites = forms.IntegerField(label="Número de rebites: ")
    pRebites = forms.IntegerField(label="Pontos do rebite a cisalhar: ")
    dRebites = forms.IntegerField(label="Diâmetro do(s) rebite(s) [mm]: ")
    
    def tensaoCis(self):
        print(f"Função selecionada: Tensão de cisalhamento sobre o(s) rebite(s).\n")
        Q = self.cleaned_data.get("cargaExerc")
        n = self.cleaned_data.get("nRebites")
        N = self.cleaned_data.get("pRebites")
        d = self.cleaned_data.get("dRebites")

        #calculo da tensão de cisalhamento sobre o(s) rebite(s)
        result_cis = round(Q/(n*N*(math.pi/4)*math.pow(d, 2)))
        
        #exibe o resultado do cálculo em MPa
        return result_cis
