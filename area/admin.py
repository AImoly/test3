from django.contrib import admin
from area.models import *


class AreaStackedInline(admin.StackedInline):
    model = AreaInfo  # 关联子对象
    extra = 2  # 额外编辑2个子对象
class AreaInfoTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 2

# Register your models here.
class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "atitle", "title", "parent"]
    list_per_page = 10
    search_fields = ["atitle"]
    actions_on_top = True
    inlines = [AreaStackedInline]
    # inlines = [AreaInfoTabularInline]
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )


admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(Pictest)
