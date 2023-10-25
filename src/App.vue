<script setup>
import PerformanceMatrix from "./components/PerformanceMatrix.vue";
import FactorList from "./components/FactorList.vue";
</script>

<template>
  <div class="text-2xl font-bold ml-6 mt-6">机器学习Alpha信号合成可视化系统</div>
  <div class="mt-6 px-20">
    <div class="text-xl font-bold mb-2">因子选择</div>
    <FactorList />
  </div>
  <div class="mt-6 px-20">
    <div class="mb-2 text-xl font-bold">策略信号合成评价</div>
    <PerformanceMatrix />
  </div>
</template>

<style scoped>
</style>
