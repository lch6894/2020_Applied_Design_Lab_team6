from django.views import generic
from django.utils import timezone

from .models import Competition
from practice.models import Practice


class IndexView(generic.ListView):
    template_name = 'competitions/index.html'
    context_object_name = 'latest_competitions_list'

    def get_queryset(self):
        return Competition.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['practices'] = Practice.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Competition
    template_name = 'competitions/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Competition.objects.filter(pub_date__lte=timezone.now())

class AttendView(generic.DetailView):
    model = Competition
    template_name = 'competitions/attend.html'

