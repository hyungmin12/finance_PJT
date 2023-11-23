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
  <div class="form-group">
    <label for="title" class="form-label">제목</label>
    <input type="text" v-model.trim="title" placeholder="제목을 입력해주세요." class="form-input" id="title">
  </div>
  <div class="form-group">
    <label for="content" class="form-label">내용</label>
    <textarea v-model.trim="content" placeholder="함께 나누고 싶은 얘기를 남겨주세요." id="content" class="form-textarea"></textarea>
  </div>
  <button type="submit" class="form-button">글쓰기 완료!</button>
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
  top: 90%; /* Adjust as needed */
  left: 50%; /* Adjust as needed */
  transform: translate(-50%, -50%);
  z-index: 2;
  width: 1300px;
}

.carousel-container {
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
  margin-left: 30px;
  line-height: 1.4;
  margin-top: 130px;
}

  /* Add these styles to your existing styles or in a separate style block */

  .form-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #fff;
  }

  .form-group {
    margin-bottom: 20px;
  }

  .form-label {
    display: block;
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 5px;
  }

  .form-input,
  .form-textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-sizing: border-box;
  }

  .form-textarea {
    resize: vertical;
  }

  .form-button {
    background-color: #4caf50;
    color: #fff;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .form-button:hover {
    background-color: #45a049;
  }

</style>
