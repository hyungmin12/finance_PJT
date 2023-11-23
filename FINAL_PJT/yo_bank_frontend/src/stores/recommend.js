import { ref, onMounted, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'



export const useRecommendStore = defineStore('recommend', () => {
  // user 별로 1~50 51~100 101~150 151~200 201~300 301이상으로 userGrade에 딕셔너리 형태로 저장하기
  const userDepositRecommended = ref({})
  const userSavingRecommended = ref({})
  const userStore = useCounterStore()
  const tokens = ref(null)
  const myDeposit = ref(null)

  const getMyDeposit = function(){
    axios({
      method : 'get',
      url : 'http://127.0.0.1:8000/financial_data/get_my_deposit',
      headers: {
        Authorization: `Token ${tokens.value}`
      }
    })
    .then((res)=>{
      myDeposit.value = res.data
      // console.log(myDeposit.value)
    })
    .catch((err)=>{
      console.log(err.value)
    })
  }


  if (userStore.token != undefined){
    tokens.value = userStore.token
    // console.log(tokens.value)
  }
  // const token = userStore.token.value

  const getDepositRecommended = function(){
    axios({
      method : 'get',
      url : 'http://127.0.0.1:8000/financial_data/get_deposit_recommend',
      headers: {
        Authorization: `Token ${tokens.value}`
      }
    })
    .then((res)=>{
      userDepositRecommended.value = res.data
    })
    .catch((err)=>{
      console.log(err.value)
    })
  }

  const getSavingRecommended = function(){
    axios({
      method : 'get',
      url : 'http://127.0.0.1:8000/financial_data/get_saving_recommend',
      headers: {
        Authorization: `Token ${tokens.value}`
      }
    })
    .then((res)=>{
      userSavingRecommended.value = res.data
    })
    .catch((err)=>{
      console.log(err.value)
    })
  }



  return { myDeposit,getMyDeposit, userSavingRecommended, getSavingRecommended, getDepositRecommended, userDepositRecommended, }
}, { persist: true })
