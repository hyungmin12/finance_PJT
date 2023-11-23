<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner all_box ">
        <div class="carousel-item active">
          <img src="src/assets/images/bg.jpg">
          <div class="ani_box">
            <!-- <img src="src/assets/images/mypage.png" alt="" class="ani_img"> -->
            <p class="slogan">
              <strong>마이페이지</strong>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="profile">
    <!-- {{ my_products[0][0] }} -->
    <!-- <div v-for="(my_product,index) in my_products" :key="index">
      {{ my_product.data[1][0][index] }}
    </div> -->
      <!-- <div v-for=" (my_product, index )  in my_products">
        {{ my_product.data[1][0][index].spcl_cnd }}
      </div> -->
      <p class="normal">기본정보</p>
      <p class="text_font">{{ userInfo.username }}님 안녕하세요</p>
      <hr class="line">
      <p class="text_font">닉네임: {{ userInfo.nickname }}</p>
      <hr class="line">
      <p class="text_font">나이 : {{ userInfo.age }}</p>
      <hr class="line">
      <p class="text_font">email : {{ userInfo.email }}</p>
    </div>
    <div class="profile1">
      <p class="normal">투자정보</p>
      <p class="text_font">평균 급여 : {{ userInfo.salary }}</p>
      <hr class="line">
      <p class="text_font">가용 투자비용 : {{ userInfo.money_for_financial }}</p>
      <hr class="line">
    </div>

    <div class="profile1">
      <p class="normal">내가 가입한 상품</p>

      <!-- <div v-for="index in my_products?.length" :key="index">
        <p>{{ my_products[index]?.kor_co_nm }}</p>
        <p>{{ my_products[index]?.fin_prdt_nm }}</p>
        <p>{{ my_products[index]?.save_trm }}</p>
        <p>{{ my_products[index]?.intr_rate_type }}</p>
        <p>{{ my_products[index]?.intr_rate_type_nm }}</p>
        <p>{{ my_products[index]?.intr_rate }}</p>
        <p>{{ my_products[index]?.intr_rate2 }}</p>
        <p>{{ deposits[index]?.spcl_cnd }}</p>
        <p>{{ deposits[index]?.etc_note }}</p>
        <button v-if="my_products.length > 0" @click="deleteProduct(my_products[index]?.id)">해지하기</button>
      </div> -->
      <div v-for="(product,index) in my_products" :key="index">
        <p>{{ product?.kor_co_nm }}</p>
        <p>{{ product?.fin_prdt_nm }}</p>
        <p>{{ product?.save_trm }}</p>
        <p>{{ product?.intr_rate_type }}</p>
        <p>{{ product?.intr_rate_type_nm }}</p>
        <p>{{ product?.intr_rate }}</p>
        <p>{{ product?.intr_rate2 }}</p>
        <p>{{ deposits[index]?.spcl_cnd }}</p>
        <p>{{ deposits[index]?.etc_note }}</p>
        <button  @click="deleteProduct(product?.id)">해지하기</button>
      </div>
    </div>

</template>
<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const userInfo = store.userInformations
const my_products = ref(null)
const deposits = ref([])

const deleteProduct = function(subscribed_pk){
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/financial_data/delete_product/${subscribed_pk}`
  })
  .then((res)=>{
    console.log(res.data);

    // 삭제 후 다시 사용자 정보 및 가입한 상품을 가져와서 UI를 업데이트
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
    .then((res)=>{
      my_products.value = res.data[0];
      deposits.value = res.data[1];
      console.log(my_products.value)
      console.log(deposits.value)
    })
    .catch((error)=>{
      console.error('Error fetching user data:', "===================");
    })
};

onMounted(getUserData);

</script>



<!-- <script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const userInfo = store.userInformations
const my_products = ref(null)
const deposits = ref([])
// const my_data = ref([])
//여기에 가입한 상품 담겨져 있음

const deleteProduct = function(subscribed_pk){
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/financial_data/delete_product/${subscribed_pk}`
  })
  .then((res)=>{
    console.log(res.data)
  })
}


onMounted(async () => {
  // console.log("===============")
  await store.getUserInformations()
  
  await axios({
    method : 'get',
    url:"http://127.0.0.1:8000/financial_data/get_my_subscribed/",
    headers: {
        Authorization: `Token ${store.token}`
    }
  })
  .then((res)=>{
    my_products.value = res.data[0]
    deposits.value = res.data[1]
  })
  .catch((err)=>{
    console.log(err)
  })
  
})

</script> -->

<style scoped>
.ani_img{
  width: 430px;
  height: 340px;
}
/* .profile{
  position: absolute;
  left: 25%;
  width: 850px;
  height: 268px;
  border: 1px solid black;
  margin-top: 20px; 
  border-radius: 13px;
}
.profile1{
  position: absolute;
  left: 25%;
  top: 80%;
  width: 850px;
  height: 200px;
  border: 1px solid black;
  margin-top: 20px; 
  border-radius: 13px;
} */
.normal{
  font-size: 20px;
  margin: 10px;
  color: rgb(223, 219, 219);
}
.text_font{
  font-size: 17px;
  margin: 10px;
  color: black;
}
.line{
  height: 2px;
  background-color: rgb(223, 219, 219);
  margin-left: 10px;
  margin-right: 10px;
}
.bg-color{
  background-color: gray;
}
</style>