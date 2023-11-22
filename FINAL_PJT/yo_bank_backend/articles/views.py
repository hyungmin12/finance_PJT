from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer,CommentSerializer
from .models import Article,Comment



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    user = request.user
    print(user.money_for_financial)
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        if 0<=user.money_for_financial<=500000:
            articles = Article.objects.filter(money_for_financial__range=(0, 500000))
        elif 500001<=user.money_for_financial<=1000000:
            articles = Article.objects.filter(money_for_financial__range=(500001, 1000000))
        elif 1000001<=user.money_for_financial<=1500000:
            articles = Article.objects.filter(money_for_financial__range=(1000001, 1500000))
        elif 1500001 <= user.money_for_financial <= 2000000:
            articles = Article.objects.filter(money_for_financial__range=(1500001, 2000000))
        elif 2000001 <= user.money_for_financial <= 2500000:
            articles = Article.objects.filter(money_for_financial__range=(2000001, 2500000))
        elif 2500001 <= user.money_for_financial <= 3000000:
            articles = Article.objects.filter(money_for_financial__range=(2500001, 3000000))
        elif 3000001 <= user.money_for_financial:
            articles = Article.objects.filter(money_for_financial__range=(3000001, 9999999999))

        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        request.data['money_for_financial']=request.user.money_for_financial
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, id=article_pk)
    # 해당 게시물의 댓글 목록 가져오기
    comments = article.comment_set.all()
    # 댓글 목록을 직렬화
    serializer = CommentSerializer(comments, many=True)
    # 반환
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','DELETE','PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    print("===================")
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article,user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)