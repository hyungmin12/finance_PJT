<template>
  <div>
    <h1 style="text-align: center; margin-top: 30px;">여기는 __원이하 자산관리 커뮤니티 입니다.</h1>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner all_box ">
        <div class="carousel-item active">
          <img src="src/assets/images/bg.jpg">
          <div class="ani_box">
            <img src="src/assets/images/travel.jpg" alt="" class="ani_img">
            <p class="slogan">
              <strong>자산관리 전략</strong><br>어떻게 세워야 할까?
            </p>
          </div>
        </div>
      </div>
      <!-- <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button> -->
    </div>
    <div class="container d-flex flex-row justify-content-center">
        <TravelComponent class="m-5"/>
      </div>
  </div>
</template>

<script setup>
import TravelComponent from '@/components/TravelComponent.vue';
</script>

<style scoped>
.all_box {
  height: 350px;
  margin-top: 50px;
}

.ani_box {
  width: 1000px;
  margin: 0 auto;
  position: relative; /* 부모 요소에 대해 상대적 위치 설정 */
}

.ani_img {
  position: absolute;
  top: 0;
  right: 0;
  width: 480px;
  height: 300px;
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
</style>
