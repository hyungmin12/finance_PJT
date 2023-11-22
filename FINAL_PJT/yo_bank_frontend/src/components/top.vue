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
            <RouterLink to="/depositList" class="navvar m-5">예금</RouterLink>
          </li>
          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/savingList" class="navvar m-5">적금</RouterLink>
          </li>
          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/community1" class="navvar m-5">커뮤니티1</RouterLink>
          </li>
          <!-- <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/community2" class="navvar m-5">커뮤니티2</RouterLink>
          </li> -->

          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/userprofile" class="navvar m-5">마이페이지</RouterLink>
          </li>
          <li v-if="store.isLogin" class="nav-item">
            <RouterLink to="/recommend" class="navvar m-5">추천페이지</RouterLink>
          </li>


          <form v-if="store.isLogin" @submit.prevent="store.logOut">
            <input type="submit" value="logOut">
          </form>

          <li v-if="!store.isLogin" class="nav-item">
            <RouterLink to="/login" class="navvar m-5">로그인</RouterLink>
          </li>
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