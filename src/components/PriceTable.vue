<template>
  <div>
<!--    <div class="text-2xl font-bold mb-2">-->
<!--      历史数据浏览器-->
<!--    </div>-->
    <div class="relative overflow-auto sm:rounded-lg">
      <table class="w-full text-sm text-left text-gray-500 sm:rounded-lg">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3">
            日期
            <div class="cursor-pointer mt-1" @click="downloadData">
              <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512">
                <path
                    d="M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32V274.7l-73.4-73.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l128 128c12.5 12.5 32.8 12.5 45.3 0l128-128c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L288 274.7V32zM64 352c-35.3 0-64 28.7-64 64v32c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V416c0-35.3-28.7-64-64-64H346.5l-45.3 45.3c-25 25-65.5 25-90.5 0L165.5 352H64zm368 56a24 24 0 1 1 0 48 24 24 0 1 1 0-48z"/>
              </svg>
            </div>
          </th>
          <th scope="col" class="px-6 py-3">
            开盘价
          </th>
          <th scope="col" class="px-6 py-3">
            最高价
          </th>
          <th scope="col" class="px-6 py-3">
            最低价
          </th>
          <th scope="col" class="px-6 py-3">
            收盘价
          </th>
          <th scope="col" class="px-6 py-3">
            交易量
          </th>
          <th scope="col" class="px-6 py-3">
            库存
          </th>
        </tr>
        </thead>
        <tbody>
        <tr class="bg-white border-b hover:bg-gray-50" v-for="price in futures_data">
          <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
            {{ price.time.slice(0, 10) }}
          </th>
          <td class="px-6 py-4">
            {{ price.open }}
          </td>
          <td class="px-6 py-4">
            {{ price.high }}
          </td>
          <td class="px-6 py-4">
            {{ price.low }}
          </td>
          <td class="px-6 py-4">
            {{ price.close }}
          </td>
          <td class="px-6 py-4">
            {{ price.vol }}
          </td>
          <td class="px-6 py-4">
            {{ price.inventory }}
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import axios from "axios"
import {computed, onMounted, ref, watch} from "vue"
import {useStore} from "vuex"
import {Parser} from '@json2csv/plainjs'

const store = useStore()

const current_ft = computed(() => store.state.current_ft)
const futures_data = ref()

onMounted(async () => {
  await get_future_data(current_ft.value)
  watch(current_ft, (newValue, oldValue) => {
    if (newValue !== oldValue) {
      get_future_data(current_ft.value)
    }
  })
})

const get_future_data = async (symbol) => {
  const response = await axios.get(`https://api.financialrisk.online/cn_futures?name=${symbol}`)
  if (response) {
    futures_data.value = response.data
  }
}

const downloadData = async () => {
  await axios.get(`https://api.financialrisk.online/cn_futures?name=${current_ft.value}`, {responseType: 'text'})
      .then(response=> {
        const obj = JSON.parse(response.data)
        const parser = new Parser()
        const csv = parser.parse(obj)
        const blob = new Blob([csv], {type: 'text/csv'})
        const link = document.createElement('a')
        link.href = URL.createObjectURL(blob)
        link.download = `${current_ft.value}.csv`
        link.click()
        URL.revokeObjectURL(link.href)
      })

}

</script>