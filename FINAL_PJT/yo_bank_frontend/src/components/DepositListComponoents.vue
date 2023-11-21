<!-- <template>
  <div>
    <h1>depositListComponent</h1>
    <div v-for="deposit of store.changeDeposits" :key="deposit.id">
      <p>금융기관 : {{ deposit.kor_co_nm }}</p>
      <p>상품 : {{ deposit.fin_prdt_nm }}</p>
      <p>{{ deposit.spcl_cnd }}</p>
      <p>{{ deposit.etc_note }}</p>
      <button @click="toggleDetails(deposit.id)">Toggle Details</button>
      <div v-if="showDetails[deposit.id]">
        <div v-for="option of deposit.options" :key="option.save_trm">
          <hr />
          <p>예치기간 : {{ option.save_trm }}</p>
          <p>저축금리 : {{ option.intr_rate }}</p>
          <p>우대금리 : {{ option.intr_rate2 }}</p>
          <button @click="signUpThisProduct(option.id)">가입하기</button>
        </div>
        <hr />
      </div>
    </div> 
  </div>
</template> -->

<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>금융기관</th>
          <th>상품</th>
          <th>자세히 보기</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="deposit of store.changeDeposits" :key="deposit.id">
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
            <button @click="toggleDetails(deposit.id)">Toggle Details</button>
              <div v-if="showDetails[deposit.id]">
                <div v-for="option of deposit.options" :key="option.save_trm">
                  <hr />
                  <table>
                    <thead>
                      <tr>
                        <th>금융기관</th>
                        <th>상품</th>
                        <th>자세히 보기</th>
                      </tr>
                    </thead>
                    <td>예치기간 : {{ option.save_trm }}</td>
                    <td>저축금리 : {{ option.intr_rate }}</td>
                    <td>우대금리 : {{ option.intr_rate2 }}</td>
                  </table>
                  <form @submit.prevent="signUpThisProduct(option.id)">
                    <input v-model="amount" type="text">
                    <button>가입하기</button>
                    <input type="submit">
                  </form>
                </div>
              </div>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<!-- "fin_co_no": "0010024",
"fin_prdt_cd": "21001203",
"kor_co_nm": "경남은행",
"fin_prdt_nm": "BNK주거래우대정기예금",
"join_deny": 1,
"join_member": "개인 및 개인사업자",
"join_way": "인터넷,스마트폰",
"spcl_cnd": "①급여,연금,가맹점대금 중 한 종류 입금할 경우 0.10%\n②당행 신용/체크카드 결제실적 보유할 경우 0.10%\n③가입일 기준 6개월이내 당행 정기예금 미보유 신규 고객인 경우 0.10%",
"max_limit": 500000000,
"etc_note": "1. 이 예금의 계약기간은 6개월, 1년, 2년으로 한다.\n2. 가입좌수 제한없으며 가입금액은 최소 1백만원 이상 최고 5억원 이하이다.",
"dcls_end_day": null
},
{
"id": 514,
"options": [
    {
        "id": 1406,
        "intr_rate_type": "S",
        "intr_rate_type_nm": "단리",
        "save_trm": 12,
        "intr_rate": 3.45,
        "intr_rate2": 3.65,
        "deposit_product": "01211310121"
    }, -->
<script setup>
import { ref } from "vue";
import { useProductStore } from "@/stores/product.js";
import { useCounterStore } from "@/stores/counter.js";
import axios from "axios";

const store = useProductStore();
const store2 = useCounterStore();
const showDetails = ref({});
const token = store2.token;
const amount = ref(null)

const toggleDetails = (depositId) => {
  showDetails.value[depositId] = !showDetails.value[depositId];
};

const signUpThisProduct = function (optionPk) {
  axios({
    method: "POST",
    url: `http://127.0.0.1:8000/financial_data/signup_deposit/${optionPk}`,
    headers: {
      Authorization: `Token ${token}`,
    },
    data : {
      amount : amount.value
    }
  })
  .then((res) => {
    console.log(res.data);
  })
  .catch((err) => {
    console.log(err);
  });
};
</script>

<style lang="scss" scoped>
/* 필요한 스타일링을 추가할 수 있습니다. */
table {
  border-collapse: collapse;
  width: 90%;
  margin: 1rem auto;
  background-color: white;
}

/* 테이블 행 */
th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  text-align: center;
}

th {
  background-color: #1b1b1b;
  color: #ddd;
}

/* 테이블 올렸을 때 */
tbody tr:hover {
  background-color: #d3d3d3;
  opacity: 0.9;
  cursor: pointer;
}

/* 테이블 비율 */
th:nth-child(1),
td:nth-child(1) {
  width: 15%;
}

th:nth-child(2),
td:nth-child(2) {
  width: 55%;
}

th:nth-child(3),
td:nth-child(3) {
  width: 30%;
}

tr:nth-child(even) {
  background-color: #fff6f6;
}
</style>
