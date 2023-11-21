import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  const router = useRouter()
  const deposits = ref([])
  const USER_API = 'http://127.0.0.1:8000'
  // const change = ref(null)

  const getDeposititem = function(){
    axios({
      method:"get",
      url:"http://127.0.0.1:8000/financial_data/save-deposit-data/"
    })
    .then((res)=>{
      // console.log("o")
      getDepositList()
      console.log("get_deposit_item")
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  // change = computed(()=>{
  //   getDepositList()
  // })

  const getDepositList = function(){
    axios({
      method:"get",
      url:"http://127.0.0.1:8000/financial_data/deposit_product_list/"
    })
    .then((res)=>{
      deposits.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  const changeDeposits = computed(()=>{
    return deposits.value
  })



  return { getDepositList, getDeposititem, deposits, changeDeposits }
}, { persist: true })
