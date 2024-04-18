<template>
  <div class="rounded-2xl py-4 px-4 shadow-md sm:rounded-lg">
    <span>
      <span class="font-bold text-2xl select-none">社会融资规模增量</span>  <span class="ml-2 text-2xl font-medium select-none">{{ display_data?.月份 }}</span>
    </span>
    <div class="mt-8">
      <span class="font-bold text-3xl">{{ display_data['社会融资规模增量'] }}</span>
      <span class="font-medium text-2xl">亿人民币</span>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import {onMounted, ref} from "vue";

const data = ref()
const display_data = ref({
  '社会融资规模增量': 0.0,
})

onMounted(async () => {
  const response = await axios.get(`https://api.financialrisk.online/social_rz`)
  data.value = response.data
  display_data.value = data.value[data.value.length - 1]
})
</script>