from django.shortcuts import render
from django.http import JsonResponse
from rembg import remove
from .models import HomePage, AboutPage, ContactPage, PrivacyPolicyPage, TermsAndConditionsPage, Socials
import base64

def query_headtags(headtag_i):
    return {
                "title": headtag_i.title,
                "description": headtag_i.description,
                "robots_tag": headtag_i.robots_tag, 
                "og_site_name": headtag_i.site_name, 
                "og_title": headtag_i.og_title, 
                "og_description": headtag_i.og_description, 
                "og_image_url": headtag_i.og_image_url, 
                "headtags": headtag_i.headtags
        }

def render_page(request, PageModel, template_name):
    context = {
        'socials': Socials.objects.filter(is_active=True)
    }

    page_instance = PageModel.objects.filter(is_active=True).first()
    if page_instance and page_instance.headtags: 
        headtags = query_headtags(headtag_i=page_instance.headtags)
        
        context['headtags'] = headtags
        context['home'] = page_instance

    return render(request, template_name, context)


def home(request):
    return render_page(request, HomePage, 'index.html')
    

def about(request):
    return render_page(request, AboutPage, 'page.html')
def contact(request):
    return render_page(request, ContactPage, 'page.html')
def privaypolicy(request):
    return render_page(request, PrivacyPolicyPage, 'page.html')
def termsandconditions(request):
    return render_page(request, TermsAndConditionsPage, 'page.html')
   

def remover(request):
    if request.method == 'POST' and request.FILES.get('input_image'):
        print(request.FILES)
        uploaded_file = request.FILES['input_image']
        file_content = uploaded_file.read()
        try:
                processed_image_content = remove(file_content, alpha_matting=True)
                file_content_base64 = base64.b64encode(processed_image_content).decode('utf-8')
                response_data = {
                    'file_name': uploaded_file.name,
                    'file_size': uploaded_file.size,
                    'file_content': file_content_base64 # Read the file content
                }
                return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': "It's not you it's us."}, status=400)
    return JsonResponse({'error': 'Please upload a file using a POST request.'}, status=400)

