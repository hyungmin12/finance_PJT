<template>
    <tr>
        <td style="text-align: center;">{{ saving.kor_co_nm }}</td>
        <td style="text-align: center;">{{ saving.fin_prdt_nm }}</td>
        <td style="text-align: center;">
            <button @click="toggleDetails">Toggle Details</button>
        </td>
    </tr>
    <td colspan="3">
        <div v-if="isShow" style="display: inline-block; width:100%;">
            <div class="d-flex">
                
            </div>
            <div v-for="option of saving.options" :key="option.save_trm">
        <hr>
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
</td>
</template>

<script setup>
    import { ref } from 'vue'
    const isShow = ref(false)
    defineProps({
        saving:Object
    })
    const toggleDetails = () => {
    // showDetails.value[depositId] = !showDetails.value[depositId];
    if (isShow.value) {
        isShow.value = false
    } else {
        isShow.value = 1
    }
    };
</script>

<style scoped>

</style>