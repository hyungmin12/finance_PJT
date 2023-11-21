<template>
  <div>
    <h1>여기 Deposit List</h1>
    <DepositListComponoents/>
  </div>
  
</template>

<script setup>
import DepositListComponoents from '@/components/DepositListComponoents.vue';
import { useProductStore } from '@/stores/product.js'
import axios from 'axios'
import { ref, onMounted } from 'vue'
const store = useProductStore()

onMounted(async () => {
  // 첫 번째 비동기 함수 호출
  await store.getDeposititem()

  // 첫 번째 함수가 완료된 후에 두 번째 비동기 함수 호출
  // await store.getDepositList()
});


</script>

<style lang="scss" scoped>

</style>