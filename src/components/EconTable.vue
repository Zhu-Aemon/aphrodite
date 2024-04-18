<template>
  <div class="relative overflow-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-black">
      <thead class="text-xl text-black bg-gray-100">
      <tr>
        <th scope="col" class="px-6 py-3">
          经济指标
        </th>
        <th scope="col" class="px-6 py-3" v-for="ind in indicator_symbols">
          {{ indicator_names[ind] }}
        </th>
      </tr>
      </thead>
      <tbody>
      <tr class="bg-white border-b hover:bg-gray-100" v-for="data in countries_en">
        <th scope="row"
            class="px-6 py-4 font-bold text-black whitespace-nowrap select-none">
          {{ countries[data] }}
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

const countries = {'US': '美国', 'CN': '中国', 'EU': '欧洲', 'JP': '日本', 'DE': '德国', 'GB': '英国', 'FR': '法国', 'RU': '俄罗斯',
  'CA':'加拿大', 'IT': '意大利', 'AU': '澳大利亚'}
const indicator_names = {'GDP': 'GDP', 'POP': '人口', 'GDPYY': 'GDP增长率', 'INTR': '利率', 'IRYY': '通货膨胀率', 'UR': '失业率',
  'CAG': '经常账户比GDP', 'GDG': '政府债务比GDP'}
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
      }
    } else {
      return `${econ_data.value[data][ind]["value"]}%`
    }
    if (econ_data.value[data][ind]["value"] === null) {
      return
    }
  }
}
</script>