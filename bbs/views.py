from django.shortcuts import render, redirect

from django.views import View
from .models import Category, Topic, Reply
from .forms import TopicForm, ReplyForm

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


class ReplyView(View):
    def get(self, request, pk, *args, **kwargs):

        context = []
        context["topic"] = Topic.objects.filter(id=pk).first()
        context["replies"] = Reply.objects.filter(target=pk)

        return render(request, "bbs/reply.html", context)

    def post(self, request, pk, *args, **kwargs):
        
        #request.POSTのコピーオブジェクトを作る。(そのままでは書き換えはできないため)
        copied = request.POST.copy()
        copied["target"] = pk

        form = ReplyForm(copied)

        if form.is_valid():
            form.save()
        else:
             print("バリデーションNG")
        
        return redirect("bbs:reply", pk)

reply = ReplyView.as_view()


