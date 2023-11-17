<template>

  <div>
    <h1>나는 환율계산기</h1>
    <!-- <p v-for="ex of store.exchange_data">
      <p>{{ ex.ttb }}</p>
    </p> -->
  <div>
    <select style="height:30px;" class="m-1" @change="findrequiredDealbasr(selectedCountry)" v-model="selectedCountry">
      <option v-for="ex of store.exchange_data">
        {{ex.cur_nm}}
      </option>
    </select>
    <input class="m-1" style="width:300px;" type="text" @input="changeflag_dela" v-model="required_won">

  </div>

  <input @input="changeflag_won" clsss="m-1" type="text" v-model="required_dela_bas_r">
  <button @click="ChangerequiredDealbasr(selectedCountry)">환율계산</button>

  </div>

</template>

<script setup>

import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { ref,computed } from 'vue'

//ttb = 환율 값
const store = useCounterStore()
const selectedCountry = ref([])
const required_dela_bas_r = ref(null)
const required_won = ref(null)
let flag = false
let required_dela = 0

const changeflag_won = function(){
  flag = true
  console.log(flag)
  required_dela = required_dela_bas_r.value
  console.log(required_dela)
}

const changeflag_dela = function(){
  flag = false
}

const findrequiredDealbasr= function(keyName) {
    const temp = store.exchange_data.filter(item => item.cur_nm === keyName)
    required_dela_bas_r.value = temp[0].deal_bas_r.replace(/,/g,'')
    // required_won.value = null
  }

const ChangerequiredDealbasr= function(keyName) {
  const temp = store.exchange_data.filter(item => item.cur_nm === keyName)
  required_dela_bas_r.value = temp[0].deal_bas_r.replace(/,/g,'')
  if (flag === false){
      required_dela_bas_r.value = required_dela_bas_r.value * required_won.value
    }
  else if (flag === true){
      console.log(required_dela_bas_r.value , required_dela)
      required_won.value =  required_dela / required_dela_bas_r.value
      required_dela_bas_r.value = required_dela
  }
  }


</script>


<style lang="scss" scoped>

</style>