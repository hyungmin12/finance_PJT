<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner all_box ">
        <div class="carousel-item active">
          <img src="src/assets/images/bg.jpg">
          <div class="ani_box">
            <img src="src/assets/images/asset_management.png" alt="" class="ani_img">
            <p class="slogan">
              <strong>자산관리 전략</strong><br>어떻게 세워야 할까?
            </p>
          </div>
        </div>
      </div>
      <div class="text-create" style="text-align: right; margin-top: 20px; margin-right: 178px;">
        <RouterLink :to="{ name: 'CreateView' }" class="text-create">
          글쓰기
        </RouterLink>
      </div>
    </div>
    <div>
      <FinanceComponent />
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import FinanceComponent from '@/components/FinanceComponent.vue'

const store = useCounterStore()



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
.text-create{
  text-decoration-line: none;

}
</style>
