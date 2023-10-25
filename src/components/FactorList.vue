<template>
  <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-gray-500">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50">
      <tr>
        <th scope="col" class="p-4">
          <div class="flex items-center">
            <input id="checkbox-all-search" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2">
            <label for="checkbox-all-search" class="sr-only">checkbox</label>
          </div>
        </th>
        <th scope="col" class="px-6 py-3">
          因子名称
        </th>
        <th scope="col" class="px-6 py-3">
          因子类型
        </th>
        <th scope="col" class="px-6 py-3">
          因子IC
        </th>
        <th scope="col" class="px-6 py-3">
          因子Sharpe
        </th>
        <th scope="col" class="px-6 py-3">
          因子暴露显著性
        </th>
      </tr>
      </thead>
      <tbody>
      <tr class="bg-white border-b hover:bg-gray-50">
        <td class="w-4 p-4">
          <div class="flex items-center">
            <input id="checkbox-table-search-1" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2">
            <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
          </div>
        </td>
        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
          乖离度
        </th>
        <td class="px-6 py-4">
          动量
        </td>
        <td class="px-6 py-4">
          0.5
        </td>
        <td class="px-6 py-4">
          1.1
        </td>
        <td class="px-6 py-4">
          始终显著大于0
        </td>
      </tr>
      </tbody>
    </table>
    <nav class="flex items-center justify-between pt-4 relative mb-2" aria-label="Table navigation">
      <span class="text-sm font-normal text-gray-500 ml-4">Showing <span class="font-semibold text-gray-900">1-10</span> of <span class="font-semibold text-gray-900">1000</span></span>
      <ul class="inline-flex -space-x-px text-sm h-8 mr-2">
        <li>
          <a href="#" class="flex items-center justify-center px-3 h-8 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700">Previous</a>
        </li>
        <li>
          <a href="#" class="flex items-center justify-center px-3 h-8 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700">1</a>
        </li>
        <li>
          <a href="#" class="flex items-center justify-center px-3 h-8 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700">2</a>
        </li>
        <li>
          <a href="#" class="flex items-center justify-center px-3 h-8 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700">Next</a>
        </li>
      </ul>
    </nav>
  </div>

</template>

<scirpt setup>

</scirpt>
<script setup>
</script>