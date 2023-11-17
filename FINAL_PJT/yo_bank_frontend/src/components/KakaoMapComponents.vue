<template>
  <div>
    <h1>Maps</h1>
  </div>
</template>

<script setup>



mounted() {
  if (window.kakao && window.kakao.maps) {
    this.initMap();
  } else {
    const script = document.createElement('script');
    /* global kakao */
    script.onload = () => kakao.maps.load(this.initMap);
    script.src =
      'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=카카오API_KEY';
    document.head.appendChild(script);
  }
},



</script>

<style lang="scss" scoped>

</style>