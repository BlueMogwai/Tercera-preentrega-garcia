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
            "size_del_grupo",
            "descripcion",
            "fecha",
            "hora_inicio",
            "hora_fin",
        ]    
        labels = {
            "nombre": "Elegir nombre del juego",
            "disponible": "Disponible",
            "capacidad": "Número de jugadores",
            "descripcion": "Descripción de la partida",
            "sistema_de_juego": "Sistema de juego",
            "fecha": "Fecha",
            "hora_inicio": "Hora de inicio",
            "hora_fin": "Hora de final"
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
            "tipo": "Grupo instrumental o con vox",
            "descripcion": "Descripción del grupo y su estilo"
        }