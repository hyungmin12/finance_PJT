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
        <tr class="hoverable-row">
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>ddd</td>
          <td>ddd</td>
          <td>ddd</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
</script>

<style scoped>
  .hoverable-row:hover td {
    background-color: #f5f5f5;
  }

  table {
    border-collapse: collapse;
    width: 100%;
  }

  th, td {
    padding: 8px;
    text-align: left;
  }
</style>
