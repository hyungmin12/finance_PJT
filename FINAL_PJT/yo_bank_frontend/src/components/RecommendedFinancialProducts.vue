<template>
  <div>
    <h1>금융추천상품 칸</h1>
    <p v-for="recommended of store.userDepositRecommended">
      <p>{{ recommended.rank }}위 {{ recommended.kor_co_nm }}</p>
      <p>상품명 : {{ recommended.fin_prdt_nm }}</p>
      <p>이자 : {{ recommended.intr_rate }}</p>
      <p>우대이자 : {{ recommended.intr_rate2 }}</p>
      <p>가입방법 : {{ recommended.join_way }}</p>
      <p>가입대상 : {{ recommended.join_member }}</p>
      <p>이자 타입 : {{ recommended.intr_rate_type_nm }}</p>
      <p>예치기간 : {{ recommended.save_trm }}</p>
      <p>상세 : {{ recommended.spcl_cnd }}</p>
      <p>기타 : {{ recommended.etc_note }}</p>
      <hr>
      
    </p>
  </div>
</template>

<script setup>
import { useRecommendStore } from '@/stores/recommend'
import { ref, onMounted } from 'vue'
const store = useRecommendStore()

onMounted(async () => {
  await store.getDepositRecommended()
})

</script>

<style scoped>

</style>
