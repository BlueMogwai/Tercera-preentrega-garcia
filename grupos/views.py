from django.shortcuts import render
from .forms import ReservaCreateForm, ReservaSearchForm, ClaseCreateForm, GrupoCreateForm
from .models import Size, Tipo, Grupo, Clase, Reserva

def join_class_form_view(request):
    if request.method == "GET":
        contexto = {"create_reserva_form": ReservaCreateForm()}
        return render(request, "grupos/join-group.html", contexto)
    elif request.method == "POST":
        form = ReservaCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            clase = form.cleaned_data["clase"]
            instrumento = form.cleaned_data["instrumento"]
            seccion = form.cleaned_data["seccion"]
            experiencia = form.cleaned_data["experiencia"]
            presentacion = form.cleaned_data["presentacion"]
            nueva_reserva = Reserva(
                nombre=nombre,
                clase=clase,
                instrumento=instrumento,
                seccion=seccion,
                experiencia=experiencia,
                presentacion=presentacion,
            )
            nueva_reserva.save()
            return detail_class_view(request, clase.id)

def create_class_form_view(request):
    if request.method == "GET":
        contexto = {"create_form": ClaseCreateForm}
        return render(request, "grupos/form-create-clase.html", contexto)
    elif request.method == "POST":
        form = ClaseCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            disponible = form.cleaned_data["disponible"]
            numero_de_musicos = form.cleaned_data["numero_de_musicos"]
            grupo = form.cleaned_data["grupo"]
            descripcion = form.cleaned_data["descripcion"]
            fecha = form.cleaned_data["fecha"]
            hora_inicio = form.cleaned_data["hora_inicio"]
            hora_fin = form.cleaned_data["hora_fin"]
            nueva_clase = Clase(
                nombre=nombre,
                disponible=disponible,
                numero_de_musicos=numero_de_musicos,
                grupo=grupo,
                descripcion=descripcion,
                fecha=fecha,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
                )
            nueva_clase.save()
            return detail_class_view(request, nueva_clase.id)

def create_group_form_view(request):
    if request.method == "GET":
        contexto = {"create_group_form": GrupoCreateForm}
        return render(request, "grupos/form-create-grupo.html", contexto)
    elif request.method == "POST":
        form = GrupoCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            size = form.cleaned_data["size"]
            tipo = form.cleaned_data["tipo"]
            descripcion = form.cleaned_data["descripcion"]
            nuevo_grupo = Grupo(
                nombre=nombre,
                size=size,
                tipo=tipo,
                descripcion=descripcion,
                )
            nuevo_grupo.save()
            return detail_group_view(request, nuevo_grupo.id)

def home_view(request):
    return render(request, "grupos/home.html")

def list_view(request):
    clases = Clase.objects.all()
    contexto = {"todas_las_clases": clases}
    return render(request, "grupos/list.html", contexto)

def search_view(request, musico):
    clases_del_usuario = Clase.objects.filter(musico=musico)
    contexto = {"todos_las_clases": clases_del_usuario}
    return render(request, "grupos/list.html", contexto)

def search_with_form_view(request):
    if request.method == "GET":
        form = ReservaSearchForm()
        return render(request, "grupos/form-search.html", context={"search_form": form})
    elif request.method == "POST":
        form = ReservaSearchForm(request.POST)
        if form.is_valid():
            musico = form.cleaned_data["musico"]
            reservas_del_musico = Reserva.objects.filter(nombre=musico)
            contexto = {"todas_las_clases": reservas_del_musico}
            return render(request, "grupos/detail.html", contexto)
        else:
            return render(request, "grupos/form-search.html", {"search_form": form})
    
def detail_view(request, reservas_id):
    reserva = Reserva.objects.get(id=reservas_id)
    contexto = {"reserva": reserva}
    return render(request, "grupos/detail.html", contexto)

def detail_class_view(request, clase_id):
    clase = Clase.objects.get(id=clase_id)
    contexto = {"clase": clase}
    return render(request, "grupos/detail-clase.html", contexto)

def detail_group_view(request, grupo_id):
    grupo = Grupo.objects.get(id=grupo_id)
    contexto = {"grupo": grupo}
    return render(request, "grupos/detail-grupo.html", contexto)