<template>
  <div ref="chartContainer" class="px-20"></div>
</template>

<script setup>
import {createChart} from "lightweight-charts"
import {computed, ref, watch, onMounted} from 'vue'
import {useStore} from "vuex"
import axios from "axios";

const store = useStore()

const current_ft = computed(() => store.state.current_ft)

const chartContainer = ref()
const future_data = ref()

const chart_options = {
  layout: {
    textColor: 'black',
    background: {
      type: 'solid',
      color: 'white'
    }
  },
  height: 500,
  width: 1320,
}

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
  const response = await axios.get(`http://localhost:3628/display?name=${symbol}`)
  if (response) {
    future_data.value = response.data
  }
}
</script>