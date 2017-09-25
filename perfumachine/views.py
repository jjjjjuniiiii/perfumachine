from django.shortcuts import render
from models import Item

# Create your views here.
@login_required
def item_like(request, pk):
  item = get_object_or_404(Item, pk=pk)
  # 중간자 모델 Like 를 사용하여, 현재 item와 request.user에 해당하는 Like 인스턴스를 가져온다.
  item_like, item_like_created = item.like_set.get_or_create(user=request.user)

  if not item_like_created:
    item_like.delete()

    return redirect('item:item_list')