<template>
    <header>
      <h1 style="text-align: center; margin-top: 40px; margin-bottom: 40px;">마이 페이지</h1>
    </header>
    <div class="container">
      <div class="row">
        <div class="col-4">
          <div class="profile borderclass py-3 px-3"
            style="margin-top: 30px; border: 1px solid black; text-align: center; border-radius: 8px;">
            <img class="profile-img" src="@/assets/images/mypage.png" alt="">
            <h2 style=" margin: 10px;">기본정보</h2>
            <hr style="height: 1px; margin: 10px;">
            <p class="text_font" style=" margin: 10px; text-align: center; font-size: 25px;"><strong>{{ userInfo.username }}</strong></p>
          <p class="text_font" style=" margin: 10px; padding-left: 120px; text-align: left;">닉네임: {{ userInfo.nickname }}</p>
          <p class="text_font" style=" margin: 10px; padding-left: 120px; text-align: left;">나이: {{ userInfo.age }}</p>
          <p class="text_font" style=" margin: 10px; padding-left: 120px; text-align: left;">이메일: {{ userInfo.email }}</p>
          <p class="text_font" style=" margin: 10px; padding-left: 120px; text-align: left;">사용금액: {{ userInfo.used_money_for_financial }}원</p>
          <p class="text_font" style=" margin: 10px; padding-left: 120px; text-align: left;">남은금액: {{ userInfo.left_money_for_financial }}원</p>
          <p class="text_font" style=" margin: 10px; padding-left: 120px; text-align: left;">급여: {{ userInfo.salary }}원</p>
          <p class="text_font" style=" margin: 10px; padding-left: 120px; text-align: left;">가용투자비용: {{ userInfo.money_for_financial }}</p>
          <p class="text_font" style=" margin: 10px; padding-left: 120px; text-align: left;">평균 급여: {{ userInfo.salary }}</p>
            <li class="nav-item" style="list-style-type: none; margin-bottom: 10px;">
              <RouterLink :to="{ name: 'UpdateUserView' }" class="btn btn-outline-secondary">회원정보수정</RouterLink>
            </li>
  
          </div>
        </div>
        <div class="col-8 d-flex flex-column" style="margin-top: 30px;">
          <div style="border: 1px solid black; text-align: center; border-radius: 8px;">
            <h4 class="mt-2">내 가입 정보</h4>
            <div class="profile1 d-flex justify-content-center py-2">
              <div class="mx-5">
                <RouterLink :to="{ name: 'UserProfileView2' }" class="btn btn-outline-secondary" style="width:300px; font-size: 30px;">예금/적금</RouterLink>
              </div>
            </div>
          </div>
          <div style="margin-top: 30px; border: 1px solid black; border-radius: 8px;">
            <RouterView style="margin: 10px;" />
          </div>
        </div>
      </div>
  
  
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { RouterLink, RouterView } from 'vue-router';
  const store = useCounterStore()
  const userInfo = store.userInformations
  
  onMounted(async () => {
    await store.getUserInformations()
  })
  </script>
  
  <style scoped>
  .profile-img {
    width: 200px;
    height: 130px;
    margin: 30px 0px 20px 0px;
    position: absolute;
    top: -140px;
    left: 17%;
    z-index: 1;
    transform: translate(-50%, 0);
  }
  </style>