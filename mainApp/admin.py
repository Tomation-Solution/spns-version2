from django.contrib import admin

from . import models

admin.site.register(models.ServiceModel)
admin.site.register(models.PeopleDataForPdf)
admin.site.register(models.Contact)


admin.site.site_header ="Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Your Admin Dashboard"





class researchinsight_ParaGraphConten(admin.TabularInline):
    model = models.researchinsight_ParaGraph
    extra=1

class ResearchInsightInfoAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['heading','cover_image','intro_content','pdf_file']})]
    inlines=[researchinsight_ParaGraphConten]


admin.site.register(models.ResearchInsightInfo,ResearchInsightInfoAdmin)

