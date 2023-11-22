<template>
<div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner" style="height: 100px;">
    <div class="carousel-item active" >
      <img src="src/assets/images/img1.jpg" alt="...">
      <!-- <img src="..." class="d-block w-100" alt="..."> -->
    </div>
    <div class="carousel-item">
      <img src="src/assets/images/img2.jpg" alt="...">
      <!-- <img src="..." class="d-block w-100" alt="..."> -->
    </div>
    <div class="carousel-item">
      <img src="src/assets/images/img.JPG" alt="...">
      <!-- <img src="..." class="d-block w-100" alt="..."> -->
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
<div v-if="store.isLogin" class="container d-flex flex-row justify-content-center">
  <FinanceComponent class="m-5"/><TravelComponent class="m-5"/>
</div>
<h1 v-if="!store.isLogin">로그인 해주세요</h1>
</template>

<script setup>
  import FinanceComponent from '@/components/FinanceComponent.vue';
  import TravelComponent from '@/components/TravelComponent.vue';
  import { useCounterStore } from '@/stores/counter';
  const store = useCounterStore()
</script>

<style scoped>
img {
  width: 2000px;
  height: 530px;
}

</style>