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
import RecommendedFinancialProducts from '@/components/RecommendedFinancialProducts.vue'
import SavingListView from '@/views/SavingListView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import KakaoMapView from '@/views/KakaoMapView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import DepositAndSavingView from '@/views/DepositAndSavingView.vue'
import UpdateUserView from '@/views/UpdateUserView.vue'
import UserProfileView2 from '@/views/UserProfileView2.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
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
      path: '/depositandsaving',
      name: 'DepositAndSavingView',
      component: DepositAndSavingView
    },
    {
      path: '/savingList',
      name: 'SavingListView',
      component: SavingListView
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
    {
      path: '/recommend',
      name: 'recommendView',
      component: RecommendedFinancialProducts
    },
    {
      path: '/userprofile',
      name: 'UserProfileView',
      component: UserProfileView
    },
    {
      path: '/exchange',
      name: 'ExchangeView',
      component: ExchangeView
    },
    {
      path: '/kakaomap',
      name: 'KakaoMapView',
      component: KakaoMapView
    },
    // {
    //   path: '/updateuser',
    //   name: 'UpdateUserView',
    //   component: UpdateUserView
    // },
    {
      path: '/userprofile',
      name: 'UserProfileView',
      component: UserProfileView,
      children:[
        {
          path: '/UpdateUserView',
          name: 'UpdateUserView',
          component: UpdateUserView,
        },
        {
          path: '/userprofileview2',
          name: 'UserProfileView2',
          component: UserProfileView2
        },
        {
          path: '/aa',
          name: 'ArticleView',
          component: ArticleView
        },
      ]
    },
    
  ]
})

export default router
