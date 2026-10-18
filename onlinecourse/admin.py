from django.contrib import admin

from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission,
)


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date', 'total_enrollment')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'course', 'order')
    list_filter = ['course']
    search_fields = ['title', 'content']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'lesson', 'grade')
    list_filter = ['lesson__course']
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'is_correct')
    list_filter = ['is_correct']


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'enrollment', 'submitted_at')
    readonly_fields = ('submitted_at',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)
