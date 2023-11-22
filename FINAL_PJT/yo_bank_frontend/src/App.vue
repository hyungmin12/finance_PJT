<template>
  <header>
    <top/>
    <!-- <RecommendedFinancialProducts/> -->
  </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import top from '@/components/top.vue';


const store = useCounterStore()



</script>

<style scoped>
</style>

<!-- store.exchange_data[0] -->