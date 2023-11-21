<template>
  <header>
    <form @submit.prevent="store.logOut">
        <input type="submit" value="logOut">
    </form>
    <top/>
  </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import top from '@/components/top.vue';
import DepositListView from '@/views/DepositListView.vue';

import ExchangeComponents from '@/components/ExchangeComponents.vue'
import KakaoMapComponents from '@/components/KakaoMapComponents.vue'
import { useProductStore } from '@/stores/product.js'


const store = useCounterStore()



</script>

<style scoped>
</style>

<!-- store.exchange_data[0] -->