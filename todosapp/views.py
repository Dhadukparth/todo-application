from django.shortcuts import render, redirect, HttpResponse
from .models import todos
from django.contrib import messages
import json

# Create your views here.

def home(request):
    fetch_all_data = todos.objects.all()
    return render(request, "index.html", context={'records': fetch_all_data})


def newTodo(request):
    if request.method == "POST":
        todo_name = request.POST['todoName']
        todo_description = request.POST['todoDescription']

        new_todo = todos.objects.create(name = todo_name, description = todo_description)
        new_todo.save()

        messages.success(request, "Save SuccessFully")
        return redirect('/')
        
    else:
        return redirect('/')

def editTodo(request):
    if request.method == 'POST':
        edit_todo_id = request.POST['edit_todo_id']
        edit_todo_name = request.POST['edit_todo_name']
        edit_todo_description = request.POST['edit_todo_description']

        edit_fetch_record = todos.objects.get(id = edit_todo_id)
        edit_fetch_record.name = edit_todo_name
        edit_fetch_record.description = edit_todo_description
        edit_fetch_record.save()

        messages.success(request, "Todo Is Update SuccessFully.")

        return redirect('/')
    else:
        get_todo_id = request.GET.get('todo_id')
        fetch_record = todos.objects.get(id = get_todo_id)

        editData = json.dumps({
            'todo_id' : fetch_record.id,
            'todo_name' : fetch_record.name,
            'todo_description' : fetch_record.description,
        })

        return HttpResponse(editData, content_type="application/json")


def removeTodo(request, id):
    remove_fetch_todo = todos.objects.get(id=id)
    # remove_fetch_todo.delete()

    messages.success(request, "Todo Is Delete SuccessFully.")

    return redirect('/')