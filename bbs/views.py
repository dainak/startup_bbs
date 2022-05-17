from django.shortcuts import render, redirect

from django.views import View
from .models import Category, Topic
from .forms import TopicForm

class IndexView(View):
    def get(self, request, *args, **kwargs):

        context = {}
        context["topics"] = Topic.objects.all()

        #カテゴリの選択肢を作るため、全てのカテゴリをcontextに引き渡す
        context["categories"] = Category.objects.all()

        return render(request, "bbs/index.html", context)

    def post(self, request, *args, **kwargs):

        form = TopicForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print("バリデーションNG")

        # posted = Topic( comment = request.POST["comment"])
        # posted.save()

        return redirect("bbs:index")

index = IndexView.as_view()