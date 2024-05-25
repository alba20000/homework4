from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core import models, filters, serializers


class Staff(ListView):
    template_name = 'core/index.html'
    model = models.Staff
    context_object_name = 'staff'

    def get_filters(self):
        return filters.Staff(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['filter'] = self.get_filters()
        return context


class StaffAPI(APIView):
    def get(self, request):
        qs = models.Staff.objects.all()
        serializer = serializers.Staff(qs, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.Staff(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'OK'})


class StaffModel(ModelViewSet):
    queryset = models.Staff.objects.all()
    filterset_class = filters.Staff
    serializer_class = serializers.Staff
