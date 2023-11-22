<template>
  <div>
    <h1>여기 Saving List</h1>
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

  // 첫 번째 함수가 완료된 후에 두 번째 비동기 함수 호출
  // await store.getDepositList()
});


</script>

<style lang="scss" scoped>

</style>