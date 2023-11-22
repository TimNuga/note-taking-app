from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from .views import NoteList, NoteDetail, SummarizeNoteView

schema_view = get_schema_view(
    openapi.Info(
        title="Note Taking API",
        default_version='v1',
        description="API for note-taking",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('notes/', NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
    path('notes/<int:pk>/summarize/', SummarizeNoteView.as_view(), name='summarize-note'),
    path('admin/', admin.site.urls),

    
    # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
