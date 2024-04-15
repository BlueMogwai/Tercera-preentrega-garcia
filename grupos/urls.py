from django.urls import path

from .views import(
    join_class_form_view,
    create_class_form_view,
    create_group_form_view,
    home_view,
    list_view,
    search_view,
    search_with_form_view,
    detail_view,
    detail_class_view,
    detail_group_view
)

urlpatterns = [
    path("", home_view),
    path("detail/<reservas_id>", detail_view),
    path("list/", list_view, name="grupos-list"),
    path("buscar/<musico>", search_view),
    path("buscar-con-formulario/", search_with_form_view, name="buscar-musico-con-form"),
    path("unirse-con-formulario/", join_class_form_view, name="unirse-clase-con-form"),
    path("crear-clase-con-formulario/", create_class_form_view, name="crear-clase-con-form"),
    path("crear-grupo-con-formulario/", create_group_form_view, name="crear-grupo-con-form"),
    path("detail-clase/<clase_id>", detail_class_view, name="detalle-clase"),
    path("detail-grupo/<grupo_id>", detail_group_view, name="detalle-grupo")

]