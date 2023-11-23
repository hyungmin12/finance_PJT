<!-- <template>
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
        <tr v-for="deposit of store.changeSavings" :key="deposit.id">
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
                  <form @submit.prevent="signUpThisSaving(option.id)">
                    <input v-model="amount" type="text">
                    <input type="submit" value="가입하기">
                  </form>
                </div>
              </div>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script setup>
import { ref } from "vue";
import { useSavingStore } from "@/stores/saving.js";
import { useCounterStore } from "@/stores/counter.js";
import axios from "axios";

const store = useSavingStore();
const store2 = useCounterStore();
const showDetails = ref({});
const token = store2.token;
const amount = ref(null)

const toggleDetails = (depositId) => {
  showDetails.value[depositId] = !showDetails.value[depositId];
};

const signUpThisSaving = function (optionPk) {
  axios({
    method: "POST",
    url: `http://127.0.0.1:8000/financial_data/signup_saving/${optionPk}`,
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
</style> -->

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
        <Savingdetail
        v-for="saving of store.changeSavings" :key="saving.id"
        :saving="saving"
        />
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useSavingStore } from "@/stores/saving.js";
import { useCounterStore } from "@/stores/counter.js";
import axios from "axios";
import Savingdetail from "@/components/Savingdetail.vue";

const store = useSavingStore();
const store2 = useCounterStore();
const showDetails = ref({});
const token = store2.token;
const amount = ref(null)


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
</style>