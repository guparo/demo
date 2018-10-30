from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('video', TemplateView.as_view(template_name='books/video.html'), name='video'),

    path('chart/',          views.chart,                name='chart'),

    path('book_pdf',        views.bookPdf.as_view(),    name='book_pdf'),
    path('book_list',       views.BookList.as_view(),   name='book_list'),
    path('view/<int:pk>',   views.BookView.as_view(),   name='book_view'),
    path('new',             views.BookCreate.as_view(), name='book_new'),
    path('view/<int:pk>',   views.BookView.as_view(),   name='book_view'),
    path('edit/<int:pk>',   views.BookUpdate.as_view(), name='book_edit'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
    path('contact_new',     views.ContactCreate.as_view(),   name='contact_new'),
    path('contact_list',     views.ContactList.as_view(),    name='contact_list'),
    path('passenger_new',   views.PassengerCreate.as_view(), name='passenger_new'),
    path('passenger_list',  views.PassengerList.as_view(),   name='passenger_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)