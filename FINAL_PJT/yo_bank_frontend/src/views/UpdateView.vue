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
                <strong>게시글 수정하기</strong>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="article-form-container">
      <form @submit.prevent="ModifyPost" class="article-form detail-content">
        <div class="form-group">
          <label for="title">제목</label>
          <input type="text" v-model.trim="title" id="title" class="form-control">
        </div>
        <div class="form-group">
          <label for="content">내용</label>
          <textarea v-model.trim="content" id="content" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-secondary form-group">수정하기</button>
        <button @click="goBack" class="btn btn-secondary">돌아가기</button>
      </form>
    </div>
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
  <style scoped>
  .detail-content{
  width: 800px;
  position: absolute;
  left: 25%;
  top: 50%;
  }
  .form-group{
    margin: 10px;
  }
  
  </style>