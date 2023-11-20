<template>
  <div>
    <h1>depositListComponent</h1>
    <p v-for="deposit of store.deposits">{{deposit.fin_co_no}}</p>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product.js'
const store = useProductStore()
console.log(store.deposits[0])

</script>

<style lang="scss" scoped>

</style>