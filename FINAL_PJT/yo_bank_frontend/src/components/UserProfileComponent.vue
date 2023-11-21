<template>
  <div>
    <h1>여기가 프로필!!</h1>
    <p>{{ userInfo.username }}</p>
    <p>{{ userInfo.nickname }}</p>
    <p>{{ userInfo.age }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const userInfo = store.userInformations
onMounted(async () => {
  // console.log("===============")
  await store.getUserInformations()
  // console.log(store.userInformations,"===여기 컴포넌트===")
  // console.log(store.userInformations.username)
  // console.log("===============")
})

</script>

<style scoped>

</style>
