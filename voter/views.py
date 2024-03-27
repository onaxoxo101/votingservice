from rest_framework import generics
from .serializers import VoterSerializer
from .models import Voter

# Create your views here.
class VoterListCreateView(generics.ListCreateAPIView):
     serializer_class = VoterSerializer
     queryset = Voter.objects.all()


     def get_queryset(self):
          queryset = Voter.objects.all()

          party = self.request.query_params.get('party', None)

          if party:
              queryset = queryset.filter(vote=party)

          return queryset


class SingleVoterView(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = VoterSerializer
     queryset =  Voter.objects.all()
