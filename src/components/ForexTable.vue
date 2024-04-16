<template>
  <div class="relative overflow-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-black">
      <thead class="text-sm text-black bg-gray-100">
      <tr>
        <th scope="col" class="px-6 py-3" v-for="field in fields">
          {{ field }}
        </th>
      </tr>
      </thead>
      <tbody>
      <tr class="bg-white border-b hover:bg-gray-100" v-for="data in forex_data">
        <th scope="row"
            class="px-6 py-4 font-medium text-black whitespace-nowrap select-none">
          {{data.Symbol}}
        </th>
        <td class="px-6 py-4">
          {{data.Price.toFixed(3)}}
        </td>
        <td class="px-6 py-4">
          {{data.PercentChange.toFixed(3)}}%
        </td>
        <td class="px-6 py-4">
          {{data.Change.toFixed(3)}}
        </td>
        <td class="px-6 py-4">
          {{data.Bid.toFixed(3)}}
        </td>
        <td class="px-6 py-4">
          {{data.Ask.toFixed(3)}}
        </td>
        <td class="px-6 py-4">
          {{data.High.toFixed(3)}}
        </td>
        <td class="px-6 py-4">
          {{data.Low.toFixed(3)}}
        </td>
        <td class="px-6 py-4 text-red-600 font-bold">
          {{data.TechRating.toFixed(2)}}
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import axios from "axios";
import {onMounted, ref} from "vue";

const fields = ['外汇货币对', '价格', '涨幅', '涨跌额', '买价', '卖价', '最高价', '最低价', '机器学习风险评级']
const forex_data = ref()
const risk_dict = {'Buy': '汇率走高风险', 'Sell': '汇率走低风险', 'Neutral': '短期无风险', 'Strong Buy': '短期汇率走高风险较大', 'Strong Sell': '短期汇率走低风险较大'}

onMounted(async () => {
  const response = await axios.get(`https://api.financialrisk.online/forex`)
  if (response) {
    forex_data.value = response.data
  }
})
</script>