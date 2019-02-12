from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from . models import TODOModel
from django.urls import reverse
from django.shortcuts import redirect
from datetime import datetime
from . forms import TODOForm
from django.utils.html import strip_tags, escape


def assign_sort_list(request):

    sort_from_request = request.GET.get('sort', None)
    sort_list = request.session.get('sort_list',
                                    ['priority', 'due_date'])

    if not sort_from_request:
        return sort_list

    if sort_from_request in sort_list:
        sort_list.remove(sort_from_request)
    else:
        sort_list.append(sort_from_request)

    request.session['sort_list'] = sort_list

    return sort_list


@login_required
@csrf_protect
def get_index(request):

    sort_list = assign_sort_list(request)

    todo_list = TODOModel.objects.filter(owner=request.user)\
                                 .order_by(*sort_list)

    form = TODOForm()

    context = {
                'todo_list': todo_list,
                'date': datetime.now,
                'form': form,
                'sort_list': sort_list,
                }
    print("context.sort_list: {}".format(context['sort_list']))

    return render(request, "core/index.html", context)


def sanitizing_value(form, fieldname):
    return escape(strip_tags(form.cleaned_data[fieldname]))


@login_required
@csrf_protect
def add_task(request):
    if request.POST:

        form = TODOForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user
            todo.title = sanitizing_value(form, 'title')
            todo.description = sanitizing_value(form, 'description')

            todo.save()

    return redirect(reverse('index'))


@login_required
@csrf_protect
def remove_task(request):

    if request.POST:

        print("in remove task")

        task_id = request.POST.get("task_id")

        TODOModel.objects.filter(id=task_id).delete()

    return redirect(reverse('index'))
