<template>
  <div class="profile1">
    <div class="d-flex row justify-content-between" v-if="my_products && my_products.length > 0">
      <div v-for="(product, index) in my_products" :key="index" class="product-item col-6" style="width:47%;">
        <div class="product-info">
          <p><strong>은행명:</strong> {{ product?.kor_co_nm }}</p>
          <p><strong>상품명:</strong> {{ product?.fin_prdt_nm }}</p>
          <p><strong>저축기간:</strong> {{ product?.save_trm }}</p>
          <p><strong>이자유형:</strong> {{ product?.intr_rate_type }}</p>
          <p><strong>이자유형명:</strong> {{ product?.intr_rate_type_nm }}</p>
          <p><strong>기본이자:</strong> {{ product?.intr_rate }}</p>
          <p><strong>최대이자:</strong> {{ product?.intr_rate2 }}</p>
        </div>
        <div class="product-deposit">
          <p><strong>특별조건:</strong> {{ deposits[index]?.spcl_cnd }}</p>
          <p><strong>기타노트:</strong> {{ deposits[index]?.etc_note }}</p>
        </div>
        <button @click="deleteProduct(product?.id)">해지하기</button>
      </div>
    </div>
    <div v-else>
      <p>가입한 상품이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const my_products = ref(null)
const deposits = ref([])

const deleteProduct = function(subscribed_pk) {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/financial_data/delete_product/${subscribed_pk}`
  })
  .then((res) => {
    console.log(res.data);
    getUserData();
  })
  .catch((error) => {
    console.error('Error deleting product:', error);
  });
}

const getUserData = async () => {
  await store.getUserInformations();
  await axios.get("http://127.0.0.1:8000/financial_data/get_my_subscribed/", {
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    my_products.value = res.data[0];
    deposits.value = res.data[1];
  })
  .catch((error) => {
    console.error('Error fetching user data:', error);
  });
};

onMounted(getUserData);

</script>

<style scoped>
.profile1 {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.product-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 10px;
  padding: 10px;
  width: 300px;
}

.product-info {
  margin-bottom: 10px;
}

.product-deposit {
  margin-top: 10px;
}

button {
  padding: 5px 10px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>
