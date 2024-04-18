<template>
  <div class="rounded-2xl inline-block py-4 px-4 shadow-md sm:rounded-lg mt-4 ml-20">
    <div class="flex">
      <div>
        <svg @click="idxBackward" class="mt-5 cursor-pointer" width="52px" height="52px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M16.1795 3.26875C15.7889 2.87823 15.1558 2.87823 14.7652 3.26875L8.12078 9.91322C6.94952 11.0845 6.94916 12.9833 8.11996 14.155L14.6903 20.7304C15.0808 21.121 15.714 21.121 16.1045 20.7304C16.495 20.3399 16.495 19.7067 16.1045 19.3162L9.53246 12.7442C9.14194 12.3536 9.14194 11.7205 9.53246 11.33L16.1795 4.68297C16.57 4.29244 16.57 3.65928 16.1795 3.26875Z" fill="#0F0F0F"></path> </g></svg>
      </div>
      <div>
        <span>
          <span class="font-bold text-2xl select-none">中国宏观杠杆率</span>  <span class="ml-2 text-2xl font-medium select-none">{{ display_data?.时间 }}</span>
        </span>
        <div v-for="(value, key) in display_data" :key="key">
          <div class="mt-2 flex" v-if="key === Object.keys(display_data)[idx]">
            <svg width="52px" height="52px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M19 9.77806V16.2C19 17.8801 19 18.7202 18.673 19.3619C18.3854 19.9264 17.9265 20.3854 17.362 20.673C16.7202 21 15.8802 21 14.2 21H9.8C8.11984 21 7.27976 21 6.63803 20.673C6.07354 20.3854 5.6146 19.9264 5.32698 19.3619C5 18.7202 5 17.8801 5 16.2V9.7774M21 12L15.5668 5.96393C14.3311 4.59116 13.7133 3.90478 12.9856 3.65138C12.3466 3.42882 11.651 3.42887 11.0119 3.65153C10.2843 3.90503 9.66661 4.59151 8.43114 5.96446L3 12M14 12C14 13.1045 13.1046 14 12 14C10.8954 14 10 13.1045 10 12C10 10.8954 10.8954 9.99996 12 9.99996C13.1046 9.99996 14 10.8954 14 12Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
            <div class="mt-1.5 ml-2">
              <span class="font-medium text-3xl select-none">{{ key }}：</span>
              <span class="text-3xl font-bold select-none">{{ value }}%</span>
            </div>
          </div>
        </div>
    </div>
      <div>
        <svg @click="idxForward" class="mt-5 cursor-pointer" width="52px" height="52px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M7.82054 20.7313C8.21107 21.1218 8.84423 21.1218 9.23476 20.7313L15.8792 14.0868C17.0505 12.9155 17.0508 11.0167 15.88 9.84497L9.3097 3.26958C8.91918 2.87905 8.28601 2.87905 7.89549 3.26958C7.50497 3.6601 7.50497 4.29327 7.89549 4.68379L14.4675 11.2558C14.8581 11.6464 14.8581 12.2795 14.4675 12.67L7.82054 19.317C7.43002 19.7076 7.43002 20.3407 7.82054 20.7313Z" fill="#0F0F0F"></path> </g></svg>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import {onMounted, ref, computed} from "vue";

const data = ref()
const display_data = computed(() => {
  return data.value? data.value[data.value.length - 1]: {}
});
const idx = ref(1)

onMounted(async () => {
  const response = await axios.get(`https://api.financialrisk.online/cnbs`)
  data.value = response.data
})

const idxForward = () => {
  if (idx.value < 8) {
    idx.value += 1
  } else if (idx.value === 8){
    idx.value = 1
  }
}

const idxBackward = () => {
  if (idx.value >= 2) {
    idx.value -= 1
  } else if (idx.value === 1) {
    idx.value = 8
  }
}
</script>