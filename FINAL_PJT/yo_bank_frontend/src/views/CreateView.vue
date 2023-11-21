<template>
  <div class="container">
    <div class="carousel-container">
      <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner all_box ">
          <div class="carousel-item active">
            <img src="src/assets/images/bg.jpg">
            <div class="ani_box">
              <img src="src/assets/images/create.png" alt="" class="ani_img">
              <p class="slogan">
                <strong>게시글 작성</strong>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <form @submit.prevent="createArticle" class="form-container">
      <div>
        <input type="text" v-model.trim="title" placeholder="제목을 입력해주세요." class="title" id="title">
      </div>
      <div>
        <textarea v-model.trim="content" placeholder="함께 나누고 싶은 얘기를 남겨주세요." id="content" class="content"></textarea>
      </div>
      <input type="submit" value="글쓰기 완료!" class="write">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.USER_API}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'Community1View' })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style>
.container {
  position: relative;
}

.form-container {
  position: absolute;
  top: 110%; /* Adjust as needed */
  left: 50%; /* Adjust as needed */
  transform: translate(-50%, -50%);
  z-index: 2;
}

.carousel-container {
  position: relative;
}

.all_box {
  height: 350px;
  margin-top: 50px;
}

.ani_box {
  width: 1000px;
  margin: 0 auto;
  position: relative;
}

.ani_img {
  margin-top: 31px;
  position: absolute;
  top: 0;
  right: 0;
  width: 400px;
  height: 200px;
}

.slogan {
  margin-bottom: 50px;
  line-height: 1.4;
  margin-top: 130px;
}

.ani_box .slogan {
  display: inline-block;
  font-size: 30px;
  font-weight: 300;
}

.carousel-inner img {
  position: absolute;
  top: 0;
  z-index: -1;
  height: auto;
}

.text-create {
  text-decoration-line: none;
}
.title{
  width: 500px;
  margin-bottom: 20px;
  border-radius: 15px;
}
.content{
  width: 500px;
  height: 450px;
  border-radius: 15px;
}
.write{
  position: absolute;
  margin-top: 20px;
  left: 80%;
  color: gray;
}
</style>
