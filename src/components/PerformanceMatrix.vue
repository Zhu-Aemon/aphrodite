<template>
 <div class="overflow-x-auto relative rounded-[5px]">
   <table class="w-full text-sm text-left text-gray-500">
     <thead class="text-xs text-gray-700 uppercase bg-gray-50">
     <tr>
       <th scope="col" class="px-6 py-3">
         信号合成模型
       </th>
       <th scope="col" class="px-6 py-3">
         年化收益率
       </th>
       <th scope="col" class="px-6 py-3">
         夏普比率
       </th>
       <th scope="col" class="px-6 py-3">
         年化波动率
       </th>
       <th scope="col" class="px-6 py-3">
         最大回撤
       </th>
       <th scope="col" class="px-6 py-3">
         卡玛比率
       </th>
     </tr>
     </thead>
     <tbody>
     <tr class="border-b">
       <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
         多元线性模型
       </th>
       <td class="px-6 py-4">
         18%
       </td>
       <td class="px-6 py-4">
         2.12
       </td>
       <td class="px-6 py-4">
         7.78%
       </td>
       <td class="px-6 py-4">
         3.2%
       </td>
       <td class="px-6 py-4">
         5.625
       </td>
     </tr>
     <tr class="border-b">
       <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
         闵氏度规KNN分类模型
       </th>
       <td class="px-6 py-4">
         18%
       </td>
       <td class="px-6 py-4">
         2.12
       </td>
       <td class="px-6 py-4">
         7.78%
       </td>
       <td class="px-6 py-4">
         3.2%
       </td>
       <td class="px-6 py-4">
         5.625
       </td>
     </tr>
     <tr class="border-b">
       <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
         CatBoost
       </th>
       <td class="px-6 py-4">
         18%
       </td>
       <td class="px-6 py-4">
         2.12
       </td>
       <td class="px-6 py-4">
         7.78%
       </td>
       <td class="px-6 py-4">
         3.2%
       </td>
       <td class="px-6 py-4">
         5.625
       </td>
     </tr>
     <tr class="border-b">
       <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
         BP神经网络
       </th>
       <td class="px-6 py-4">
         18%
       </td>
       <td class="px-6 py-4">
         2.12
       </td>
       <td class="px-6 py-4">
         7.78%
       </td>
       <td class="px-6 py-4">
         3.2%
       </td>
       <td class="px-6 py-4">
         5.625
       </td>
     </tr>
     </tbody>
   </table>
 </div>
</template>

<script setup>

</script>