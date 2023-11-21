import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const articles = ref([])
  const exchange_data = ref([])
  const USER_API = 'http://127.0.0.1:8000'
  const token = ref(null)
  const EXCHANGE_API = 'cScsNMc43zgGq56PFZDLCLqWdRhiZizf'
  const EXCHANGE_URL = '/exchange-api?authkey=' + EXCHANGE_API + '&data=AP01'



  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${USER_API}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const {   username,
              password1,
              password2,
              nickname,
              email,
              age,
              money_for_financial,
              money_for_travel,
              salary, } = payload
    // console.log(typeof money_for_financial)
    // money_for_financial = Number(money_for_financial)
    // money_for_travel = Number(money_for_travel)
    // age = Number(age)
    // salary = Number(salary)
    // const data = new FormData();
    // data.append('username',username)
    // data.append('password1',password1)
    // data.append('password2',password2)
    // data.append('nickname',nickname)
    // data.append('email',email)
    // data.append('age',age)
    // data.append('money_for_financial',money_for_financial)
    // data.append('money_for_travel',money_for_travel)
    // data.append('salary',salary)
    
    axios({
      method: 'post',
      url: `${USER_API}/accounts/signup/`,
      data: {
              username: username,
              password1: password1,
              password2: password2,
              nickname: nickname,
              email: email,
              age: age,
              money_for_financial: money_for_financial,
              money_for_travel: money_for_travel,
              salary : salary,
            }
      })
      .then((res) => {
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${USER_API}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${USER_API}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  const exchange = function() {
    //ttb를 사용해야함
    axios({
      method: 'GET',
      url: EXCHANGE_URL,
    })
    .then((res) => {
      exchange_data.value = res.data
      // console.log(exchange_data.value,"--------==========")
    })
    .catch((err) => {
      console.log(err)
    })
  }

  return { articles, USER_API, getArticles, signUp, logIn, token, isLogin, logOut, exchange, exchange_data  }
}, { persist: true })
