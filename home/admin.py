from django.contrib import admin
from .models import HeadTags, HomePage, Socials,AboutPage, ContactPage, PrivacyPolicyPage, TermsAndConditionsPage
# Register your models here.
admin.site.register(HeadTags)

class HomePageAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active']
    list_display_links = ['id', 'is_active']
    list_filter = ['is_active']
    search_fields = ['hero_heading', 'what_heading', 'how_heading', 'benefits_heading', 'special_heading']
    fieldsets = [
        ('General', {'fields': ['is_active', 'headtags']}),
        ('Hero Section', {'fields': ['hero_heading', 'hero_para']}),
        ('What is Section', {'fields': ['what_heading', 'what_para']}),
        ('How to Section', {'fields': ['how_heading', 'how_para', ('how_step_1', 'how_step_1_body'), ('how_step_2', 'how_step_2_body'), ('how_step_3', 'how_step_3_body'), ('how_step_4', 'how_step_4_body'), ('how_step_5', 'how_step_5_body'), ('how_step_6', 'how_step_6_body'), ('how_step_7', 'how_step_7_body'), 'how_to_closure']}),
        ('Benefits Section', {'fields': ['benefits_heading', ('benefits_1', 'benefits_1_body', 'benefits_1_svg'), ('benefits_2', 'benefits_2_body', 'benefits_2_svg'), ('benefits_3', 'benefits_3_body', 'benefits_3_svg'), ('benefits_4', 'benefits_4_body', 'benefits_4_svg')]}),
        ('Special Section', {'fields': ['special_heading', 'special_para', ('special_point_1', 'special_point_1_body'), ('special_point_2', 'special_point_2_body'), ('special_point_3', 'special_point_3_body'), ('special_point_4', 'special_point_4_body')]}),
        ('Home Page Ads', {'fields': [('home_ad_1'),('home_ad_2'),('home_ad_3'),('home_ad_4'),('home_ad_5'),('home_ad_6'),]}),
    ]

admin.site.register(HomePage, HomePageAdmin)

class SocialAdmin(admin.ModelAdmin):
    list_display = ['social_name', 'is_active']
    list_display_links = ['social_name', 'is_active']
    list_filter = ['is_active']

admin.site.register(Socials, SocialAdmin)

admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.register(PrivacyPolicyPage)
admin.site.register(TermsAndConditionsPage)
