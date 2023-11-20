import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  const router = useRouter()
  const deposits = ref([])
  const USER_API = 'http://127.0.0.1:8000'

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



  return { getDepositList, deposits }
}, { persist: true })
