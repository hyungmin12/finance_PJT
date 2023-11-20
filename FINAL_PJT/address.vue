<template>
  <div>
    <div>
      <input v-model="searchKeyword" placeholder="은행을 검색하세요" />
      <button @click="search">검색</button>
    </div>
    <div ref="map" style="width: 100%; height: 350px;"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      map: null,
      infowindow: null,
      searchKeyword: '',
    };
  },
  mounted() {
    this.infowindow = new window.kakao.maps.InfoWindow({ zIndex: 1 });
    const mapContainer = this.$refs.map;
    const mapOption = {
      center: new window.kakao.maps.LatLng(37.566826, 126.9786567),
      level: 3,
    };
    this.map = new window.kakao.maps.Map(mapContainer, mapOption);
    this.setupGeolocation();
  },
  methods: {
    setupGeolocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
          const lat = position.coords.latitude;
          const lon = position.coords.longitude;
          const locPosition = new window.kakao.maps.LatLng(lat, lon);
          const message = '<div style="padding:5px;">여기에 계신가요?!</div>';

          if (this.map) {
            this.displayMarker(locPosition, message);
          } else {
            console.error('지도가 정의되어 있지 않습니다.');
          }
        });
      } else {
        const locPosition = new window.kakao.maps.LatLng(37.566826, 126.9786567);
        const message = 'geolocation을 사용할 수 없어요..';
        this.displayMarker(locPosition, message);
      }
    },
    search() {
      if (this.searchKeyword) {
        const geocoder = new window.kakao.maps.services.Geocoder();
        geocoder.addressSearch(this.searchKeyword, (result, status) => {
          if (status === window.kakao.maps.services.Status.OK) {
            const coords = new window.kakao.maps.LatLng(result[0].y, result[0].x);
            this.clearMarkers(); // 기존 마커 제거
            this.displayMarker(coords, result[0]);
            this.map.setCenter(coords); // 지도의 중심을 결과값으로 받은 위치로 이동
          } else {
            alert('주소 검색 실패');
          }
        });
      }
    },
    displayMarker(place, data) {
      const marker = new window.kakao.maps.Marker({
        map: this.map,
        position: place,
      });

      window.kakao.maps.event.addListener(marker, 'click', () => {
        this.infowindow.setContent(
          '<div style="padding:5px;font-size:12px;">' +
            data.address_name +
            '</div>'
        );
        this.infowindow.open(this.map, marker);
      });

      if (!this.map.markers) {
        this.map.markers = []; // markers가 정의되어 있지 않으면 초기화
      }

      this.map.markers.push(marker); // 마커를 배열에 추가
    },
    clearMarkers() {
      // 지도에 표시된 마커들을 모두 제거
      if (this.map.markers) {
        this.map.markers.forEach((marker) => {
          marker.setMap(null);
        });
        this.map.markers = [];
      }
    },
  },
};
</script>

<style scoped>
/* 필요한 스타일이 있다면 여기에 추가하세요 */
</style>
