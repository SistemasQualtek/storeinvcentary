from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ProductoList,
    ProductoCreation,
    ProductoUpdate,
    ProductoDelete
)
urlpatterns = [
    url(r'^$',views.principal, name='principal'),
    url(r'^inicio/',views.inicio, name='inicio'),
    url(r'^Lista/Productos/',views.ProductoList, name='producto_list'),
    url(r'^Producto/(?P<pk>[0-9]+)/$',views.ProductoDetail,name='producto_detail'),
    url(r'^Entrada/(?P<pk>[0-9]+)/$',views.EntradaDetail,name='padentro'),
    url(r'^Salida/(?P<pk>[0-9]+)/$',views.SalidaDetail,name='pafuera'),
    url(r'^Producto/Nuevo',views.producto,name="producto"),
    url(r'^Categoria/Nueva',views.categoria,name="categoria"),
    url(r'^Venta/Nueva',views.venta,name="venta"),
    url(r'^Lista/Ventas/',views.listaventas,name="listaventas"),
    url(r'^Pdf/Dia',views.pdfdia,name="pdfdia"),
    url(r'^Pdf/General',views.pdfgen,name="pdfgen"),
    url(r'^PDF/Grafica',views.grafica_pastel,name="grafica_pastel"),
    url(r'^Editar/(?P<pk>\d+)', login_required(ProductoUpdate.as_view()), name='edit'),
    url(r'^Borrar/(?P<pk>\d+)', login_required(ProductoDelete.as_view()), name='delete'),
]
