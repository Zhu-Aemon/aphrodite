<template>
  <div ref="chartContainer" class="px-20"></div>
</template>

<script setup>
import {createChart} from "lightweight-charts"
import {computed, ref, watch, onMounted} from 'vue'
import {useStore} from "vuex"
import { useWindowSize } from 'vue-window-size'
import axios from "axios";

const store = useStore()

const current_ft = computed(() => store.state.current_ft)

const chartContainer = ref()
const future_data = ref()
let { width, height } = useWindowSize()

const chart_options = {
  layout: {
    textColor: 'black',
    background: {
      type: 'solid',
      color: 'white'
    }
  },
  height: 500,
  width: width.value > 600 ? width.value - 300 : 300,
}

console.log(width.value)

onMounted(async () => {
  await get_display_data(current_ft.value)
  const chart = createChart(chartContainer.value, chart_options)
  const candleStick = chart.addCandlestickSeries(future_data.value)
  candleStick.setData(future_data.value)
  chart.timeScale().fitContent()
  watch(current_ft, async (oldValue, newValue) => {
    if (oldValue !== newValue) {
      await get_display_data(current_ft.value)
      candleStick.setData(future_data.value)
    }
  })
})

const get_display_data = async (symbol) => {
  const response = await axios.get(`https://api.financialrisk.online/display?name=${symbol}`)
  if (response) {
    future_data.value = response.data
  }
}
</script>