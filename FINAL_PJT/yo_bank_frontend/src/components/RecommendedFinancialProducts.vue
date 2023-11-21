<template>
  <div>
    <h1>금융추천상품 칸</h1>
  </div>
</template>

<script setup>
import { useRecommendStore } from '@/stores/recommend'
import { ref, onMounted } from 'vue'
const store = useRecommendStore()

onMounted(async () => {
  // console.log("===============")
  await store.getDepositRecommended()
  // console.log(store.userInformations,"===여기 컴포넌트===")
  // console.log(store.userInformations.username)
  // console.log("===============")
})

</script>

<style scoped>

</style>
