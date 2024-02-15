<script setup>
import PerformanceMatrix from "./components/PerformanceMatrix.vue";
import FuturesList from "./components/FuturesList.vue";
import PriceTable from "./components/PriceTable.vue";
import {useStore} from "vuex";
import {computed} from "vue";
import {onMounted} from "vue";
import Chart from "./components/Chart.vue";
import axios from "axios";

const store = useStore()
const current_ft = computed(() => store.state.current_ft_name)
onMounted(async () => {
  // exec()
  await axios.get(`http://localhost:3628/data_update?name=noname`)
})
</script>

<template>
  <div class="text-3xl font-bold ml-6 mt-6">金融风险预测综合屏</div>
  <div class="text-2xl font-bold ml-8 inline-block rounded-lg py-2 px-3 bg-blue-200 mt-2 mb-4">当前走势：<span class="text-red-500">{{ current_ft }}</span></div>
  <chart />
  <div class="mt-6 px-20 flex">
    <FuturesList class="mr-10 drop-shadow-2xl h-[400px] overflow-auto"/>
    <div class="h-[400px] w-2/3 drop-shadow-2xl rounded-b-lg overflow-auto">
      <PriceTable/>
    </div>
  </div>
  <div class="mt-6 px-20">
    <div class="mb-2 text-xl font-bold">策略信号合成评价</div>
    <PerformanceMatrix />
  </div>
</template>
