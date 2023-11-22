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
        <p class="text">작성일 : {{ article.created_at }}</p>
        <p class="text">수정일 : {{ article.updated_at }}</p>
        <button @click="updateArticle" class="btn btn-secondary text">수정하기</button>
        <button @click="deleteArticle" class="btn btn-secondary text">삭제하기</button>
        <button @click="goCommunity" class="btn btn-secondary text">돌아가기</button>
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

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.USER_API}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
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
</script>

<style>
.detail-content{
  position: absolute;
  left: 25%;
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