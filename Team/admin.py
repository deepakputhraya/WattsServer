from django.contrib import admin
from Team.models import TeamMember

class TeamMemberAdmin(admin.ModelAdmin):
  list_display = ('name', 'description')

admin.site.register(TeamMember,TeamMemberAdmin)