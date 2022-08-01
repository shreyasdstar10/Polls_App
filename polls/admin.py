from django.contrib import admin
from django.utils import timezone
from .models import Question, Choice

admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'pub_date']
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]

    def save_model(self, request, obj, form, change):
        obj.pub_date = timezone.now()
        obj.save()

admin.site.register(Question,QuestionAdmin)
