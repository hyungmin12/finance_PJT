<template>
  <div>
    <table class="table w-35">
      <thead>
        <tr>
          <th scope="col">제목</th>
          <th scope="col">내용</th>
          <th scope="col">좋아요</th>
          <th scope="col">조회</th>
          <th scope="col">댓글</th>
          <th scope="col">작성일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index" @click="redirectToSite(item.id)" :class="{ 'row-hover': hoveredIndex === index }">
          <td>{{ item.title }}</td>
          <td>{{ item.content }}</td>
          <td>{{ item.likes }}</td>
          <td>{{ item.views }}</td>
          <td>{{ item.comments }}</td>
          <td>{{ item.createdDate }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
const items = [
  { id: 1, title: 'Title 1', content: 'Content 1', likes: 5, views: 10, comments: 3, createdDate: '2023-11-20' },
  { id: 2, title: 'Title 2', content: 'Content 2', likes: 8, views: 15, comments: 2, createdDate: '2023-11-21' },
  { id: 3, title: 'Title 3', content: 'Content 3', likes: 12, views: 20, comments: 5, createdDate: '2023-11-22' },
];

let hoveredIndex = null;

const redirectToSite = (itemId) => {
  // Replace 'YOUR_TARGET_URL' with the actual URL you want to redirect to.
  window.location.href = `YOUR_TARGET_URL/${itemId}`;
};
</script>

<style scoped>
.table {
  border-collapse: collapse;
  width: 100%;
}

td {
  text-align: left;
  padding: 8px;
  transition: background-color 0.3s;
}

tr.row-hover:hover {
  background-color: #f5f5f5;
  cursor: pointer;
}
</style>
