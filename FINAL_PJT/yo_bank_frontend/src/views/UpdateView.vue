<template>
    <div class="article-form-container">
      <h1>게시글 수정하기</h1>
      <form @submit.prevent="ModifyPost" class="article-form">
        <div class="form-group">
          <label for="title">제목</label>
          <input type="text" v-model.trim="title" id="title" class="form-control">
        </div>
        <div class="form-group">
          <label for="content">내용</label>
          <textarea v-model.trim="content" id="content" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">수정하기</button>
      </form>
      <button @click="goBack" class="btn btn-secondary">돌아가기</button>
    </div>
  </template>
  
  
  <script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'
    import { useCounterStore } from '@/stores/counter'
    import { useRouter, useRoute } from 'vue-router'
  
    const store = useCounterStore()
    const router = useRouter()
    
    const title = ref('');
    const content = ref('');
    const articleId = ref('');
    const route = useRoute()
    
    onMounted(() => {
      console.log(route.params.id)
      title.value = route.query.title
      content.value = route.query.content
      articleId.value = route.params.id;
    })
  
    const ModifyPost = function () {
      axios({
        method: 'put',
        url: `${store.USER_API}/api/v1/articles/${articleId.value}/`,
        data: {
          title: title.value,
          content: content.value
        },
      })
        .then((res) => {
          router.push({ name: 'DetailView', params: {id:articleId.value}})
        })
        .catch((err) => {
          console.log(err)
        })
    }
  
    const goBack = function(){
      router.go(-1)
    }
  </script>