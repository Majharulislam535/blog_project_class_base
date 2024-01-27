from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .import forms
from .import models

from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

# @login_required(login_url='/login/')
# def add_post(request):
#     if request.method =='POST':
#        form =forms.Add_Post(request.POST)
       
#        if form.is_valid():
#             form.instance.author=request.user
#             form.save()
#             return redirect('home')
#     else:
#         form =forms.Add_Post()
#     return render(request,'add_post.html',{'form':form})

#class base --- add post
@method_decorator(login_required,name='dispatch')
class AddPost_view(CreateView):
     model= models.Post
     form_class=forms.Add_Post
     template_name= 'add_post.html'
     success_url = reverse_lazy('home')
     def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#class 

# @login_required
# def edit_post(request,id):
#     post = models.Post.objects.get(pk=id)
#     form =forms.Add_Post(instance=post)
#     if request.method =='POST':
#        form =forms.Add_Post(request.POST,instance=post)
       
#        if form.is_valid():
#             form.save()
#             return redirect('home')
    
#     return render(request,'add_post.html',{'form':form})


# class base edit post 
@method_decorator(login_required,name='dispatch')
class Edit_Post_View(UpdateView):
        model=models.Post
        form_class=forms.Add_Post
        template_name='add_post.html'
        pk_url_kwarg='id'
        success_url=reverse_lazy('home')




# @login_required(login_url='/login/')
# def delete_post(request,id):
#     post = models.Post.objects.get(pk=id)
#     post.delete()
#     return redirect('home')


#class delete view
@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name='delete.html'
    success_url=reverse_lazy('home')
    pk_url_kwarg='id'


class DetailsView(DetailView):
        model=models.Post
        pk_url_kwarg='id'
        template_name='post_details.html'

        def post(self,request,*args,**kwargs):
                        comment_form = forms.CommentForm(data=self.request.POST)
                        post=self.get_object()
                        if comment_form.is_valid():
                                new_comment = comment_form.save(commit=False)
                                new_comment.post = post
                                new_comment.save()
                        return self.get(request,*args,**kwargs)

        def get_context_data(self,**kwargs):
                context = super().get_context_data(**kwargs)
                post = self.object
                comments = post.comments.all()
                comment_form=forms.CommentForm()

                context['comments'] = comments
                context['comment_form']=comment_form
                return context