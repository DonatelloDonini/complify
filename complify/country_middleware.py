# country_middleware.py
#from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
from ipware.ip import get_client_ip

class CountryRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #esce non facendo i controlli
        #response = self.get_response(request)
        #return response
    
        #user_ip = get_client_ip(request)
        client_ip, is_routable = get_client_ip(request)
        if client_ip=='127.0.0.1':
             response = self.get_response(request)
             return response

    
        user_country = self.get_country_from_ip(client_ip)
        #user_country = self.get_country_from_ip(user_ip)
        if user_country not in settings.ALLOWED_COUNTRIES:
            # Se il paese dell'utente non è nella lista delle nazioni consentite
            # Esegui un'altra azione, ad esempio un reindirizzamento a una pagina di errore personalizzata
            return redirect(settings.COUNTRY_BLOCKED_RESPONSE)

        response = self.get_response(request)
        return response

    def get_country_from_ip(self, user_ip):


        from geoip2.database import Reader
        reader = Reader('GeoLite2-Country.mmdb')
        response = reader.country(user_ip)
        user_country = response.country.iso_code

        # Restituisci il codice del paese
        return user_country

        # Sostituisci questa parte con la logica reale per ottenere il paese dell'utente

        return None  # Torna None se non è possibile determinare il paese
