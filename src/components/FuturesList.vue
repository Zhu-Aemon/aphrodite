<template>
  <div class="w-1/3 h-96 relative overflow-x-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-gray-500">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50">
      <tr>
        <th scope="col" class="px-6 py-3">
          期货名称
        </th>
        <th scope="col" class="px-6 py-3">
          期货Symbol
        </th>
        <th scope="col" class="px-6 py-3">
          交易所
        </th>
      </tr>
      </thead>
      <tbody>
      <tr class="bg-white border-b hover:bg-gray-50" v-for="future in future_list">
        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap cursor-pointer hover:underline hover:text-blue-500 select-none" @dblclick="ft_dblClicked(future.symbol)">
          {{future.name}}
        </th>
        <td class="px-6 py-4">
          {{future.symbol}}
        </td>
        <td class="px-6 py-4">
          {{future.exchange}}
        </td>
      </tr>
      </tbody>
    </table>
  </div>

</template>

<script setup>
import axios from 'axios'
import {onMounted, onUnmounted, ref, computed} from "vue"
import {useStore} from "vuex"

const store = useStore()

const future_list = ref()

const current_ft = computed(() => store.state.current_ft)

onMounted(async () => {
  await get_all_futures()
})

const get_all_futures = async () => {
  const response = await axios.get(`http://localhost:3628/all_cn_futures?name=futures`)
  if (response) {
    future_list.value = response.data
  }
}

const ft_dblClicked = (future) => {
  store.commit('update_current_ft', future)
}
</script>