from cProfile import label
import math
from django import forms
from .tensCis import TensCis
import planesections as ps


class TensCis_Forms(forms.Form):
    cargaExerc = forms.FloatField(label="Carga exercida sobre a peça [N]: ")
    nRebites = forms.FloatField(label="Número de rebites: ")
    pRebites = forms.FloatField(label="Pontos do rebite a cisalhar: ")
    dRebites = forms.FloatField(label="Diâmetro do(s) rebite(s) [mm]: ")
    
    def tensaoCis(self):
        print(f"Função selecionada: Tensão de cisalhamento sobre o(s) rebite(s).\n")
        Q = self.cleaned_data.get("cargaExerc")
        n = self.cleaned_data.get("nRebites")
        N = self.cleaned_data.get("pRebites")
        d = self.cleaned_data.get("dRebites")

        #calculo da tensão de cisalhamento sobre o(s) rebite(s)
        result_cis = Q/(n*N*(math.pi/4)*math.pow(d, 2))
        
        #exibe o resultado do cálculo em MPa
        return result_cis

class MomFletor_Forms(forms.Form):
    cargaExerc = forms.FloatField(label="Intensidade da força que origina o Momento Fletor [N]: ")
    distRef = forms.FloatField(label="Distância entre o ponto de referência e o ponto onde a força é aplicada[m]: ")
    
    def momFletor(self):
        print(f"\nFunção selecionada: Cálculo de Momento Fletor.")

        F = self.cleaned_data.get("cargaExerc")
        l = self.cleaned_data.get("distRef")

        resMomento = F*l

        return resMomento

class MaxFlexao_Forms(forms.Form):
    mom_fletor = forms.FloatField(label=f"Momento fletor sobre a peça [Nm]: ")
    raio_rebite = forms.FloatField(label=f"Raio do rebite [m]: ")
    momento_inercia = forms.FloatField(label="Momento de inércia da geometria [m⁴]: ")

    def maxFlexao(self):
        print(f"\nFunção selecionada: Tensão Máxima de Flexão.")

        M = self.cleaned_data.get("mom_fletor")
        y = self.cleaned_data.get("raio_rebite")
        I = self.cleaned_data.get("momento_inercia")

        flexao = M*y/I*(1e-6)

        return flexao

class TensNormal_Forms(forms.Form):
    area = forms.FloatField(label=f"Área da peça [m²]: ")
    forca = forms.FloatField(label=f"Força a ser aplicada [N]: ")

    def tensNormal(self):
        A = self.cleaned_data.get("area")
        N = self.cleaned_data.get("forca")

        E = N/A
        return E