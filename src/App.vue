<script setup>
import PerformanceMatrix from "./components/PerformanceMatrix.vue";
import FuturesList from "./components/FuturesList.vue";
import PriceTable from "./components/PriceTable.vue";
import EconTable from "./components/EconTable.vue";
import {useStore} from "vuex";
import {computed} from "vue";
import {onMounted} from "vue";
import Chart from "./components/Chart.vue";
import axios from "axios";
import ForexTable from "./components/ForexTable.vue";
import ChinaEcon from "./components/ChinaEcon.vue";

let currentDate = new Date();
let year = currentDate.getFullYear();
let month = String(currentDate.getMonth() + 1).padStart(2, '0'); // Month is zero-based, so we add 1
let day = String(currentDate.getDate()).padStart(2, '0');
let dateString = `数据更新时间：${year}年${month}月${day}日`;

const store = useStore()
const current_ft = computed(() => store.state.current_ft_name)
const drop_atype_vis = computed(() => store.state.drop_atype_show)

onMounted(async () => {
  // exec()
  await axios.get(`https://api.financialrisk.online/data_update?name=noname`)
})

const show_selection_menu = () => {
  console.log(drop_atype_vis.value)
  store.commit("change_atype_vis", !drop_atype_vis.value)
}
</script>

<template>
  <div class="text-3xl font-bold ml-6 mt-6">金融风险预测综合屏</div>
  <div class="text-2xl font-bold ml-20 mt-10">
    世界主要经济体实时数据
  </div>
  <div class="text-sm font-medium ml-20 mt-2 text-amber-600">
    {{dateString}}
  </div>
  <EconTable class="mt-2 ml-20 mr-20 drop-shadow-2xl rounded-2xl" />
  <div class="text-red-500 ml-20 mt-2 font-bold text-sm">
    红色标注的内容代表该项和上一期相比出现了负增长
  </div>
  <div class="text-2xl font-bold ml-20 mt-10">
    中国特色经济数据专区
  </div>
  <ChinaEcon class="mt-4 ml-20" />
  <div class="text-2xl font-bold ml-20 mt-6 mb-4">
    <span>国内期货市场走势</span>
    <div class="rounded-lg inline-block bg-blue-200 py-2 px-3 ml-4">当前走势：<span class="text-red-500">{{ current_ft }}</span></div>
  </div>
  <chart />
  <div class="mt-6 px-20 flex">
    <div>
      <div class="text-2xl font-bold mb-2 rounded-2xl py-2 px-3">
        <div class="flex">
          国内期货品种（连续合约）
        </div>
      </div>
      <FuturesList class="mr-10 drop-shadow-2xl h-[400px] overflow-auto"/>
    </div>
    <div>
      <div class="text-2xl font-bold mb-2">
        历史数据浏览器
      </div>
      <PriceTable class="h-[400px] drop-shadow-2xl overflow-auto"/>
    </div>
  </div>
  <div class="text-2xl font-bold ml-20 mt-10">
    人民币汇率实时数据
  </div>
  <div class="text-sm font-medium ml-20 mt-2 text-amber-600">
    {{dateString}}
  </div>
  <ForexTable class="mt-2 ml-20 mr-20 drop-shadow-2xl rounded-2xl mb-20" />
</template>
