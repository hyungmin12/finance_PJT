import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import HomeView from '@/views/HomeView.vue'
import DepositListView from '@/views/DepositListView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import UpdateView from '@/views/UpdateView.vue'
import Community1View from '@/views/Community1View.vue'
import Community2View from '@/views/Community2View.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      // 다시 건들기
      path: '/aa',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/depositList',
      name: 'DepositListView',
      component: DepositListView
    },
    {
      path: '/community1',
      name: 'Community1View',
      component: Community1View
    },
    {
      path: '/community2',
      name: 'Community2View',
      component: Community2View
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/update/:id',
      name: 'UpdateView',
      component: UpdateView
    },
  ]
})

import { useCounterStore } from '@/stores/counter'

// router.beforeEach((to, from) => {
//   const store = useCounterStore()
//   if (to.name === 'ArticleView' && !store.isLogin) {
//     window.alert('로그인이 필요합니다.')
//     return { name: 'LogInView' }
//   }
//   if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
//     window.alert('이미 로그인 했습니다.')
//     return { name: 'ArticleView' }
//   }
// })

export default router
