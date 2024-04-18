<template>
  <div class="rounded-2xl py-4 px-4 shadow-md sm:rounded-lg">
    <span>
      <span class="font-bold text-2xl select-none">CPI月率</span>  <span class="ml-2 text-2xl font-medium select-none">{{ new Date().getMonth() + 1 }}月</span>
    </span>
    <div class="mt-8">
      <span class="font-bold text-3xl">同比 {{ display_data }}%</span>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import {onMounted, ref} from "vue";

const data = ref()
const display_data = ref(0)

onMounted(async () => {
  const response = await axios.get(`https://api.financialrisk.online/CPI_monthly`)
  data.value = response.data
  display_data.value = data.value[data.value.length - 1]
})
</script>