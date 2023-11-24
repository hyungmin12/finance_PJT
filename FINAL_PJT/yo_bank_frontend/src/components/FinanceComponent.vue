
<template>
  <div>
    <table class="table w-35" style="width: 1200px;">
      <thead>
        <tr>
          <th scope="col" style="width:130px;" class="notice-board"></th>
          <th scope="col" style="width:300px;" class="notice-board">제목</th>
          <th scope="col" class="notice-board">내용</th>
          <!-- <th scope="col" class="notice-board">작성일</th> -->
        </tr>
      </thead>
      <tbody> 
        <!-- v-for="article in store.articles"
        :key="article.id"
        :article="article" -->
        <tr v-for="(article, index) in store.articles"  class="hoverable-row"  @click="router.push({name:'DetailView',params:{id:article.id}})">
            <th style="text-align:center;" scope="row">{{ index+1 }}</th>
            <td>{{ article.title }}</td>
            <td>{{ article.content }}</td>
            <!-- <td>{{ formatCreatedAt(article.created_at) }}</td> -->
        </tr>
        <div>
  </div>
      </tbody>
    </table>
  </div>

</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import { format, parseISO } from 'date-fns';

const store = useCounterStore()
const router = useRouter()

onMounted(() => {
  store.getArticles()
})

const formatCreatedAt = (createdAt) => {
  try {
    const parsedDate = parseISO(createdAt);
    return format(parsedDate, 'yyyy-MM-dd HH:mm:ss');
  } catch (error) {
    console.error('Error parsing date:', error);
    return 'Invalid Date';
  }
};

</script>

<style scoped>
  .hoverable-row:hover td {
    background-color: #f5f5f5;
  }

  table {
    border-collapse: collapse;
    width: 100%;
    border-top: 1px solid black; /* 테이블 전체의 테두리 제거 */
    border-bottom: 1px solid black; /* 테이블 전체의 테두리 제거 */
  }

  th, td {
    padding: 8px;
    text-align: left;
    border-top: 1px solid rgb(207, 205, 205); /* 테이블 전체의 테두리 제거 */
    border-bottom: 1px solid rgb(207, 205, 205); /* 각 셀의 테두리 제거 */
    border-left: none;
    border-right: none;
  }
  .notice-board{
    background-color: rgb(242, 239, 239);
  }
  .notice-bd{
    width: 300px;
  }
</style>
