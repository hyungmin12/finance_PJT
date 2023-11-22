import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useSavingStore = defineStore('saving', () => {
  const router = useRouter()
  const Savings = ref([])
  const USER_API = 'http://127.0.0.1:8000'
  // const change = ref(null)

  const getSavingitem = function(){
    //아이템처리
    axios({
      method:"get",
      url:"http://127.0.0.1:8000/financial_data/save-deposit-data/"
    })
    .then((res)=>{
      // console.log("o")
      getSavingList()
      console.log("get_deposit_item")
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  // change = computed(()=>{
  //   getDepositList()
  // })

  const getSavingList = function(){
    //리스트 처리
    axios({
      method:"get",
      url:"http://127.0.0.1:8000/financial_data/deposit_product_list/"
    })
    .then((res)=>{
      Savings.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  const changeSavings = computed(()=>{
    return Savings.value
  })



  return { getSavingList, getSavingitem, Savings, changeSavings }
}, { persist: true })
