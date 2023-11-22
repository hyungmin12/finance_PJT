<template>
    <tr style="border-bottom: solid 1px black;">
      <td style="text-align: center;">{{ deposit.kor_co_nm }}</td>
      <td style="text-align: center;">{{ deposit.fin_prdt_nm }}</td>
      <!-- <td style="text-align: center;" v-html="deposit.etc_note.split('-').join('<br>')"></td> -->

      <!-- <td style="text-align: center;">{{ deposit.etc_note }}</td> -->
      <td style="text-align: center;">
        <button @click="toggleDetails">Toggle Details</button>
      </td>
    </tr>
    <tr>
    <td colspan="3">
        <div v-if="isShow" style="display: inline-block; width:100%;">
            
            <div class="d-flex flex-column mb-4" style="background-color: lightgray;" >
                <td class="fw-bold" style="padding-left: 150px; padding-right: 40px;">부가 조건 : {{deposit.etc_note}}</td>
                <td class="fw-bold" style="padding-left: 150px; padding-right: 40px;">특별 조건 : {{deposit.spcl_cnd}}</td>
            </div>
            
            
            <div class="d-flex justify-content-between">
                <span style="text-align: center; width: 25%;">예치기간</span>
                <span style="text-align: center; width: 25%;">보통이자</span>
                <span style="text-align: center; width: 25%;">우대이자</span>
                <div style="padding-right: 100px;">
                <input v-model="amount" type="text" >
                </div>
            </div>
                

            <hr style="height: 1px;">
        <div v-for="option of deposit.options" :key="option.save_trm" style="display: inline-block;" class="d-flex flex-column">
            <div class="d-flex justify-content-between">
                <span style="text-align: center; width: 25%;">{{ option.save_trm }}</span>
                <span style="text-align: center; width: 25%;">{{ option.intr_rate }}</span>
                <span style="text-align: center; width: 25%;">{{ option.intr_rate2 }}</span>
                <!-- <span style="text-align: center; width: 25%;">{{ option. }}</span> -->
                <div style="padding-right: 100px;">
                <form @submit.prevent="signUpThisProduct(option.id)" style="text-align: right; display: inline-block; width:25%;">
                    <input type="submit" value="가입하기">
                </form>
                </div>
            </div>
            <hr style="height: 1px;">
        </div>
        </div>
    </td>
    </tr>

</template>

<script setup>
import { ref } from 'vue'
import { useProductStore } from "@/stores/product.js";
import { useCounterStore } from "@/stores/counter.js";
import axios from "axios";

const store = useProductStore();
const store2 = useCounterStore();
const showDetails = ref({});
const token = store2.token;
const amount = ref(null)


const signUpThisProduct = function (optionPk) {
  axios({
    method: "POST",
    url: `http://127.0.0.1:8000/financial_data/signup_deposit/${optionPk}`,
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
  })
  .catch((err) => {
    console.log(err);
  });
};
const isShow = ref(false)
defineProps({
    deposit:Object
})
const toggleDetails = () => {
// showDetails.value[depositId] = !showDetails.value[depositId];
if (isShow.value) {
    isShow.value = false
} else {
    isShow.value = 1
}
};
</script>

<style scoped>

</style>