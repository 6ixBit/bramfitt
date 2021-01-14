<template>
  <div class="container">
    <table class="table-auto">
      <thead>
        <tr>
          <th class="table-header">Timestamp</th>
          <th class="table-header">Author</th>
          <th class="table-header">Views</th>
          <th class="table-header">uh huh</th>
          <th class="table-header">status</th>
        </tr>
      </thead>

      <tbody>
        <tr class="table-row">
          <td>Intro to CSS</td>
          <td>Adam</td>
          <td>858</td>
          <td>low</td>
          <td>high</td>
        </tr>

        <tr class="table-row">
          <td>
            A Long Tour
          </td>
          <td>Adam</td>
          <td>112</td>
          <td>low</td>
          <td>high</td>
        </tr>

      </tbody>
    </table>

    {{data}}
  </div>
</template>

<script>
export default {
  name: "table",
  props: ["data"]
};
</script>

<style scoped>
.container {
    @apply mx-2 w-full my-8 flex justify-center justify-self-center;
}

.table-header {
    @apply w-28 text-blue-400 mb-16;
}

.table-row {
    @apply my-8;
}

</style>
