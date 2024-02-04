from django.db import models

title_name = 'Title tag'
description_name = 'Meta description'
robots_tag_name = 'Robots tag (index, follow)'
og_site_name_name = 'og:site_name'
og_title_name = 'og:title'
og_description_name = 'og:description'
og_image_url_name = 'URL for the og:image'
headtags_name = 'HTML Head tags (Google Analytics, Tag managers, others.)'
# Create your models here.

class HeadTags(models.Model):
    is_active = models.BooleanField(verbose_name='Display these tags.', default=True)
    title = models.CharField(verbose_name=title_name, max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name=description_name, null=False, blank=False)
    robots_tag= models.CharField(verbose_name=robots_tag_name, max_length=200, null=False, blank=False, default='index, follow')
    site_name = models.CharField(verbose_name=og_site_name_name, max_length=200, null=False, blank=False)
    og_title = models.CharField(verbose_name=og_title_name, max_length=200, null=False, blank=False)
    og_description = models.TextField(verbose_name=og_description_name, null=False, blank=False)
    og_image_url = models.URLField(verbose_name=og_image_url_name, null=False, blank=False)
    headtags = models.TextField(verbose_name=headtags_name, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"

class HomePage(models.Model):
    is_active = models.BooleanField(verbose_name='Use this Home content', default=True)
    headtags = models.ForeignKey(to=HeadTags, verbose_name='Headtags for Home Page', on_delete=models.SET_NULL, null=True, blank=True)
    
    hero_heading = models.CharField(verbose_name='Hero Heading', max_length=500, null=True, blank=True)
    hero_para = models.TextField(verbose_name='Hero Body', null=True, blank=True)

    home_ad_1 = models.TextField(verbose_name='Home Ad Code', null=True, blank=True)
    home_ad_2 = models.TextField(verbose_name='Home Ad Code', null=True, blank=True)

    what_heading = models.CharField(verbose_name='"What is section" Heading', max_length=500, null=True, blank=True)
    what_para = models.TextField(verbose_name='"What is section" Body', null=True, blank=True)

    home_ad_3 = models.TextField(verbose_name='Home Ad Code', null=True, blank=True)

    how_heading = models.CharField(verbose_name='"How to section" Heading', max_length=500, null=True, blank=True)
    how_para = models.TextField(verbose_name='"How to section" Body', null=True, blank=True)
    how_step_1 = models.CharField(verbose_name='How to Step 1', max_length=500, null=True, blank=True)
    how_step_1_body = models.TextField(verbose_name='How to Step 1 Body', null=True, blank=True)
    how_step_2 = models.CharField(verbose_name='How to Step 2', max_length=500, null=True, blank=True)
    how_step_2_body = models.TextField(verbose_name='How to Step 2 Body', null=True, blank=True)
    how_step_3 = models.CharField(verbose_name='How to Step 3', max_length=500, null=True, blank=True)
    how_step_3_body = models.TextField(verbose_name='How to Step 3 Body', null=True, blank=True)
    how_step_4 = models.CharField(verbose_name='How to Step 4', max_length=500, null=True, blank=True)
    how_step_4_body = models.TextField(verbose_name='How to Step 4 Body', null=True, blank=True)
    how_step_5 = models.CharField(verbose_name='How to Step 5', max_length=500, null=True, blank=True)
    how_step_5_body = models.TextField(verbose_name='How to Step 5 Body', null=True, blank=True)
    how_step_6 = models.CharField(verbose_name='How to Step 6', max_length=500, null=True, blank=True)
    how_step_6_body = models.TextField(verbose_name='How to Step 6 Body', null=True, blank=True)
    how_step_7 = models.CharField(verbose_name='How to Step 7', max_length=500, null=True, blank=True)
    how_step_7_body = models.TextField(verbose_name='How to Step 7 Body', null=True, blank=True)
    how_to_closure = models.TextField(verbose_name='How to Closure Body', null=True, blank=True)

    home_ad_4 = models.TextField(verbose_name='Home Ad Code', null=True, blank=True)

    benefits_heading = models.CharField(verbose_name='"Benefits section" Heading', max_length=500, null=True, blank=True)
    benefits_1 = models.CharField(verbose_name='Benefits 1', max_length=500, null=True, blank=True)
    benefits_1_body = models.TextField(verbose_name='Benefits 1 Body', null=True, blank=True)
    benefits_1_svg = models.TextField(verbose_name='Benefits 1 SVG Code', null=True, blank=True)
    benefits_2 = models.CharField(verbose_name='Benefits 2', max_length=500, null=True, blank=True)
    benefits_2_body = models.TextField(verbose_name='Benefits 2 Body', null=True, blank=True)
    benefits_2_svg = models.TextField(verbose_name='Benefits 2 SVG Code', null=True, blank=True)
    benefits_3 = models.CharField(verbose_name='Benefits 3', max_length=500, null=True, blank=True)
    benefits_3_body = models.TextField(verbose_name='Benefits 3 Body', null=True, blank=True)
    benefits_3_svg = models.TextField(verbose_name='Benefits 3 SVG Code', null=True, blank=True)
    benefits_4 = models.CharField(verbose_name='Benefits 4', max_length=500, null=True, blank=True)
    benefits_4_body = models.TextField(verbose_name='Benefits 4 Body', null=True, blank=True)
    benefits_4_svg = models.TextField(verbose_name='Benefits 4 SVG Code', null=True, blank=True)

    home_ad_5 = models.TextField(verbose_name='Home Ad Code', null=True, blank=True)

    special_heading = models.CharField(verbose_name='"Special  section" Heading', max_length=500, null=True, blank=True)
    special_para = models.TextField(verbose_name='"Special  section" Body', null=True, blank=True)
    special_point_1 = models.CharField(verbose_name='Special  Point 1', max_length=500, null=True, blank=True)
    special_point_1_body = models.TextField(verbose_name='Special  Point 1 Body', null=True, blank=True)
    special_point_2 = models.CharField(verbose_name='Special  Point 2', max_length=500, null=True, blank=True)
    special_point_2_body = models.TextField(verbose_name='Special  Point 2 Body', null=True, blank=True)
    special_point_3 = models.CharField(verbose_name='Special  Point 3', max_length=500, null=True, blank=True)
    special_point_3_body = models.TextField(verbose_name='Special  Point 3 Body', null=True, blank=True)
    special_point_4 = models.CharField(verbose_name='Special  Point 4', max_length=500, null=True, blank=True)
    special_point_4_body = models.TextField(verbose_name='Special  Point 4 Body', null=True, blank=True)
    
    home_ad_6 = models.TextField(verbose_name='Home Ad Code', null=True, blank=True)

    class Meta:
        verbose_name='Home Page Content'
        verbose_name_plural='Home Page Contents'


class AboutPage(models.Model):
    is_active = models.BooleanField(verbose_name='Show this content', default=True)
    headtags = models.ForeignKey(to=HeadTags, verbose_name='Headtags for About Page', on_delete=models.SET_NULL, null=True, blank=True)
    html_content = models.TextField(null=False, blank=False)
    class Meta:
        verbose_name='About Page Content'
        verbose_name_plural='About Page Contents'

class ContactPage(models.Model):
    is_active = models.BooleanField(verbose_name='Show this content', default=True)
    headtags = models.ForeignKey(to=HeadTags, verbose_name='Headtags for Contact Page', on_delete=models.SET_NULL, null=True, blank=True)
    html_content = models.TextField(null=False, blank=False)
    class Meta:
        verbose_name='Contact Page Content'
        verbose_name_plural='Contact Page Contents'

class TermsAndConditionsPage(models.Model):
    is_active = models.BooleanField(verbose_name='Show this content', default=True)
    headtags = models.ForeignKey(to=HeadTags, verbose_name='Headtags for Terms & Conditions Page', on_delete=models.SET_NULL, null=True, blank=True)
    html_content = models.TextField(null=False, blank=False)
    class Meta:
        verbose_name='Terms & Conditions  Page Content'
        verbose_name_plural='Terms & Conditions  Page Contents'

class PrivacyPolicyPage(models.Model):
    is_active = models.BooleanField(verbose_name='Show this content', default=True)
    headtags = models.ForeignKey(to=HeadTags, verbose_name='Headtags for Privacy Policy Page', on_delete=models.SET_NULL, null=True, blank=True)
    html_content = models.TextField(null=False, blank=False)
    class Meta:
        verbose_name='Privacy Policy Page Content'
        verbose_name_plural='Privacy Policy Page Contents'

class Socials(models.Model):
    is_active = models.BooleanField(verbose_name='Show this social', default=True)
    social_svg = models.TextField(verbose_name='Social SVG Code', null=False, blank=False)
    social_link = models.URLField(verbose_name='Link', null=False, blank=False)
    social_name = models.CharField(max_length=100 ,verbose_name='Social Name', null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.social_name}"

