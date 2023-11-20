<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
      <button @click="updateArticle">수정하기</button>
      <button @click="deleteArticle">삭제하기</button>
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

const deleteArticle = function() {
  axios({
    method: 'DELETE',
    url: `${store.USER_API}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      store.getArticles()
      router.push({name:'ArticleView'})
    })
    .catch((err) => {
      console.log(err)
      router.push({name:'ArticleView'})
    })
}

</script>

<style>

</style>
