<template>
  <div class="font-bold text-2xl mt-6 ml-20">
    中国M1与M2货币增速剪刀差
  </div>
  <div class="ml-40 mt-8">
    <VueApexCharts type="area" height="600" width=1500
                   :options="{
                      chart: {
                        height: 600,
                        type: 'area'
                      },
                      xaxis: {
                        categories: dates
                      },
                      dataLabels: {
                        enabled: false
                      },
                      stroke: {
                        curve: 'smooth'
                      },
                      tooltip: {
                        x: {
                          format: 'dd/MM/yy HH:mm'
                        },
                      }
                    }"
                   :series="[{
                        name: '货币(M1)-同比增长', data: m1Growth
                      }, {
                        name: '货币和准货币(M2)-同比增长', data: m2Growth
                      }]"/>
  </div>
</template>

<script setup>
import VueApexCharts from 'vue3-apexcharts'
import { useWindowSize } from 'vue-window-size'
import {onMounted, ref} from "vue";
import axios from "axios";

const MS_data = ref()
const dates = ref([])
const m1Growth = ref([])
const m2Growth = ref([])
// let { width, height } = useWindowSize()
// const chartWidth = ref(width - 300)

onMounted(async () => {
  const response_MS = await axios.get(`https://api.financialrisk.online/money_supply`)
  MS_data.value = response_MS.data
  dates.value = MS_data.value.map(item => item.date);
  m2Growth.value = MS_data.value.map(item => item.value["货币和准货币(M2)-同比增长"]);
  m1Growth.value = MS_data.value.map(item => item.value["货币(M1)-同比增长"]);
  console.log(dates.value, m1Growth.value, m2Growth.value)
})
</script>