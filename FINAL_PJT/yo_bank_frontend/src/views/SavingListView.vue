<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner all_box ">
        <div class="carousel-item active">
          <img src="src/assets/images/bg.jpg" style="height:300px;  width:100%;" >
          <div class="ani_box">
            <img src="src/assets/images/deposit.png" alt="" class="ani_img">
            <p class="slogan">
              <strong>적금</strong>
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="d-flex justify-content-center m-0">
      <RouterLink to="/depositList" class="navvar m-5"><button style="width:150px;" class="btn btn-lg btn-outline-secondary">예금</button></RouterLink>
        <RouterLink to="/savingList" class="navvar m-5"><button style="width:150px;" class="btn btn-lg btn-outline-secondary">적금</button></RouterLink>
    </div>
    <SavingListComponents/>
  </div>
  
</template>

<script setup>
import SavingListComponents from '@/components/SavingListComponents.vue';
import { useSavingStore } from '@/stores/saving.js'
import axios from 'axios'
import { ref, onMounted } from 'vue'
const store = useSavingStore()

onMounted(async () => {
  // 첫 번째 비동기 함수 호출
  await store.getSavingitem()
});


</script>

<style lang="scss" scoped>
.ani_img{
  position: absolute;
  top: -30%;
  width: 350px;
  height: 350px;
}
</style>