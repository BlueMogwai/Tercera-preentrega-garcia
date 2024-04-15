from django import forms

from .models import Grupo, Clase, Reserva

class ReservaSearchForm(forms.Form):
    musico = forms.CharField(max_length=50, required=True, label="Ingresar nombre del músico")

class ReservaCreateForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            "nombre",
            "instrumento",
            "seccion",
            "experiencia",
            "presentacion",
            "clase",
        ]
        labels = {
            "nombre": "Nombre del músico",
            "instrumento": "Instrumento principal que tocas",
            "seccion": "Familia a la que pertenece tu instrumento",
            "experiencia": "Experiencia en grupos",
            "presentacion": "Cuéntanos algo sobre ti y tu experiencia musical",
        }


class ClaseCreateForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = [
            "nombre", 
            "disponible",
            "numero_de_musicos",
            "grupo",
            "descripcion",
            "fecha",
            "hora_inicio",
            "hora_fin",
        ]    
        labels = {
            "nombre": "Nombre de la clase", 
            "disponible": "Disponible",
            "numero_de_musicos": "Número de músicos",
            "grupo": "Grupo",
            "descripcion": "Descripción",
            "clase": "A qué clase quieres unirte",
            "fecha": "Fecha",
            "hora_inicio": "Hora de inicio",
            "hora_fin": "Hora de finalización",
        }

class GrupoCreateForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = [
            "nombre",
            "size",
            "tipo",
            "descripcion",
        ]
        labels = {
            "nombre": "Nombre del grupo",
            "size": "Tipo de grupo por tamaño",
            "tipo": "Grupo instrumental o con voz",
            "descripcion": "Descripción del grupo y su estilo"
        }