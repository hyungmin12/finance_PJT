<template>
  <div>
    <div id="carouselExampleControls">
      <div class="carousel-inner all_box ">
        <div class="carousel-item active">
          <img src="src/assets/images/bg.jpg">
          <div class="ani_box">
            <img src="src/assets/images/moneychange.png" alt="" class="ani_img">
            <p class="slogan">
              <strong>환율 계산</strong>
            </p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <FinanceComponent />
    </div>
  </div>
    <div class="exchange-calculator" style="margin-top: 30px; margin-bottom: 30px;">
      <h1>환율 계산기</h1>
      <p v-if="rate === -1">현재 통화 선택이 유효하지 않습니다.</p>
      <!-- <p>{{ isNumeric(output_money) ? output_money.toFixed(2) : output_money }}</p> -->
      <p v-else-if="rate">현재 환율은 {{ isNumeric((currencyUnit / rate)) ?  (currencyUnit / rate).toFixed(2) : (currencyUnit / rate) }}입니다.</p>
      <p v-else>두 통화를 선택해주세요.</p>
      <div class="currency-selection">
        <select v-model="select1">
          <option v-for="payment in payments" :key="payment" :value="payment">
            {{ country[payment] }}
          </option>
        </select>
        :
        <input type="text" v-model.number="input_money" style="margin-left: 7px;">
      </div>
      <div class="currency-selection">
        <select v-model="select2">
          <option v-for="payment in payments" :key="payment" :value="payment">
            {{ country[payment] }}
          </option>
        </select>
        <button @click="calculate" class="btn btn-outline-secondary">계산</button>
      </div>
      <p>{{ formatNumber(output_money) }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from "vue";
  import axios from "axios";
  // prettier-ignore
  const payments = ref(["KRW", "USD","JPY","CNY", "EUR", "TWD", "VND", "GBP","CHF","CAD","AUD","HKD","SEK","NZD", "SGD","NOK","MXN","INR","RUB","ZAR","TRY","BRL","AED","BHD","BND","CNH","CZK","DKK","IDR","ILS","MYR","QAR","SAR","THB","CLP","COP","EGP","HUF","KWD","OMR","PHP","PLN","PKR","RON", "BDT","DZD","ETB","FJD","JOD","KES","KHR","KZT","LKR","LYD","MMK","MNT","MOP","NPR","TZS","UZS",
    ]);
  const country = ref({"KRW" : "한국 원", "USD" : "US 달러", "JPY" : "일본 엔", "CNY" : "중국 위안", "EUR" : "유로","TWD" : '대만 대만달러',"VND" : '베트남 동', "GBP" : "영국 파운드","CHF" : '스위스 프랑',"CAD" : '캐나디안 달러',"AUD" : "오스트레일리아 달러","HKD" : '홍콩 달러',"SEK": '스웨덴 크로나',"NZD" : "뉴질랜드 달러", "SGD" : '싱가포르 달러',"NOK" : '노르웨이 크로네',"MXN" : '멕시코 페소',"INR" : '인디안 루피',"RUB" : '러시아 루블',"ZAR" : '남아공 랜드',"TRY" : '터키 리라',"BRL" : '브라질리안 헤알',"AED" : '아랍에미리트 디르함',"BHD" : '바레인 디나르',"BND" : '브루나이 달러',"CNH" : '역외 중국 위안',"CZK":'체코 코루나',"DKK" : '덴마크 크로네',"IDR" : '인도네시아 루피아',"ILS" : '이스라엘 셰켈',"MYR": '말레이시아 링겟',"QAR" : '카타르 리알',"SAR" : '사우디 리알',"THB" : '태국 바트',"CLP" : '칠레 페소',"COP" : '콜롬비아 페소',"EGP" : '이집트 파운드',"HUF": '헝가리 포린트',"KWD" : '쿠웨이트 디나르',"OMR" : '오만 리알',"PHP" : '필리핀 페소',"PLN" : '폴란드 즐로티',"PKR": '파키스탄 루피',"RON" : '루마니아 레우',"BDT" : '방글라데쉬 타카',"DZD" : '알제리 디나르',"ETB": '에디오피아 디르',"FJD" : '피지 달러',"JOD" : '요르단 디나르',"KES" : '케냐 실링',"KHR" : '캄보디아 릴',"KZT" : '카자흐스탄 텡게',"LKR" : '스리랑카 루피',"LYD" : '리비아 디나르',"MMK" : '미얀마 차트',"MNT" : '몽골 투그리크',"MOP" : '마카오 파타카',"NPR" : '네팔 루피',"TZS" : '탄자니아 실링',"UZS" : '우즈베키스탄 숨',});
  
  const select1 = ref(null);
  const select2 = ref(null);
  
  
  
  const formatNumber = function (value) {
    if (isNumeric(value)) {
      return value.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    } else {
      return value;
    }
  };
  
  // 두 환율 옵션이 선택되었을 때에 환율 금액 정보 가져오기
  const isNumeric = function (value) {
    return typeof value === 'number' && !isNaN(value);
  };
  
  watch([select1, select2], ([newOption1, newOption2]) => {
    if (newOption1 !== null && newOption2 !== null) {
      if (newOption1 == 'KRW') {
        axios({
          url: `https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW${newOption2}`,
          method: "GET",
        })
          .then(({ data }) => {
            rate.value = data[0]?.basePrice || -1;
            currencyUnit.value = data[0]?.currencyUnit || 1;
          })
          .catch((err) => console.log(err));
        }
      else if (newOption2 == 'KRW') {
        axios({
          url: `https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW${newOption1}`,
          method: "GET",
        })
          .then(({ data }) => {
            rate.value = 1 / data[0]?.basePrice || -1;
            currencyUnit.value = 1 / data[0]?.currencyUnit || 1;
          })
          .catch((err) => console.log(err));
        }
      else {
        let rate1 = -1
        let rate2 = -1
        let cunit1 = -1
        let cunit2 = -1
        axios({
          url: `https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW${newOption1}`,
          method: "GET",
        })
        .then(({ data }) => {
          rate1 = data[0]?.basePrice || -1;
          cunit1 = data[0]?.currencyUnit || 1;
        })
        .catch((err) => console.log(err));
        axios({
          url: `https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW${newOption2}`,
          method: "GET",
        })
        .then(({ data }) => {
          rate2 = data[0]?.basePrice || -1;
          cunit2 = data[0]?.currencyUnit || 1;
          rate.value = rate2/rate1
          currencyUnit.value = cunit2/cunit1
        })
        .catch((err) => console.log(err));
      }}});
  
  const input_money = ref(0);
  const output_money = ref(0);
  
  const calculate = function () {
    output_money.value = input_money.value / rate.value * currencyUnit.value
  }
  
  const rate = ref(null);
  const currencyUnit = ref(null);
  
  
  </script>
  <style scoped>
  .exchange-calculator {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .currency-selection {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  select {
    flex: 1;
    margin-right: 10px;
    height: 30px;
  }
  
  input {
    flex: 1;
    height: 30px;
  }
  
  p {
    margin-top: 10px;
    font-size: 18px;
  }
  .slogan {
  margin-bottom: 50px;
  line-height: 1.4;
  margin-top: 160px;
  }
  .ani_img{
  width: 400px;
  height: 300px;
  margin-bottom: 50px;
  }
  </style>