<template>
<div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="src/assets/images/img.JPG" alt="...">
    </div>
    <div class="carousel-item">
      <img src="src/assets/images/img1.jpg" alt="...">
    </div>
    <div class="carousel-item">
      <img src="src/assets/images/img2.jpg" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
<div class="container d-flex flex-row justify-content-center">
  <FinanceComponent class="m-5"/><TravelComponent class="m-5"/>
</div>
</template>

<script setup>
  import FinanceComponent from '@/components/FinanceComponent.vue';
  import TravelComponent from '@/components/TravelComponent.vue';
</script>

<style scoped>
img{
  width: 2000px;
  height: 530px;
}
</style>