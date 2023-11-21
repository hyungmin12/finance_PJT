<template>
  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner all_box ">
      <div class="carousel-item active">
        <img src="src/assets/images/bg.jpg">
        <div class="ani_box">
          <img src="src/assets/images/login.png" alt="" style="width: 355px;position: absolute; top: 0; right: 0;">
          <p class="slogan">
            <strong>로그인</strong>
          </p>
        </div>
      </div>
    </div>
  </div>
  <div class="login_form">
    <table class="table">
      <thead>
        <tr class="th">
          <th scope="col" style="background-color: rgb(235, 233, 233);">아이디</th>
          <th scope="col" >
            <form @submit.prevent="logIn">
              <input type="text" v-model.trim="username" class="login-text">
            </form>
          </th>
        </tr>
        <tr>
          <th scope="col" style="background-color: rgb(235, 233, 233);">비밀번호</th>
          <th scope="col">
            <form @submit.prevent="logIn">
              <input type="password" v-model.trim="password" class="login-text">
            </form>
          </th>
        </tr>
        <input type="submit" value="로그인" class="submit">
      </thead>
    </table>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
const payload = {
  username: username.value,
  password: password.value
}
store.logIn(payload)
}
</script>

<style>
.table {
  border-collapse: collapse;
  width: 100%;
}

.table th, .table td {
  border: 1px solid #ddd; /* Add a border to all cells */
  padding: 8px;
  text-align: left;
}

.table th {
  background-color: rgb(235, 233, 233);
}

.th {
  border-top: 2px solid blue; /* Set the top border of the first column to blue */
}
hr{
background-color: blue;
height: 5px;
}
.background{
background-color: rgb(201, 199, 199);
}
.login_form{
width: 70%;
margin: 0 auto;
}
.submit{
background-color: rgb(229, 252, 252);
width: 100px;
border-radius: 5px;
margin-top: 20px;

}
.all_box {
height: 350px;
margin-top: 50px;
}

.ani_box {
width: 1000px;
margin: 0 auto;
position: relative; /* 부모 요소에 대해 상대적 위치 설정 */
}

.login_img {
margin-top: 31px;
position: absolute;
top: 0;
right: 0;
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
body {
    font-family: Arial, sans-serif;
  }
  table {
    margin-top: 40px;
    width: 35%;
    border-collapse: collapse;
  }
  th, td {
    padding: 10px;
    text-align: left;
    border: 1px solid #ddd; /* Add border style */
  }
  .login-text {
    width: 40%;
    padding: 8px;
    box-sizing: border-box;
  }
  .submit {
    background-color: #7f807e;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }
  .submit:hover {
    background-color: #7f807e;
  }
</style>