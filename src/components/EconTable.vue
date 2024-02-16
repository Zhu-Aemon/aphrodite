<template>
  <div class="relative overflow-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-gray-500">
      <thead class="text-xl text-black bg-gray-100">
      <tr>
        <th scope="col" class="px-6 py-3">
          经济指标
        </th>
        <th scope="col" class="px-6 py-3" v-for="country in countries">
          {{ country }}
        </th>
      </tr>
      </thead>
      <tbody>
      <tr class="bg-white border-b hover:bg-gray-100" v-for="data in econ_data">
        <th scope="row"
            class="px-6 py-4 font-bold text-black whitespace-nowrap select-none">
          {{ indicator_names[econ_data.indexOf(data)] }}
        </th>
        <td class="px-6 py-4">
          {{ data.US }}
        </td>
        <td class="px-6 py-4">
          {{ data.CN }}
        </td>
        <td class="px-6 py-4">
          {{ data.EU }}
        </td>
        <td class="px-6 py-4">
          {{ data.JP }}
        </td>
        <td class="px-6 py-4">
          {{ data.DE }}
        </td>
        <td class="px-6 py-4">
          {{ data.GB }}
        </td>
        <td class="px-6 py-4">
          {{ data.FR }}
        </td>
        <td class="px-6 py-4">
          {{ data.RU }}
        </td>
        <td class="px-6 py-4">
          {{ data.CA }}
        </td>
        <td class="px-6 py-4">
          {{ data.IT }}
        </td>
        <td class="px-6 py-4">
          {{ data.AU }}
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import axios from "axios";
import {onMounted, ref} from "vue";

const countries = ['美国', '中国', '欧洲', '日本', '德国', '英国', '法国', '俄罗斯', '加拿大', '意大利', '澳大利亚']
const indicator_names = ['GDP', '人口', 'GDP增长率', '利率', '通货膨胀率', '失业率', '经常账户比GDP', '政府债务比GDP']
const econ_data = ref()

onMounted(async () => {
  let currentDate = new Date();
  let year = currentDate.getFullYear();
  let month = String(currentDate.getMonth() + 1).padStart(2, '0'); // Month is zero-based, so we add 1
  let day = String(currentDate.getDate()).padStart(2, '0');
  let dateString = `${year}_${month}_${day}`;
  console.log(dateString)
  const response = await axios.get(`http://localhost:3628/econ_indicators?date=${dateString}`)
  if (response) {
    econ_data.value = response.data
  }
})
</script>