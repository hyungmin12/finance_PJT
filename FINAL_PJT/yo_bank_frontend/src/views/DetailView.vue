<template>
  <div>
    <div class="carousel-container">
      <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner all_box ">
          <div class="carousel-item active">
            <img src="@/assets/images/bg.jpg">
            <div class="ani_box">
              <img src="@/assets/images/create.png" alt="" class="ani_img">
              <p class="slogan">
                <strong>게시글 수정/삭제</strong>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div v-if="article" class="detail-content" style="background-color: white; width: 60%;">
        <p class="text-title"><strong>제목 : {{ article.title }}</strong></p>
        <hr class="hr-line">
        <p class="text">내용 : {{ article.content }}</p>
        <p class="text">작성일 : {{ formatDateTime(article.created_at) }}</p>
        <p class="text">수정일 : {{ formatDateTime(article.updated_at) }}</p>

        <button v-if="article.user === userId" @click="updateArticle" class="btn btn-outline-secondary text">수정하기</button>
        <button v-if="article.user === userId" @click="deleteArticle" class="btn btn-outline-secondary text">삭제하기</button>
        <button @click="goCommunity" class="btn btn-outline-secondary text">돌아가기</button>
        <hr style="height: 1px; margin: 10px;">
        <div v-for="comment of comments" class="d-flex">
            <p class="text">댓글: {{ comment.content }}</p>
            <button v-if="comment.user === userId"  @click="deleteComment(comment.id, article.pk)" style="width: 96px; height: 35px; border-radius: 8px; margin: 10px;" class="btn btn-outline-secondary">댓글 삭제</button>
        </div>

        <form @submit.prevent="createComment">
          <input type="text" v-model="commentContent" style=" height: 35px; border-radius: 8px; margin: 10px;">
          <input type="submit" value="댓글 작성" style="width: 96px; height: 35px; border-radius: 8px; margin: 10px;" class="btn btn-outline-secondary">
        </form>

      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const comments = ref(null)
const commentContent = ref(null)

const userId = store.userInformations.id

const formatDateTime = function (dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0'); // 월은 0부터 시작하므로 1을 더합니다.
    const day = date.getDate().toString().padStart(2, '0');
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    
    return `${year}년 ${month}월${day}일 ${hours}시${minutes}분`;
}

// 
const createComment = function(){
  axios({
    method: 'POST',
    url: `${store.USER_API}/api/v1/comment_create/${route.params.id}/`,
    data : {
      content : commentContent.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    // 댓글이 성공적으로 생성되면 comments 배열에 새로운 댓글을 추가
    comments.value.push(res.data);
    // 댓글 입력 필드 초기화
    commentContent.value = null;
  })
  .catch((err) => {
    console.log(err);
  });
};

// 

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.USER_API}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data

        axios({
          method: 'get',
          url: `${store.USER_API}/api/v1/comments/${route.params.id}/list`
        })
        .then((res) => {
          // console.log(res.data)
          comments.value = res.data
        })
        .catch((err) => {
          console.log(err)
        })

    })
    .catch((err) => {
      console.log(err)
    })
})

const updateArticle = function() {
  router.push({ name: 'UpdateView', params: { id: route.params.id }})
}

const goCommunity = function(){
  router.push({ name: 'Community1View'})
}

const deleteArticle = function() {
  axios({
    method: 'DELETE',
    url: `${store.USER_API}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      store.getArticles()
      router.push({name:'Community1View'})
    })
    .catch((err) => {
      console.log(err)
      router.push({name:'Community1View'})
    })
}

const deleteComment = function(comment_pk, article_pk) {
  axios({
    method: 'DELETE',
    url: `${store.USER_API}/api/v1/comments/${comment_pk}/`,
  })
    .then((res) => {
      // 댓글 삭제 후 comments 배열에서 해당 댓글을 제거
      comments.value = comments.value.filter(comment => comment.id !== comment_pk);
      router.push({name:'DetailView', params : { id: article_pk }});
    })
    .catch((err) => {
      console.log(err);
    });
};

</script>

<style>
.detail-content{
  position: absolute;
  left: 20%;
  top: 50%;
  border: solid 1px black;
  border-radius: 8px;
}
.text{
  margin: 10px;
}
.text-title{
  font-size: 25px;
  margin: 10px;
}
.hr-line{
  background-color: black;
  height: 1px;
  margin-left: 8px;
  margin-right: 8px;
}
</style>