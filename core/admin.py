from django.contrib import admin
from django.utils.html import format_html
from .models import Group, Subject, Teacher, Student, Mark, Raspisanie


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'view_students', 'view_raspisanie']
    list_display_links = ['id', 'name']
    search_fields = ['name']

    def view_students(self, obj):
        return format_html(f'<a href="/admin/core/student/?group__id__exact={obj.id}">{obj.student_set.count()} студентов</a>')
    
    def view_raspisanie(self, obj):
        return format_html(f'<a href="/admin/core/raspisanie/?group__id__exact={obj.id}">{obj.raspisanie_set.count()} пар</a>')
    
    view_students.short_description = 'Студенты'
    view_raspisanie.short_description = 'Расписание'


admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Mark)
admin.site.register(Raspisanie)