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

onMounted(() => {
      store.getDepositList()
    });


</script>

<style lang="scss" scoped>

</style>