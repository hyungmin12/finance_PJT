<template>
  <header>
    <top/>
    <!-- <RecommendedFinancialProducts/> -->
    <!-- <ChangeUserInfoComponents/> -->
  </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
// import ChangeUserInfoComponents from '@/components/ChangeUserInfoComponents.vue';

import top from '@/components/top.vue';


const store = useCounterStore()



</script>

<style scoped>
</style>

<!-- store.exchange_data[0] -->