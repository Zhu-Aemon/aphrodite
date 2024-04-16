<template>
  <div class="relative overflow-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-black">
      <thead class="text-xl text-black bg-gray-100">
      <tr>
        <th scope="col" class="px-6 py-3">
          经济指标
        </th>
        <th scope="col" class="px-6 py-3" v-for="ind in indicator_symbols">
          {{ ind }}
        </th>
      </tr>
      </thead>
      <tbody>
      <tr class="bg-white border-b hover:bg-gray-100" v-for="data in countries_en">
        <th scope="row"
            class="px-6 py-4 font-bold text-black whitespace-nowrap select-none">
          {{ data }}
        </th>
        <td class="px-6 py-1"
        v-for="ind in indicator_symbols">
          <span :class="{'text-black': econ_data[data][ind]['change'] > 0, 'text-red-500': econ_data[data][ind]['change'] < 0}"
          >
            {{ format_digit(data, ind) }}
          </span>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import axios from "axios";
import {onMounted, ref, computed} from "vue";

const countries = ['美国', '中国', '欧洲', '日本', '德国', '英国', '法国', '俄罗斯', '加拿大', '意大利', '澳大利亚']
const indicator_names = ['GDP', '人口', 'GDP增长率', '利率', '通货膨胀率', '失业率', '经常账户比GDP', '政府债务比GDP']
const indicator_symbols = ref()
const econ_data = ref()
const countries_en = ref()

onMounted(async () => {
  const response = await axios.get(`https://api.financialrisk.online/econ_indicators`)
  if (response) {
    econ_data.value = response.data
    countries_en.value = response.data.countries
    indicator_symbols.value = response.data.indicators
  }
})

const format_digit = (data, ind) => {
  if (econ_data.value[data]) {
    if (econ_data.value[data] === null) {
      return
    }
    if (ind === 'GDP') {
      return `${(econ_data.value[data][ind]["value"] / 100000000).toFixed(1)}亿美元`
    } else if (ind === 'POP') {
      if (1000000 > econ_data.value[data][ind]["value"] && econ_data.value[data][ind]["value"] >= 1000) {
        return `${(econ_data.value[data][ind]["value"] / 1000).toFixed(2)}K`
      } else if (1000000000 > econ_data.value[data][ind]["value"] && econ_data.value[data][ind]["value"] >= 1000000) {
        return `${(econ_data.value[data][ind]["value"] / 1000000).toFixed(2)}M`
      } else if (1000000000000 > econ_data.value[data][ind]["value"] && econ_data.value[data][ind]["value"] >= 1000000000) {
        return `${(econ_data.value[data][ind]["value"] / 1000000000).toFixed(2)}B`
      } else {
        console.log(econ_data.value[data][ind]["value"])
        console.log(1000000000 > econ_data.value[data][ind]["value"] >= 1000000)
        return '?'
      }
    } else {
      return `${econ_data.value[data][ind]["value"]}%`
    }
  }
}
</script>