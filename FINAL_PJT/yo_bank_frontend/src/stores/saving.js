import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

// 1. getSavingitem구현
// 2. getSavingList구현




export const useSavingStore = defineStore('saving', () => {
  const router = useRouter()
  const Savings = ref([])
  const USER_API = 'http://127.0.0.1:8000'
  // const change = ref(null)

  const getSavingitem = function(){
    
    axios({
      method:"get",
      url:"http://127.0.0.1:8000/financial_data/save-saving-data/"
    })
    .then((res)=>{
      // console.log("o")
      getSavingList()
      console.log("get_saving_item")
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  const getSavingList = function(){
    //리스트 처리
    axios({
      method:"get",
      url:"http://127.0.0.1:8000/financial_data/saving_product_list/"
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
