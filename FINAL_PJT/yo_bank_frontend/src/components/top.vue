<template>
  <div class="head">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="d-flex justify-content-between w-100">
    <div>
      <RouterLink to="/" class="me-auto p-2 bd-highlight">VO-BANK</RouterLink>
    </div>
    <div>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 ma-2 pa-2">
          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/depositandsaving" class="navvar m-5">예적금</RouterLink>
          </li>
          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/community1" class="navvar m-5">금융게시판</RouterLink>
          </li>
          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/exchange" class="navvar m-5">환율계산기</RouterLink>
          </li>
          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/kakaomap" class="navvar m-5">은행찾기</RouterLink>
          </li>
          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/userprofile" class="navvar m-5">마이페이지</RouterLink>
          </li>
          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/recommend" class="navvar m-5">예적금추천</RouterLink>
          </li>
          <form v-if="store.isLogin" @submit.prevent="store.logOut">
            <input type="submit" value="로그아웃" style="background-color: #f8f9fa; border:none">
          </form>

          <li v-if="!store.isLogin" class="nav-item">
            <RouterLink to="/signup" class="navvar m-5">회원가입</RouterLink>
          </li>
        </ul>
      </div>
  </div>
    </nav>
  </div>
  <RouterView/>
</template>

<script setup>

import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'


const store = useCounterStore()

</script>

<style scoped>
  a{
    text-decoration: none;
    color: black;
  }
  .navvar{
    margin-left: 30px;
  }
</style>