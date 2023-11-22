<template>
  <div>
    <table class="table w-35" style="width: 1200px;">
      <thead>
        <tr>
          <th scope="col" class="notice-board"></th>
          <th scope="col" class="notice-board"></th>
          <th scope="col" class="notice-board">조회</th>
          <th scope="col" class="notice-board">댓글</th>
          <th scope="col" class="notice-board">작성일</th>
        </tr>
      </thead>
      <tbody> 
        <tr class="hoverable-row">
          <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
            <th scope="row">{{ article.id }}</th>
            <td>{{ article.title }}</td>
            <td>{{ article.content }}</td>
            <td>{{ article.content }}</td>
            <td>{{ article.content }}</td>
            <!-- [Detail] -->
          </RouterLink>
        </tr>
        <div>
    <hr>
  </div>
      </tbody>
    </table>
  </div>

</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})

defineProps({
  article: Object
})



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
