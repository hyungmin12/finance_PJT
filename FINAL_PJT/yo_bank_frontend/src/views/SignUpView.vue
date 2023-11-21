<template>
  <div>
    <h1>Signup</h1>
    <form class="d-flex flex-column" @submit.prevent="signUp">
      <p>아이디 : <input type="text" v-model.trim="username"></p>
      <p>비밀번호 : <input type="password" v-model.trim="password1"></p>
      <p>비밀번호 확인 <input type="password" v-model.trim="password2"></p>
      <p>닉네임 : <input type="text" v-model.trim="nickname"></p>
      <p>나이 : <input type="text" v-model.trim="age"></p>
      <p>email : <input type="text" v-model.trim="email"></p>
      <p>가용 투자비용 : <input type="text"  v-model.trim="money_for_financial"></p>
      <p>가용 여행비용 : <input type="text"  v-model.trim="money_for_travel"></p>
      <p>평균 급여 : <input type="text" v-model.trim="salary"></p>

      <input type="submit">
    </form>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const email = ref(null)
const age = ref(null)
const money_for_financial = ref(null)
const money_for_travel = ref(null)
const salary = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    email: email.value,
    age: age.value,
    // used_money_for_financial : 0,
    // left_money_for_financial : 0,
    money_for_financial: money_for_financial.value,
    money_for_travel: money_for_travel.value,
    salary : salary.value,
  }
  // console.log(username,money_for_financial,salary)
  store.signUp(payload)
}


</script>

<style>

</style>
