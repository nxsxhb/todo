from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . models import Todo
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.

class TodoListView(ListView):
    model=Todo
    template_name='home.html'
    context_object_name = 'task1'

class TodoDeleteView(DeleteView):
    model=Todo
    template_name='delete.html'
    success_url = reverse_lazy('cbvhome')

class TodoDetailView(DetailView):
    model=Todo
    template_name='details.html'
    context_object_name = 'task'

class TodoUpdateView(UpdateView):
    model=Todo
    template_name='edit.html'
    context_object_name = 'task'
    fields=('taskname','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

def home(request):
    task1=Todo.objects.all()    
    if request.method=="POST":
        taskname=request.POST.get('taskname', '')
        priority=request.POST.get('priority', '')
        date=request.POST.get('date','')
        task=Todo(taskname=taskname,priority=priority,date=date)
        task.save()
    
    return render(request, 'home.html', {'task1':task1})

def delete(request,id):
    task1=Todo.objects.get(id=id)
    if request.method=="POST":
        task1.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request,id):
    task=Todo.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "update.html", {'task':task,'form':form})
        