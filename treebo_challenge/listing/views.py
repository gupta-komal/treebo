from django.db.models import Q, Avg, Max, Min
from django.views.generic import TemplateView
from listing.models import Hotel_Deals


class StatPage(TemplateView):
    def get(self, request, *args, **kwargs):
        self.template_name = 'stats.html'
        price = {}
        area_wise_hotel_distribution = {}
        data = {}
        average_rating = round(Hotel_Deals.objects.all().aggregate(Avg('rating'))['rating__avg'],2)
        price['Minimum'] = Hotel_Deals.objects.all().aggregate(Min('actual_price'))['actual_price__min']
        price['Maximum'] = Hotel_Deals.objects.all().aggregate(Max('actual_price'))['actual_price__max']
        blr_hotels = Hotel_Deals.objects.filter(location__icontains='bengaluru').count()
        che_hotels = Hotel_Deals.objects.filter(location__icontains='chennai').count()
        hyd_hotels = Hotel_Deals.objects.filter(location__icontains='hyderabad').count()
        mum_hotels = Hotel_Deals.objects.filter(location__icontains='mumbai').count()
        del_hotels = Hotel_Deals.objects.filter(location__icontains='delhi').count()
        area_wise_hotel_distribution['BLR'] = blr_hotels
        area_wise_hotel_distribution['CHE'] = che_hotels
        area_wise_hotel_distribution['HYD'] = hyd_hotels
        area_wise_hotel_distribution['MUM'] = mum_hotels
        area_wise_hotel_distribution['DEL'] = del_hotels
        data['average'] = average_rating
        data['price'] = price
        data['area_wise_hotel_distribution'] = area_wise_hotel_distribution
        return self.render_to_response({'data': data})


class ListView(TemplateView):
    def get(self, request, *args, **kwargs):
        search_keyword = request.GET.get('search', None)
        sort_by = request.GET.get('sort_by', None)
        self.template_name = 'hotel_list.html'
        queryset = Hotel_Deals.objects.all()
        if search_keyword:
            queryset = queryset.filter(Q(location__icontains=search_keyword) | Q(name__icontains=search_keyword))
        if sort_by and sort_by == 'rating':
            queryset = queryset.order_by('-rating')
        if sort_by and sort_by == 'pricing':
            queryset = queryset.order_by('actual_price')
        return self.render_to_response({'hotel_deals': queryset})

