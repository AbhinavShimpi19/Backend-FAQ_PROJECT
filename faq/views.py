# faq/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ

def home(request):
    """
    A simple view for the home page.
    You can replace this with your own HTML template or logic.
    """
    return render(request, 'home.html')

class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')

        # Define a unique cache key based on the language
        cache_key = f'faqs_{lang}'

        # Try to fetch the data from the cache
        data = cache.get(cache_key)

        if not data:
            faqs = FAQ.objects.all()
            data = [
                {
                    'id': faq.id,
                    'question': faq.get_translated_question(lang),
                    'answer': faq.get_translated_answer(lang),
                }
                for faq in faqs
            ]
            cache.set(cache_key, data, timeout=3600)

        return Response(data)
