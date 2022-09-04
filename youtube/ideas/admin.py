from django.contrib import admin
from .models import Idea, Vote
# żeby przed atakami się chronić
from django.utils.html import  format_html

# to było słabe
# admin.site.register(Idea)
# admin.site.register(Vote)


# żeby na dole było widać głosy oddane do danej idei
class VoteInline(admin.StackedInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    # lupa na górze
    search_fields = ['title']
    list_display = ['title', 'status', 'show_youtube_url']
    # filtruje po statusie
    list_filter = ['status']
    # szuka idei na podstawie tytułu
    inlines = [
        VoteInline
    ]


    # self wskazuje na IdeaAdmin, obj wskazuje na konkretny wiersz
    # ta metoda po to żeby zwrócić klikalny link, a nie zwykły tekstowy link
    def show_youtube_url(self, obj):
        if obj.youtube_url is not None:
            return format_html(f'<a href="{obj.youtube_url}" target="_blank">{obj.youtube_url}</a>')
        else:
            return ''

    # zamiast SHOW YOUTUBE URL kolumna będzie się nazywać YOUTUBE URL
    show_youtube_url.short_description = 'Youtube URL'


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    # po prawej stronie jest filtr
    list_filter = ['idea']
