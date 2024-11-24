from django.views.generic import ListView  
from .filters import PostFilter  

class NewsListView(ListView):  
    model = Post  
    template_name = 'news_list.html'  
    context_object_name = 'news_list'  
    paginate_by = 10  

    def get_queryset(self):  
        queryset = Post.objects.filter(post_type=Post.NEWS)  
        self.filterset = PostFilter(self.request.GET, queryset=queryset)  
        return self.filterset.qs  

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        context['filterset'] = self.filterset  
        return context
    
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.models import Group  
from django.http import HttpResponseRedirect  
from django.urls import reverse  

@login_required  
def become_author(request):  
    author_group = Group.objects.get(name='authors')  
    request.user.groups.add(author_group)  
    return HttpResponseRedirect(reverse('profile_view'))  # Замените на реальный маршрут профиля