from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _


class HttpStatusCodeFilter(admin.SimpleListFilter):
    title = _("http status code")
    parameter_name = "http_status_code"

    def lookups(self, request, model_admin):
        return [
            ("100", _("1xx")),
            ("200", _("2xx")),
            ("300", _("3xx")),
            ("400", _("4xx")),
            ("500", _("5xx")),
        ]

    def queryset(self, request, queryset):
        if self.value() == "100":
            return queryset.filter(
                http_status_code__gte=100,
                http_status_code__lte=199,
            )
        if self.value() == "200":
            return queryset.filter(
                http_status_code__gte=200,
                http_status_code__lte=299,
            )
        if self.value() == "300":
            return queryset.filter(
                http_status_code__gte=300,
                http_status_code__lte=399,
            )
        if self.value() == "400":
            return queryset.filter(
                http_status_code__gte=400,
                http_status_code__lte=499,
            )
        if self.value() == "500":
            return queryset.filter(
                http_status_code__gte=500,
                http_status_code__lte=599,
            )


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'method', 'length', 'http_status_code', 'status', 'time_create', 'time_update',)
    list_display_links = ('id', 'url', 'length',)
    list_filter = [HttpStatusCodeFilter]
    search_fields = ('url', 'method', 'length', 'http_status_code', 'status',)


admin.site.register(Task, TaskAdmin,)
