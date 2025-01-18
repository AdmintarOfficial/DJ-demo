import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponse
import json

def index(request):
    title = None
    price = None
    error = None  # to handle any error messages

    if request.method == 'POST':  # Ensure that we handle POST request
        search = request.POST.get('search', None)  # Safely get the search term

        if search:
            response = requests.get(search)

            if response.status_code != 200:
                error = "Failed to fetch the page."
            else:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Get price information
                price_element = soup.find(class_='font-price')
                if not price_element:
                    error = "Price not found."
                else:
                    price = price_element.get_text(strip=True)

                # Get title information
                title_element = soup.find('title')
                if title_element:
                    title = title_element.get_text(strip=True)
                else:
                    title = "No title found"

    response_data = {
        'title': title,
        'price': price,
        'error': error,  # Passing error to the template if any
    }

    return render(request, 'index.html', context=response_data)
