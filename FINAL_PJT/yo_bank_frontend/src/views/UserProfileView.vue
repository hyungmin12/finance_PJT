<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner all_box ">
        <div class="carousel-item active">
          <img src="src/assets/images/bg.jpg">
          <div class="ani_box">
            <img src="src/assets/images/mypage.png" alt="" class="ani_img">
            <p class="slogan">
              <strong>마이페이지</strong>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
    <div class="profile">
      <p class="normal">기본정보</p>
      <p class="text_font">{{ userInfo.username }}님 안녕하세요</p>
      <hr class="line">
      <p class="text_font">닉네임: {{ userInfo.nickname }}</p>
      <hr class="line">
      <p class="text_font">나이 : {{ userInfo.age }}</p>
      <hr class="line">
      <p class="text_font">email : {{ userInfo.email }}</p>
    </div>
    <div class="profile1">
      <p class="normal">투자정보</p>
      <hr class="line">
      <p class="text_font">가용투자비용 : {{ userInfo.money_for_financial }}</p>
      <hr class="line">
      <p class="text_font">평균 급여 : {{ userInfo.salary }}</p>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const userInfo = store.userInformations
onMounted(async () => {
  // console.log("===============")
  await store.getUserInformations()
  // console.log(store.userInformations,"===여기 컴포넌트===")
  // console.log(store.userInformations.username)
  // console.log("===============")
})

</script>

<style scoped>
.ani_img{
  width: 430px;
  height: 340px;
}
.profile{
  position: absolute;
  left: 25%;
  width: 850px;
  height: 268px;
  border: 1px solid black;
  margin-top: 20px; 
  border-radius: 13px;
}
.profile1{
  position: absolute;
  left: 25%;
  top: 80%;
  width: 850px;
  height: 200px;
  border: 1px solid black;
  margin-top: 20px; 
  border-radius: 13px;
}
.normal{
  font-size: 20px;
  margin: 10px;
  color: rgb(223, 219, 219);
}
.text_font{
  font-size: 17px;
  margin: 10px;
  color: black;
}
.line{
  height: 2px;
  background-color: rgb(223, 219, 219);
  margin-left: 10px;
  margin-right: 10px;
}
.bg-color{
  background-color: gray;
}
</style>