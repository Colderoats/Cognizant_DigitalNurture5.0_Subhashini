<template>
  <div>
    <h2>Product List</h2>

    <input
      v-model="search"
      placeholder="Search product..."
    />

    <ul>
      <li
        v-for="product in filteredProducts"
        :key="product.id"
      >
        {{ product.name }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";

const search = ref("");

const products = ref([
  { id: 1, name: "Laptop" },
  { id: 2, name: "Keyboard" },
  { id: 3, name: "Mouse" },
  { id: 4, name: "Monitor" },
  { id: 5, name: "Phone" }
]);

const filteredProducts = computed(() => {
  return products.value.filter(product =>
    product.name.toLowerCase().includes(search.value.toLowerCase())
  );
});
</script>
