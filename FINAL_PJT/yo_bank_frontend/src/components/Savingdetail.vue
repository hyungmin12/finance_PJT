
<template>
  <tr style="border-bottom: solid 1px black;">
    <td style="text-align: center;">{{ saving.kor_co_nm }}</td>
    <td style="text-align: center;">{{ saving.fin_prdt_nm }}</td>
    <td style="text-align: center;">
        <button @click="toggleDetails" class="btn btn-outline-dark">자세히 보기</button>
    </td>
  </tr>
  <td colspan="3">
      <div v-if="isShow" style="display: inline-block; width:100%;">
          <div class="d-flex flex-column mb-4" style="background-color: lightgray;" >
              <td class="fw-bold" style="padding-left: 150px; padding-right: 40px;">부가 조건 : {{saving.etc_note}}</td>
              <td class="fw-bold" style="padding-left: 150px; padding-right: 40px;">특별 조건 : {{saving.spcl_cnd}}</td>
          </div>
          <div class="d-flex justify-content-between">
            <span style="text-align: center; width: 25%;">금융기관</span>
            <span style="text-align: center; width: 25%;">상품</span>
            <span style="text-align: center; width: 25%;">자세히 보기</span>
            <div style="padding-right: 85px;">
              <input v-model="amount" type="text" style= "width: 100px;">
            </div>
          </div>
          <hr style="height: 1px;">
    <div v-for="option of saving.options" :key="option.save_trm" style="display: inline-block;" class="d-flex flex-column">
      <div class="d-flex justify-content-between">
        <span style="text-align: center; width: 25%;">{{ option.save_trm }}</span>
        <span style="text-align: center; width: 25%;">{{ option.intr_rate }}</span>
        <span style="text-align: center; width: 25%;">{{ option.intr_rate2 }}</span>
        <div style="padding-right: 100px;">
        <form @submit.prevent="signUpThisSaving(option.id)" style="text-align: right; display: inline-block; width: 25%;">
            <input type="submit" class="btn btn-outline-secondary" value="가입하기">
          </form>
        </div>
    </div>
    <hr style="height: 1px;">
  </div>
  </div>
</td>
</template>

<script setup>
  import { ref } from 'vue'
  import { useSavingStore } from "@/stores/saving.js";
  import { useCounterStore } from "@/stores/counter.js";
  import axios from 'axios'
  const isShow = ref(false)

const store2 = useCounterStore();
const token = store2.token;
const amount = ref(null)



  defineProps({
      saving:Object
  })
  const toggleDetails = () => {
  // showDetails.value[depositId] = !showDetails.value[depositId];
  if (isShow.value) {
      isShow.value = false
  } else {
      isShow.value = 1
  }
  };


const signUpThisSaving = function (optionPk) {
  axios({
    method: "POST",
    url: `http://127.0.0.1:8000/financial_data/signup_saving/${optionPk}`,
    headers: {
      Authorization: `Token ${token}`,
    },
    data : {
      amount : amount.value
    }
  })
  .then((res) => {
    amount.value = null
    console.log(res.data);
    amount.value = null
    if (res.data.message === "already"){
      alert("이미 가입한 상품입니다.")
    }
    else if(res.data.message === "okay"){
      alert("상품에 가입 되었습니다.")
    }
  })
  .catch((err) => {
    console.log(err);
  });
};
</script>

<style scoped>

</style>