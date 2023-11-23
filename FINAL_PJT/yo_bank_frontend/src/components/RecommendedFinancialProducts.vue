<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner all_box">
        <div class="carousel-item active">
          <img src="src/assets/images/bg.jpg">
          <div class="ani_box">
            <img src="src/assets/images/best.png" alt="" class="ani_img">
            <p class="slogan">
              <strong>금융추천상품</strong>
            </p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <FinanceComponent
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
      />
    </div>
  </div>
  <div class="profiles-container">
    <div class="profile" style="width: 800px;">
      <h1 class="text" style="text-align: center;">예금순위</h1>
      <hr class="line">
      <div v-for="recommended of store.userDepositRecommended" :key="recommended.id" class="recommendation" style="height:540px;">
        <strong><p class="fw-bold" style="font-size : 25px;">{{ recommended.rank }}위 {{ recommended.kor_co_nm }}</p></strong>
        <p><strong>상품명:</strong> {{ recommended.fin_prdt_nm }}</p>
        <p><strong>이자:</strong> {{ recommended.intr_rate }}</p>
        <p><strong>우대이자:</strong> {{ recommended.intr_rate2 }}</p>
        <p><strong>가입방법:</strong> {{ recommended.join_way }}</p>
        <p><strong>가입대상:</strong> {{ recommended.join_member }}</p>
        <p><strong>이자 타입:</strong> {{ recommended.intr_rate_type_nm }}</p>
        <p><strong>예치기간:</strong> {{ recommended.save_trm }}</p>
        <p><strong>상세:</strong> {{ recommended.spcl_cnd }}</p>
        <p><strong>기타:</strong> {{ recommended.etc_note }}</p>
        <!-- <hr style="background-color: lightcyan; height: 3px;"> -->
      </div>
    </div>
    <div class="profile" style="width: 800px;">
      <h1 class="text" style="text-align: center;">적금순위</h1>
      <hr class="line">
      <div v-for="recommended of store.userSavingRecommended" :key="recommended.id" class="recommendation" style="height:540px;">
        <strong><p class="fw-bold" style="font-size : 25px;">{{ recommended.rank }}위 {{ recommended.kor_co_nm }}</p></strong>
        <p><strong>상품명:</strong> {{ recommended.fin_prdt_nm }}</p>
        <p><strong>이자:</strong> {{ recommended.intr_rate }}</p>
        <p><strong>우대이자:</strong> {{ recommended.intr_rate2 }}</p>
        <p><strong>가입방법:</strong> {{ recommended.join_way }}</p>
        <p><strong>가입대상:</strong> {{ recommended.join_member }}</p>
        <p><strong>이자 타입:</strong> {{ recommended.intr_rate_type_nm }}</p>
        <p><strong>예치기간:</strong> {{ recommended.save_trm }}</p>
        <p><strong>상세:</strong> {{ recommended.spcl_cnd }}</p>
        <p><strong>기타:</strong> {{ recommended.etc_note }}</p>
        <!-- <hr style="background-color: lightcyan; height: 3px;"> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRecommendStore } from '@/stores/recommend'
import { ref, onMounted } from 'vue'
const store = useRecommendStore()

onMounted(async () => {
  await store.getDepositRecommended()
  await store.getSavingRecommended()
})

</script>

<style scoped>
.banking-page {
  text-align: center;
  color: #fff;
}

.carousel-container {
  /* Your carousel styles remain unchanged */
}

.profile {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #f8f9fa;
}

.profile h2,
.profile1 h2 {
  font-size: 24px;
  color: #007bff;
}

.text_font {
  font-size: 18px;
  margin: 10px 0;
  color: #333;
}

.line {
  height: 2px;
  background-color: #007bff;
  margin: 10px 0;
}

.ani_img {
  width: 250px;
  height: 260px;
}

.profiles-container {
  display: flex;
  justify-content: center;
}

.recommendation {
  margin-bottom: 15px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
}

button {
  padding: 5px 10px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>
