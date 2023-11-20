<template>
  <div class="head">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="d-flex justify-content-between w-100">
    <div>
      <RouterLink to="/" class="me-auto p-2 bd-highlight">VO-BANK</RouterLink>
    </div>
    <div>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 ma-2 pa-2">
          <li class="nav-item">
            <RouterLink to="/community1">커뮤니티1</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/community2" class="navvar">커뮤니티2</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/login" class="navvar m-5">로그인</RouterLink>
          </li>
        </ul>
      </div>
  </div>
    </nav>
  </div>
  <RouterView/>
</template>

<script setup>

</script>

<style scoped>
  a{
    text-decoration: none;
    color: black;
  }
  .navvar{
    margin-left: 30px;
  }
</style>