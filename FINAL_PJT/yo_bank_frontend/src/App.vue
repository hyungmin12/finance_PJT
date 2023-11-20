<template>
  <header>
    <form @submit.prevent="store.logOut">
        <input type="submit" value="logOut">
    </form>

    <div class="m-5 border border-black" >
      <ExchangeComponents/>
    </div>
    <div>
      <KakaoMapComponents/>
    </div>

    <nav>
      <RouterLink :to="{ name: 'SignUpView' }">SignUp</RouterLink>
      <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink>
      <RouterLink :to="{ name: 'DepositListView'}">DepositList</RouterLink>
    </nav>
    
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import ExchangeComponents from '@/components/ExchangeComponents.vue'
import KakaoMapComponents from '@/components/KakaoMapComponents.vue'

import axios from 'axios'

const store = useCounterStore()



</script>

<style scoped>
</style>

<!-- store.exchange_data[0] -->