<template>
  <div>
    <div>
      <div class="search-bar d-flex">
        <input class="search-input" v-model="searchKeyword" placeholder="주소를 검색하세요" />
        <button @click="search" class="d-flex btn btn-primary search-button " ><span class="align-middle">검색</span></button>
      </div>
    </div>
    <div ref="map" style="width: 100%; height: 100vh;"></div>
    <div style="z-index: 9;" class="search-div p-4" v-if="searchedBanks.length > 0">
      <h2 class="m-3">검색된 은행</h2>
      <ul>
        <li class="fw-bold m-2" v-for="bank in searchedBanks" :key="bank.id">
          {{ bank.place_name }} - {{ bank.address_name }} 
        </li>
      </ul>
    </div>
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      map: null,
      infowindow: null,
      searchKeyword: '',
      searchKeyword2: '',
      searchedBanks: [],
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

        // 검색 결과 초기화
        this.searchedBanks = [];

        const ps = new window.kakao.maps.services.Places(this.map);
        ps.categorySearch('BK9', this.placesSearchCB, { useMapBounds: true });
      } else {
        alert('주소 검색 실패');
      }
    });
  }
},
    placesSearchCB(data, status, pagination) {
  if (status === window.kakao.maps.services.Status.OK) {
    const bounds = new window.kakao.maps.LatLngBounds();

    for (let i = 0; i < data.length; i++) {
      const coords = new window.kakao.maps.LatLng(data[i].y, data[i].x);
      this.displayMarker(coords, data[i]);
      bounds.extend(coords);

      this.searchedBanks.push({
        id: data[i].id,
        place_name: data[i].place_name,
        address_name: data[i].address_name,
      });
    }

    this.map.setBounds(bounds);
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
            '<p>'+data.place_name + data.address_name + '</p>' +
            // data.road_address_name+
          '</div>'
        );
        console.log(data)
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
/* .search-button {
  position: absolute;
  border: 1px solid black;
  right: 0px;
  height: 40px;
  width: 100px;
} */

.search-bar {
  z-index: 3;
  position: absolute;
  top: 12%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.search-div{
  background-color: hsla(0, 0%, 100%, 0.8);
  position: absolute;
  top: 60%;
  left: 18%;
  /* opacity: 50%; */
  height: 100vh;
  transform: translate(-50%, -50%);
}

.search-input {
  position: relative;
  border: 1px solid black;
  width: 400px;
  height: 40px;
}

.search-button {
  position: absolute;
  border: 1px solid black;
  right: 0px;
  height: 40px;
  width: 100px;
  display: flex;
  align-items: center; /* 텍스트를 세로로 가운데 정렬 */
}

.align-middle {
  margin: auto; /* 텍스트를 가로로 가운데 정렬 */
}
</style>
