<template>
  <div class="rounded-2xl py-4 px-4 shadow-md sm:rounded-lg">
    <span>
      <span class="font-bold text-2xl select-none">企业商品价格指数</span>  <span class="ml-2 text-2xl font-medium select-none">{{ display_data?.月份 }}</span>
    </span>
    <table class="relative mt-2">
      <tr>
        <td class="px-3 py-1">
          <span class="font-medium text-2xl">总指数：</span>
          <span class="font-bold text-2xl">{{display_data['总指数-指数值']}}</span>
          <span v-if="display_data['总指数-同比增长'] > 0"> +</span>
          <span :class="{'text-red-500': display_data['总指数-同比增长'] < 0, 'text-black-800': display_data['总指数-同比增长'] >= 0}">{{display_data['总指数-同比增长'].toFixed(1)}}%</span>
        </td>
        <td class="px-3 py-1">
          <span class="font-medium text-2xl">农产品：</span>
          <span class="font-bold text-2xl">{{display_data['农产品-指数值']}}</span>
          <span v-if="display_data['农产品-同比增长'] > 0"> +</span>
          <span :class="{'text-red-500': display_data['农产品-同比增长'] < 0, 'text-black-800': display_data['农产品-同比增长'] >= 0}">{{display_data['农产品-同比增长'].toFixed(1)}}%</span>
        </td>
      </tr>
      <tr>
        <td class="px-3 py-1">
          <span class="font-medium text-2xl">煤油电：</span>
          <span class="font-bold text-2xl">{{display_data['煤油电-指数值']}}</span>
          <span v-if="display_data['煤油电-同比增长'] > 0"> +</span>
          <span :class="{'text-red-500': display_data['煤油电-同比增长'] < 0, 'text-black-800': display_data['煤油电-同比增长'] >= 0}">{{display_data['煤油电-同比增长'].toFixed(1)}}%</span>
        </td>
        <td class="px-3 py-1">
          <span class="font-medium text-2xl">矿产品：</span>
          <span class="font-bold text-2xl">{{display_data['矿产品-指数值']}}</span>
          <span v-if="display_data['矿产品-同比增长'] > 0"> +</span>
          <span :class="{'text-red-500': display_data['矿产品-同比增长'] < 0, 'text-black-800': display_data['矿产品-同比增长'] >= 0}">{{display_data['矿产品-同比增长'].toFixed(1)}}%</span>
        </td>
      </tr>
    </table>
  </div>
</template>

<script setup>
import axios from "axios";
import {onMounted, ref} from "vue";

const data = ref()
const display_data = ref({
  '总指数-指数值': 0.0,
  '总指数-同比增长': 0.0,
  '农产品-指数值': 0.0,
  '农产品-同比增长': 0.0,
  '煤油电-指数值': 0.0,
  '煤油电-同比增长': 0.0,
  '矿产品-指数值': 0.0,
  '矿产品-同比增长': 0.0,
})

onMounted(async () => {
  const response = await axios.get(`https://api.financialrisk.online/commodity_price`)
  data.value = response.data
  display_data.value = data.value[0]
})
</script>