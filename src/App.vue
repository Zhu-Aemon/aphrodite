<script setup>
import PerformanceMatrix from "./components/PerformanceMatrix.vue";
import FactorList from "./components/FuturesList.vue";
import PriceTable from "./components/PriceTable.vue";
import {useStore} from "vuex";
import {computed} from "vue";
import Chart from "./components/Chart.vue";

const store = useStore()
const current_ft = computed(() => store.state.current_ft)
</script>

<template>
  <div class="text-2xl font-bold ml-6 mt-6">金融风险预测综合屏</div>
  <div class="text-2xl font-bold py-1 ml-8">{{current_ft}}</div>
  <chart />
  <div class="mt-6 px-20 flex">
    <FactorList class="mr-10 drop-shadow-2xl" />
    <div class="w-2/3 h-96 overflow-auto drop-shadow-2xl rounded-b-lg">
      <PriceTable />
    </div>
  </div>
  <div class="mt-6 px-20">
    <div class="mb-2 text-xl font-bold">策略信号合成评价</div>
    <PerformanceMatrix />
  </div>
</template>
