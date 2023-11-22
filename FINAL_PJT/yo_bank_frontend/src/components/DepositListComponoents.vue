<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>금융기관</th>
          <th>상품</th>
          <th>자세히 보기</th>
        </tr>
      </thead>
      <tbody>
        <Depositdetail 
        v-for="deposit of store.changeDeposits" :key="deposit.id"
        :deposit="deposit"
        />
      </tbody>
    </table>
  </div>
</template>


<script setup>
import { ref } from "vue";
import { useProductStore } from "@/stores/product.js";
import { useCounterStore } from "@/stores/counter.js";
import axios from "axios";
import Depositdetail from '@/components/Depositdetail.vue'

const store = useProductStore();
const store2 = useCounterStore();
const showDetails = ref({});
const token = store2.token;
const amount = ref(null)

</script>

<style lang="scss" scoped>
/* 필요한 스타일링을 추가할 수 있습니다. */
table {
  border-collapse: collapse;
  width: 90%;
  margin: 1rem auto;
  background-color: white;
}

/* 테이블 행 */
th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  text-align: center;
}

th {
  background-color: #1b1b1b;
  color: #ddd;
}

</style>