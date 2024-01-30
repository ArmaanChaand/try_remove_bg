from django.shortcuts import render
from django.http import HttpResponse
# from rembg import remove
def home(request):
    # try:
    #     if request.method == 'POST':
    #         input_image = request.FILES.get('input_image')
    #         uploaded_image = input_image
    #         image_content = uploaded_image.read()            
    #         try:
    #             processed_image_content = remove(image_content)
    #             response = HttpResponse(processed_image_content, content_type='image/png')
    #             response['Content-Disposition'] = 'attachment; filename="processed_image.png"'
    #             return response
    #         except Exception as e:
    #             return HttpResponse("Error processing image: {}".format(e), status=500)
    # except Exception as e:
    #     print(e)
    #     return HttpResponse('Some error ocurred.')
    
    return render(request, 'index.html', {})