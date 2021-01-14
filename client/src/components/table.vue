<template>
  <div class="container">
    <table class="table-auto">
      <thead>
        <tr>
          <th class="table-header">Timestamp</th>
          <th class="table-header">Numb Plate</th>
          <th class="table-header">Bus ID</th>
          <th class="table-header">Station</th>
          <th class="table-header">Destination</th>
        </tr>
      </thead>

      <tbody>
        <tr class="table-row" v-for="row in data" v-bind:key="row.id">
          <td>{{row.timestamp}}</td>
          <td>{{row.vehicle_num_plate}}</td>
          <td>{{row.line_name}}</td>
          <td>{{row.station_name}}</td>
          <td>{{row.destination_name}}</td>
        </tr>
      </tbody>
    </table>

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
