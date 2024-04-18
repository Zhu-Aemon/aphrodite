<template>
  <div class="flex">
    <CNBSCard class="mr-14"/>
    <CommodityPriceCard />
    <CNFinancingData class="ml-14" />
    <CNCPI class="ml-14" />
  </div>
  <CNEconChart />
</template>

<script setup>
import {MiniChart} from 'vue-tradingview-widgets';
import CNBSCard from "./CNBSCard.vue";
import CommodityPriceCard from "./CommodityPriceCard.vue";
import CNFinancingData from "./CNFinancingData.vue";
import CNCPI from "./CNCPI.vue";
import CNEconChart from "./CNEconChart.vue";
</script>
